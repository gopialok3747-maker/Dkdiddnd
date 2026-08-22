#!/usr/bin/env python3
"""
FINAL HYBRID SMS PANEL MONITOR + TELEGRAM BOT
SMS Time Parse + Start Time Fix
"""

import os
import json
import re
import html
import time
import base64
import asyncio
import httpx
import aiosqlite
from pathlib import Path
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# =====================================================================
# BASE DIR & FOLDER CREATION (FIX FOR RAILWAY ERROR)
# =====================================================================
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# =====================================================================
# CONFIG
# =====================================================================
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN missing in env!")

SUPER_ADMIN_ID = int(os.getenv("SUPER_ADMIN_ID", "0"))
ADMIN_CHAT_IDS = set(map(int, os.getenv("ADMIN_CHAT_IDS", "").split(",")) if os.getenv("ADMIN_CHAT_IDS") else [])

TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

CONFIG = {
    "global_concurrency": int(os.getenv("GLOBAL_CONCURRENCY", "200")),
    "per_panel_concurrency": int(os.getenv("PER_PANEL_CONCURRENCY", "20")),
    "poll_interval": int(os.getenv("POLL_INTERVAL", "5")),
    "max_age_minutes": int(os.getenv("MESSAGE_MAX_AGE_MINUTES", "15")),
    "request_timeout": int(os.getenv("REQUEST_TIMEOUT", "15")),
}

ALLOWED_SENDER = "BIGCITY"
BLOCKED_TERMS = ["JK-IESOUS-S", "DIGICREDIT", "IESOUS"]

PANELS_PATH = DATA_DIR / "panels.json"
DB_PATH = DATA_DIR / "monitor.db"
STATUS_PATH = DATA_DIR / "monitor_status.json"
APPROVAL_FILE = DATA_DIR / "approved_users.json"
PENDING_FILE = DATA_DIR / "pending_users.json"
CHAT_STATE_FILE = DATA_DIR / "chat_state.json"

# =====================================================================
# DATABASE
# =====================================================================
db = None

async def init_db():
    global db
    try:
        db = await aiosqlite.connect(DB_PATH)
        await db.execute("""CREATE TABLE IF NOT EXISTS processed_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            panel TEXT NOT NULL,
            device TEXT NOT NULL,
            message_id TEXT NOT NULL,
            sms_datetime TEXT,
            processed_at INTEGER,
            status TEXT,
            UNIQUE(panel, device, message_id)
        )""")
        await db.execute("CREATE INDEX IF NOT EXISTS idx_panel_device ON processed_messages(panel, device)")
        await db.execute("CREATE INDEX IF NOT EXISTS idx_status ON processed_messages(status)")
        await db.commit()
    except Exception as e:
        print(f"Database Error: {e}")
        db = None

async def db_get(sql, params=()):
    if not db: return None
    cursor = await db.execute(sql, params)
    return await cursor.fetchone()

async def db_all(sql, params=()):
    if not db: return []
    cursor = await db.execute(sql, params)
    return await cursor.fetchall()

async def db_run(sql, params=()):
    if not db: return None
    cursor = await db.execute(sql, params)
    await db.commit()
    return cursor.lastrowid

# =====================================================================
# STATE & METRICS
# =====================================================================
state = {
    "metrics": {
        "panels_total": 0, "panels_active": 0,
        "devices_total": 0, "devices_online": 0,
        "requests_total": 0, "requests_failed": 0,
        "messages_detected": 0, "messages_sent": 0,
        "messages_failed": 0, "duplicates_ignored": 0,
        "old_ignored": 0, "filtered_ignored": 0,
        "panel_status": {}
    }
}

# =====================================================================
# TELEGRAM HELPERS
# =====================================================================
async def tg(method: str, **params):
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(f"{TELEGRAM_API}/{method}", json=params)
            j = r.json()
            return j.get("result") if j.get("ok") else None
    except Exception:
        return None

async def send(chat_id, text, keyboard=None, reply_to=None):
    params = {"chat_id": chat_id, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True}
    if reply_to: params["reply_to_message_id"] = reply_to
    if keyboard: params["reply_markup"] = {"inline_keyboard": keyboard}
    return await tg("sendMessage", **params)

async def edit(chat_id, message_id, text, keyboard=None):
    params = {"chat_id": chat_id, "message_id": message_id, "text": text, "parse_mode": "HTML"}
    if keyboard: params["reply_markup"] = {"inline_keyboard": keyboard}
    return await tg("editMessageText", **params)

async def get_updates(offset):
    return await tg("getUpdates", offset=offset, timeout=25) or []

# =====================================================================
# STORAGE HELPERS
# =====================================================================
def load_json(path, default=None):
    try:
        with open(path, "r", encoding="utf-8") as f: return json.load(f)
    except: return default or {}

def save_json(path, data):
    try:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: json.dump(data, f, indent=2)
    except:
        pass

def load_panels(): return load_json(PANELS_PATH, {})
def save_panels(panels): save_json(PANELS_PATH, panels)
def load_approved(): return load_json(APPROVAL_FILE, {})
def save_approved(u): save_json(APPROVAL_FILE, u)
def load_pending(): return load_json(PENDING_FILE, {})
def save_pending(u): save_json(PENDING_FILE, u)
def load_state(): return load_json(CHAT_STATE_FILE, {})
def save_state(u): save_json(CHAT_STATE_FILE, u)

# =====================================================================
# PANEL DECODER
# =====================================================================
KEY = "ZXKAIv1_Xk9mP2wN7qL4vR6jH3cF8yT1ZbE5sA09"

def decode_zxkai(link):
    m = re.search(r"s=([^&]+)", link)
    if not m: return None
    s = m.group(1)
    b64 = s.replace("-", "+").replace("_", "/")
    b64 += "=" * (-len(b64) % 4)
    try:
        raw = base64.b64decode(b64)
        dec = bytes(b ^ KEY[i % len(KEY)].encode()[0] for i, b in enumerate(raw))
        obj = json.loads(dec)
        return obj.get("u", ""), obj.get("k", "")
    except: return None

def parse_panel_link(link):
    link = link.strip().strip("<>")
    d = decode_zxkai(link)
    if d and d[0] and d[1]: return d
    m = re.search(r"(https://[^/?]+firebaseio\.com)", link)
    if not m: return None
    url = m.group(1)
    auth = re.search(r"auth=([A-Za-z0-9_\-]+)", link)
    return url, (auth.group(1) if auth else "")

def label_from_url(url):
    m = re.search(r"https://([a-z0-9\-]+)\.firebaseio\.com", url)
    return m.group(1) if m else url

# =====================================================================
# BOT KEYBOARDS
# =====================================================================
def main_keyboard(user_id):
    kb = [[{"text": "📊 Status", "callback_data": "status"}],
          [{"text": "📋 My Panels", "callback_data": "mypanels"}],
          [{"text": "➕ Add Panel", "callback_data": "add"}],
          [{"text": "❌ Remove Panel", "callback_data": "remove"}]]
    if is_admin(user_id):
        kb.append([{"text": "👥 User Management", "callback_data": "user_mgmt"}])
        kb.append([{"text": "📊 Admin Dashboard", "callback_data": "admin_dashboard"}])
    return kb

def admin_keyboard():
    return [[{"text": "📋 Pending Requests", "callback_data": "pending_requests"}],
            [{"text": "👥 Approved Users", "callback_data": "approved_users"}],
            [{"text": "➕ Add Admin", "callback_data": "add_admin"}],
            [{"text": "🔙 Back", "callback_data": "back"}]]

# =====================================================================
# BOT USERS & COMMANDS
# =====================================================================
def is_super_admin(uid): return uid == SUPER_ADMIN_ID
def is_admin(uid): return uid == SUPER_ADMIN_ID or uid in ADMIN_CHAT_IDS
def is_approved(uid): return str(uid) in load_approved()

async def cmd_start(chat_id, message_id):
    # Current IST time nikaalo
    ist_time = datetime.utcnow() + timedelta(hours=5, minutes=30)
    current_time_str = ist_time.strftime("%I:%M %p")
    
    if not is_approved(chat_id) and not is_admin(chat_id):
        pending = load_pending()
        if str(chat_id) in pending:
            await send(chat_id, "⏳ Request pending hai babu! Admin approve karega.", reply_to=message_id)
            return
        kb = [[{"text": "📨 Request Access", "callback_data": "request_access"}]]
        await send(chat_id, f"🔒 <b>Ghare Jake Sutt Babu!</b>\n\nYe bot sirf authorized users ke liye hai.\n\n🆔 Your ID: <code>{chat_id}</code>\n\n📱 <b>Current Time:</b> {current_time_str}\n\nNeeche button dabao aur access request karo.", keyboard=kb, reply_to=message_id)
        return
    await send(chat_id, "🤖 <b>Hybrid SMS Panel Monitor</b>\n\n✅ 200+ Panels Supported\n✅ Real-time Promo Detection\n\n📱 <b>Current Time:</b> {current_time_str}\n\nButtons use karo babu!", keyboard=main_keyboard(chat_id))

async def handle_status(chat_id, message_id):
    status = load_json(STATUS_PATH, {})
    text = f"📊 <b>LIVE DASHBOARD</b>\n\n📡 Panels: {status.get('panels_total', 0)}\n📦 Devices: {status.get('devices_total', 0)}\n🟢 Online: {status.get('devices_online', 0)}\n📨 Messages: {status.get('messages_detected', 0)}\n📩 Sent: {status.get('messages_sent', 0)}\n\n⚡ Success Rate: {status.get('requests_total', 0) - status.get('requests_failed', 0)}/{status.get('requests_total', 0)}"
    kb = [[{"text": "🔄 Refresh", "callback_data": "refresh"}], [{"text": "🔙 Back", "callback_data": "back"}]]
    await edit(chat_id, message_id, text, kb)

async def handle_admin_dashboard(chat_id, message_id):
    if not is_admin(chat_id): return
    status = load_json(STATUS_PATH, {})
    approved = load_approved()
    pending = load_pending()
    panels = load_panels()
    text = f"👑 <b>ADMIN COMMAND DECK</b>\n━━━━━━━━━━━━━━━━━━━━\n📊 <b>SYSTEM</b>\n{status.get('panels_total', 0)} Panels • {status.get('devices_total', 0)} Devices\n\n👥 <b>USERS</b>\n{len(approved)} Approved • {len(pending)} Pending\n\n📨 <b>ACTIVITY</b>\n{status.get('messages_detected', 0)} Detected • {status.get('messages_sent', 0)} Processed\n\n🟢 <b>HEALTH</b>\n{max(0, int((status.get('requests_total', 0) - status.get('requests_failed', 0)) / max(status.get('requests_total', 1), 1) * 100))}% System Health\n\n━━━━━━━━━━━━━━━━━━━━\n👑 <b>Super Admin:</b> Ghare Jake Sutt Babu! 😆"
    kb = [[{"text": "🔄 Refresh", "callback_data": "admin_dashboard"}], [{"text": "🔙 Back", "callback_data": "back"}]]
    await edit(chat_id, message_id, text, kb)

async def handle_mypanels(chat_id, message_id):
    panels = load_panels()
    if not panels:
        await edit(chat_id, message_id, "📭 No panels babu!", main_keyboard(chat_id))
        return
    text = "📋 <b>MY PANELS</b>\n\n"
    for i, (name, p) in enumerate(panels.items(), 1):
        text += f"{i}. {html.escape(name)} (<code>{p['url'][:30]}...</code>)\n"
    await edit(chat_id, message_id, text, main_keyboard(chat_id))

async def handle_add(chat_id, message_id):
    state = load_state()
    state[str(chat_id)] = "add"
    save_state(state)
    await edit(chat_id, message_id, "➕ <b>Add Panel</b>\n\nPanel link bhejo babu!", [[{"text": "🔙 Back", "callback_data": "back"}]])

async def handle_remove(chat_id, message_id):
    panels = load_panels()
    if not panels:
        await edit(chat_id, message_id, "📭 No panels!", main_keyboard(chat_id))
        return
    kb = [[{"text": f"❌ {i}. {name[:28]}", "callback_data": f"rm:{i}"}] for i, name in enumerate(panels.keys(), 1)]
    kb.append([{"text": "🔙 Back", "callback_data": "back"}])
    await edit(chat_id, message_id, "❌ <b>Remove Panel</b>", kb)

async def handle_user_management(chat_id, message_id):
    if not is_admin(chat_id): return
    pending = load_pending()
    approved = load_approved()
    text = f"👥 <b>User Management</b>\n\n⏳ Pending: {len(pending)}\n✅ Approved: {len(approved)}\n👤 Admins: {len(ADMIN_CHAT_IDS) + 1}"
    await edit(chat_id, message_id, text, admin_keyboard())

async def handle_pending(chat_id, message_id):
    if not is_admin(chat_id): return
    pending = load_pending()
    if not pending:
        await edit(chat_id, message_id, "📭 No pending requests!", admin_keyboard())
        return
    kb = []
    for uid, info in list(pending.items())[:10]:
        kb.append([{"text": f"✅ Approve {uid[:6]}", "callback_data": f"approve:{uid}"},
                   {"text": f"❌ Reject {uid[:6]}", "callback_data": f"reject:{uid}"}])
    kb.append([{"text": "🔙 Back", "callback_data": "user_mgmt"}])
    await edit(chat_id, message_id, "⏳ <b>Pending Requests</b>", kb)

async def request_access(chat_id, username, first_name):
    pending = load_pending()
    approved = load_approved()
    if str(chat_id) in approved:
        await send(chat_id, "✅ Already approved! /start karo.")
        return
    if str(chat_id) in pending:
        await send(chat_id, "⏳ Already pending!")
        return
    pending[str(chat_id)] = {"chat_id": chat_id, "username": username, "name": first_name, "time": time.strftime("%Y-%m-%d %H:%M:%S")}
    save_pending(pending)
    await send(chat_id, "📨 <b>Access Request Sent!</b>\n\nTumhara request admin ke paas bhej diya hai.\nApprove hote hi notification milega.\n\nThoda sabar rakho babu! 😊")
    text = f"🆕 <b>Naya Access Request Aaya Hai!</b>\n\n👤 Name: {first_name or username}\n🆔 User ID: <code>{chat_id}</code>\n\n📋 Pending Requests me check karo."
    kb = [[{"text": "📋 View Pending", "callback_data": "pending_requests"}]]
    await send(SUPER_ADMIN_ID, text, keyboard=kb)
    for admin_id in ADMIN_CHAT_IDS:
        await send(admin_id, text, keyboard=kb)

async def approve_user(uid, approver_id):
    pending = load_pending()
    approved = load_approved()
    if uid not in pending: return False
    info = pending[uid]
    approved[uid] = {"chat_id": info.get("chat_id"), "name": info.get("name"), "approved_at": time.strftime("%Y-%m-%d %H:%M:%S")}
    save_approved(approved)
    del pending[uid]
    save_pending(pending)
    if info.get("chat_id"):
        await send(info.get("chat_id"), "🎉 <b>Ujala Follows My Brother!</b>\n\nTumhara access approve ho gaya hai!\nAb tum bot use kar sakte ho.\n\nSend /start to begin.\n\nWelcome babu! 🎊")
    return True

async def reject_user(uid):
    pending = load_pending()
    if uid not in pending: return
    info = pending[uid]
    del pending[uid]
    save_pending(pending)
    if info.get("chat_id"):
        await send(info.get("chat_id"), "❌ <b>Access Denied</b>\n\nTumhara request reject kar diya gaya hai.\n\nSorry babu! 😔")

# =====================================================================
# MONITOR ENGINE
# =====================================================================
async def fetch_json(client, url):
    try:
        r = await client.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=CONFIG["request_timeout"])
        if r.status_code != 200: raise Exception(f"HTTP {r.status_code}")
        state["metrics"]["requests_total"] += 1
        return r.json()
    except Exception as e:
        state["metrics"]["requests_failed"] += 1
        raise e

def format_promo(panel_name, device, sender, message, datetime):
    original = str(message or "").strip()
    combined = f"{sender} {original}".upper()
    if ALLOWED_SENDER not in combined: return None
    for term in BLOCKED_TERMS:
        if term in combined: return None
    promo_context = re.search(r'(?:reward|promo|coupon|voucher|redemption)\s*(?:code|coupon)?', original, re.IGNORECASE)
    if not promo_context: return None
    tail = original[promo_context.end(): promo_context.end() + 120]
    promo_match = re.search(r'\b[A-Z0-9]{8,24}\b', tail)
    if not promo_match: return None
    code = promo_match.group(0)
    redeem = re.search(r'https?://[^\s]+', original)
    campaign_m = re.search(r'(?:for|from)\s+(.{2,80}?)\s+(?:is|code|promo)\b', original, re.IGNORECASE)
    campaign = campaign_m.group(1).strip() if campaign_m else ""
    txt = f"🎁 <b>PROMO CODE RECEIVED</b>\n━━━━━━━━━━━━━━\n"
    if campaign: txt += f"🏷️ Campaign: <b>{campaign}</b>\n"
    txt += f"🎟️ Code: <code>{code}</code>\n"
    if redeem: txt += f"🔗 Redeem: {redeem.group(0)}\n"
    txt += f"👤 Sender: <code>{sender}</code>\n"
    txt += f"🔗 Panel: <b>{panel_name}</b>\n"
    if datetime: txt += f"🕒 {datetime}\n"
    txt += f"\n📝 <b>Message:</b>\n<code>{original[:300]}</code>"
    return txt

class MonitorEngine:
    def __init__(self):
        self.monitors = {}
        self.running = True
        self.last_poll = 0
        self.semaphore = asyncio.Semaphore(CONFIG["global_concurrency"])
        self.notification_queue = asyncio.Queue()

    async def start_notification_worker(self):
        while True:
            item = await self.notification_queue.get()
            panel, device, mid, formatted, dt = item
            for chat_id in ADMIN_CHAT_IDS:
                await send(chat_id, formatted)
                await asyncio.sleep(0.1)
            state["metrics"]["messages_sent"] += 1
            await db_run("INSERT OR IGNORE INTO processed_messages (panel, device, message_id, sms_datetime, processed_at, status) VALUES (?, ?, ?, ?, ?, ?)", (panel, device, mid, dt, int(time.time()), 'sent'))

    async def establish_baseline(self):
        panels = load_panels()
        for name in panels:
            rows = await db_all("SELECT device, message_id FROM processed_messages WHERE panel = ?", (name,))
            dm = {}
            for r in rows: dm.setdefault(r[0], set()).add(r[1])
            self.monitors[name] = {"devices": dm}

    async def run_engine(self):
        await self.establish_baseline()
        asyncio.create_task(self.start_notification_worker())
        while self.running:
            now = time.time()
            if now - self.last_poll < CONFIG["poll_interval"]:
                await asyncio.sleep(0.5); continue
            self.last_poll = now
            panels = load_panels()
            state["metrics"]["panels_total"] = len(panels)
            if not panels:
                await asyncio.sleep(CONFIG["poll_interval"]); continue
            tasks = [self.process_panel(name, p) for name, p in panels.items()]
            await asyncio.gather(*tasks, return_exceptions=True)
            await self.update_status()

    async def process_panel(self, name, panel):
        async with self.semaphore:
            try:
                url, key = panel.get("url"), panel.get("key", "")
                auth = f"?auth={key}" if key else ""
                monitor = self.monitors.setdefault(name, {"devices": {}})
                async with httpx.AsyncClient() as client:
                    clients = await fetch_json(client, f"{url}/clients.json{auth}")
                if not isinstance(clients, dict): return
                online = [d for d, info in clients.items() if info and info.get("status") == True]
                state["metrics"]["panel_status"][name] = {"online": len(online), "total": len(clients), "active": True}
                state["metrics"]["devices_total"] += len(clients)
                state["metrics"]["devices_online"] += len(online)
                await asyncio.gather(*[self.process_device(name, d, panel, monitor) for d in online], return_exceptions=True)
            except Exception as e:
                print(f"Panel Error {name}: {e}")

    async def process_device(self, name, device, panel, monitor):
        async with self.semaphore:
            try:
                url, key = panel.get("url"), panel.get("key", "")
                auth = f"?auth={key}" if key else ""
                baseline = monitor["devices"].setdefault(device, set())
                async with httpx.AsyncClient() as client:
                    messages = await fetch_json(client, f"{url}/messages/{device}.json{auth}")
                if not isinstance(messages, dict): return
                for mid, data in messages.items():
                    if not isinstance(data, dict) or data.get("type") != "incoming": continue
                    if mid in baseline:
                        state["metrics"]["duplicates_ignored"] += 1; continue
                    sms_time = data.get("dateTime", "")
                    formatted = format_promo(name, device, data.get("sender", "?"), data.get("message", ""), sms_time)
                    if not formatted:
                        await db_run("INSERT OR IGNORE INTO processed_messages (panel, device, message_id, status) VALUES (?, ?, ?, 'filtered')", (name, device, mid))
                        baseline.add(mid); continue
                    state["metrics"]["messages_detected"] += 1
                    await self.notification_queue.put((name, device, mid, formatted, sms_time))
                    baseline.add(mid)
                    print(f"📨 Detected: {device}")
            except Exception as e:
                pass

    async def update_status(self):
        status = {"timestamp": int(time.time() * 1000), **state["metrics"]}
        save_json(STATUS_PATH, status)

# =====================================================================
# BOT CALLBACK HANDLERS
# =====================================================================
async def handle_callback(chat_id, message_id, query_id, data):
    if data == "request_access":
        await request_access(chat_id, "", "User")
    elif data.startswith("approve:"):
        if is_admin(chat_id): await approve_user(data.split(":")[1], chat_id)
    elif data.startswith("reject:"):
        if is_admin(chat_id): await reject_user(data.split(":")[1])
    elif data == "status" or data == "refresh":
        await handle_status(chat_id, message_id)
    elif data == "admin_dashboard":
        await handle_admin_dashboard(chat_id, message_id)
    elif data == "mypanels":
        await handle_mypanels(chat_id, message_id)
    elif data == "add":
        await handle_add(chat_id, message_id)
    elif data == "remove":
        await handle_remove(chat_id, message_id)
    elif data == "user_mgmt":
        await handle_user_management(chat_id, message_id)
    elif data == "pending_requests":
        await handle_pending(chat_id, message_id)
    elif data == "back":
        await edit(chat_id, message_id, "👍 Menu", main_keyboard(chat_id))
    elif data.startswith("rm:"):
        panels = load_panels()
        try:
            idx = int(data[3:]) - 1
            name = list(panels.keys())[idx]
            del panels[name]; save_panels(panels)
            await edit(chat_id, message_id, f"✅ {name} removed!", main_keyboard(chat_id))
        except:
            await edit(chat_id, message_id, "⚠️ Invalid", main_keyboard(chat_id))

async def handle_text(chat_id, text, message_id):
    if not is_approved(chat_id) and not is_admin(chat_id):
        await send(chat_id, "🔒 Access required!")
        return
    state = load_state()
    if state.get(str(chat_id)) == "add":
        links = re.split(r"[\s,;]+", text.strip())
        panels = load_panels()
        added = 0
        for link in links:
            res = parse_panel_link(link)
            if res:
                url, key = res
                name = label_from_url(url)
                if not any(p["url"] == url for p in panels.values()):
                    panels[name] = {"url": url, "key": key}
                    added += 1
        if added:
            save_panels(panels)
            await send(chat_id, f"✅ {added} panels added!", keyboard=main_keyboard(chat_id))
        else:
            await send(chat_id, "⚠️ Invalid link!", keyboard=main_keyboard(chat_id))
        state.pop(str(chat_id), None); save_state(state)
        return
    await send(chat_id, "Buttons use karo babu!", keyboard=main_keyboard(chat_id))

# =====================================================================
# MAIN LOOP
# =====================================================================
async def main():
    print("🚀 Starting Hybrid Monitor + Bot (Fast Speed)...")
    await init_db()
    
    engine = MonitorEngine()
    asyncio.create_task(engine.run_engine())
    
    offset = None
    while True:
        try:
            updates = await get_updates(offset)
            for u in updates:
                offset = u["update_id"] + 1
                if "callback_query" in u:
                    cb = u["callback_query"]
                    msg = cb.get("message")
                    if msg and "chat" in msg:
                        await handle_callback(msg["chat"]["id"], msg["message_id"], cb["id"], cb.get("data", ""))
                elif "message" in u:
                    m = u["message"]
                    chat_id = m["chat"]["id"]
                    text = m.get("text", "")
                    if text == "/start":
                        await cmd_start(chat_id, m["message_id"])
                    else:
                        await handle_text(chat_id, text, m["message_id"])
        except Exception as e:
            print(f"Bot Error: {e}")
            await asyncio.sleep(3)

if __name__ == "__main__":
    asyncio.run(main())
