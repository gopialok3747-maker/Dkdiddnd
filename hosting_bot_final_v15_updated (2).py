"""
𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐁𝐎𝐓 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 𝟒.𝟎 — 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐏𝐀𝐍𝐄𝐋
𝐂𝐘𝐁𝐄𝐑𝐏𝐔𝐍𝐊 + 𝐇𝐀𝐂𝐊𝐄𝐑 𝐓𝐄𝐑𝐌𝐈𝐍𝐀𝐋 + 𝐒𝐄𝐑𝐕𝐄𝐑 𝐑𝐀𝐂𝐊 𝐔𝐈
𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄: 𝐌𝐀𝐓𝐇𝐄𝐌𝐀𝐓𝐈𝐂𝐀𝐋 𝐁𝐎𝐋𝐃 𝐒𝐀𝐍𝐒-𝐒𝐄𝐑𝐈𝐅
"""

import subprocess
import sys
import os

# ✅ 𝐀𝐮𝐭𝐨-𝐢𝐧𝐬𝐭𝐚𝐥𝐥 𝐦𝐢𝐬𝐬𝐢𝐧𝐠 𝐦𝐨𝐝𝐮𝐥𝐞𝐬
def auto_install(package):
    try:
        __import__(package)
    except ModuleNotFoundError:
        print(f"📦 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐢𝐧𝐠 𝐦𝐢𝐬𝐬𝐢𝐧𝐠 𝐩𝐚𝐜𝐤𝐚𝐠𝐞: {package} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝: {package}")

# 𝐀𝐮𝐭𝐨-𝐢𝐧𝐬𝐭𝐚𝐥𝐥 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐦𝐨𝐝𝐮𝐥𝐞𝐬
for mod in ["telebot", "psutil", "requests", "flask", "qrcode", "Pillow", "cryptography"]:
    auto_install(mod)

# --- 𝐀𝐟𝐭𝐞𝐫 𝐚𝐮𝐭𝐨-𝐢𝐧𝐬𝐭𝐚𝐥𝐥, 𝐢𝐦𝐩𝐨𝐫𝐭 𝐚𝐥𝐥 𝐦𝐨𝐝𝐮𝐥𝐞𝐬 𝐬𝐚𝐟𝐞𝐥𝐲 ---
import telebot
import zipfile
import tempfile
import shutil
from telebot import types
import time
from datetime import datetime, timedelta
import psutil
import sqlite3
import json
import logging
import signal
import threading
import re
import atexit
import requests
from flask import Flask
from threading import Thread
import qrcode
from io import BytesIO
import hashlib
import random
import string
from cryptography.fernet import Fernet
import base64

app = Flask('')

@app.route('/')
def home():
    return "𝐈'𝐦 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐁𝐎𝐓"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
    print("✅ 𝐅𝐥𝐚𝐬𝐤 𝐊𝐞𝐞𝐩-𝐀𝐥𝐢𝐯𝐞 𝐬𝐞𝐫𝐯𝐞𝐫 𝐬𝐭𝐚𝐫𝐭𝐞𝐝.")

# ================================
# 𝐂𝐎𝐍𝐅𝐈𝐆𝐔𝐑𝐀𝐓𝐈𝐎𝐍
# ================================
TOKEN = os.environ.get('BOT_TOKEN', '8776958017:AAFLiq_MZ11ADeqgmbIcpe4Uk8ngz67NLdE')
OWNER_ID = int(os.environ.get('OWNER_ID', '8739344756'))
ADMIN_ID = OWNER_ID

if not TOKEN:
    raise SystemExit("❌ BOT_TOKEN not found.")
if OWNER_ID == 0:
    raise SystemExit("❌ OWNER_ID not set.")

# 𝐅𝐨𝐥𝐝𝐞𝐫 𝐬𝐞𝐭𝐮𝐩
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_BOTS_DIR = os.path.join(BASE_DIR, 'hosting_uploads')
HOSTING_DATA_DIR = os.path.join(BASE_DIR, 'hosting_data')
DATABASE_PATH = os.path.join(HOSTING_DATA_DIR, 'hosting_bot.db')
RUNNING_SCRIPTS_DB = os.path.join(HOSTING_DATA_DIR, 'running_scripts.json')

# 𝐓𝐈𝐄𝐑 𝐒𝐘𝐒𝐓𝐄𝐌
TIER_SYSTEM = {
    "full": {
        "name": "𝐅𝐔𝐋𝐋 𝐀𝐂𝐂𝐄𝐒𝐒",
        "upload_limit": float('inf'),
        "max_file_size": float('inf'),
        "icon": "🚀",
        "color": "#00ff00",
        "auto_restart": True
    }
}

# 𝐂𝐫𝐞𝐚𝐭𝐞 𝐧𝐞𝐜𝐞𝐬𝐬𝐚𝐫𝐲 𝐝𝐢𝐫𝐞𝐜𝐭𝐨𝐫𝐢𝐞𝐬
os.makedirs(UPLOAD_BOTS_DIR, exist_ok=True)
os.makedirs(HOSTING_DATA_DIR, exist_ok=True)

# 𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞 𝐛𝐨𝐭 (𝐜𝐥𝐚𝐬𝐬 𝐦𝐢𝐝𝐝𝐥𝐞𝐰𝐚𝐫𝐞 𝐞𝐧𝐚𝐛𝐥𝐞𝐝 𝐟𝐨𝐫 𝐩𝐞𝐫𝐬𝐨𝐧𝐚𝐥-𝐮𝐬𝐞 𝐥𝐨𝐜𝐤)
bot = telebot.TeleBot(TOKEN, use_class_middlewares=True)

# ================================
# 🔒 𝐏𝐄𝐑𝐒𝐎𝐍𝐀𝐋-𝐔𝐒𝐄 𝐋𝐎𝐂𝐊
# ================================
from telebot.handler_backends import BaseMiddleware, CancelUpdate

class OwnerOnlyMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.update_types = ['message', 'callback_query']

    def pre_process(self, update, data):
        user = getattr(update, 'from_user', None)
        if user is None or (user.id != OWNER_ID and user.id not in active_users):
            try:
                if hasattr(update, 'text') or hasattr(update, 'document'):
                    bot.reply_to(update, "🔒 𝐓𝐡𝐢𝐬 𝐛𝐨𝐭 𝐢𝐬 𝐩𝐫𝐢𝐯𝐚𝐭𝐞 𝐚𝐧𝐝 𝐥𝐨𝐜𝐤𝐞𝐝 𝐭𝐨 𝐢𝐭𝐬 𝐨𝐰𝐧𝐞𝐫 𝐨𝐧𝐥𝐲.")
                else:
                    bot.answer_callback_query(update.id, "🔒 𝐍𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝.", show_alert=True)
            except Exception:
                pass
            return CancelUpdate()
        return None

    def post_process(self, update, data, exception=None):
        pass

# bot.setup_middleware(OwnerOnlyMiddleware()) # Disabled to allow everyone

# --- 𝐃𝐚𝐭𝐚 𝐬𝐭𝐫𝐮𝐜𝐭𝐮𝐫𝐞𝐬 ---
bot_scripts = {}
# Per-script locks prevent concurrent RUN/STOP/RESTART/RESET races.
_script_locks = {}
_script_locks_guard = threading.RLock()
_state_file_lock = threading.RLock()
_reset_confirmations = {}

user_files = {}
active_users = set()
admin_ids = {OWNER_ID}
user_subscriptions = {}
admin_ids = {OWNER_ID}
bot_locked = False

# --- 𝐋𝐨𝐠𝐠𝐢𝐧𝐠 𝐒𝐞𝐭𝐮𝐩 ---
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ================================
# 𝐅𝐎𝐍𝐓 𝐂𝐎𝐍𝐕𝐄𝐑𝐒𝐈𝐎𝐍 𝐅𝐔𝐍𝐂𝐓𝐈𝐎𝐍𝐒
# ================================
def convert_to_bold_uppercase(text: str) -> str:
    """𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐭𝐞𝐱𝐭 𝐭𝐨 𝐦𝐚𝐭𝐡𝐞𝐦𝐚𝐭𝐢𝐜𝐚𝐥 𝐛𝐨𝐥𝐝 𝐬𝐚𝐧𝐬-𝐬𝐞𝐫𝐢𝐟"""
    bold_mapping = {
        'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆',
        'H': '𝐇', 'I': '𝐈', 'J': '𝐉', 'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍',
        'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓', 'U': '𝐔',
        'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙',
        'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠',
        'h': '𝐡', 'i': '𝐢', 'j': '𝐣', 'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧',
        'o': '𝐨', 'p': '𝐩', 'q': '𝐪', 'r': '𝐫', 's': '𝐬', 't': '𝐭', 'u': '𝐮',
        'v': '𝐯', 'w': '𝐰', 'x': '𝐱', 'y': '𝐲', 'z': '𝐳',
        '0': '𝟎', '1': '𝟏', '2': '𝟐', '3': '𝟑', '4': '𝟒', '5': '𝟓', '6': '𝟔',
        '7': '𝟕', '8': '𝟖', '9': '𝟗',
        ' ': ' ', '!': '!', '@': '@', '#': '#', '$': '$', '%': '%', '^': '^',
        '&': '&', '*': '*', '(': '(', ')': ')', '-': '-', '_': '_', '=': '=',
        '+': '+', '[': '[', ']': ']', '{': '{', '}': '}', '\\': '\\', '|': '|',
        ';': ';', ':': ':', "'": "'", '"': '"', ',': ',', '.': '.', '<': '<',
        '>': '>', '/': '/', '?': '?', '`': '`', '~': '~'
    }
    
    result = []
    for char in str(text):
        result.append(bold_mapping.get(char, char))
    return ''.join(result)

# 𝐀𝐥𝐢𝐚𝐬 𝐟𝐨𝐫 𝐞𝐚𝐬𝐲 𝐮𝐬𝐞
B = convert_to_bold_uppercase

def unbold(text: str) -> str:
    """𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐦𝐚𝐭𝐡𝐞𝐦𝐚𝐭𝐢𝐜𝐚𝐥 𝐛𝐨𝐥𝐝 𝐬𝐚𝐧𝐬-𝐬𝐞𝐫𝐢𝐟 𝐛𝐚𝐜𝐤 𝐭𝐨 𝐧𝐨𝐫𝐦𝐚𝐥 𝐭𝐞𝐱𝐭"""
    bold_to_normal = {
        '𝐀': 'A', '𝐁': 'B', '𝐂': 'C', '𝐃': 'D', '𝐄': 'E', '𝐅': 'F', '𝐆': 'G',
        '𝐇': 'H', '𝐈': 'I', '𝐉': 'J', '𝐊': 'K', '𝐋': 'L', '𝐌': 'M', '𝐍': 'N',
        '𝐎': 'O', '𝐏': 'P', '𝐐': 'Q', '𝐑': 'R', '𝐒': 'S', '𝐓': 'T', '𝐔': 'U',
        '𝐕': 'V', '𝐖': 'W', '𝐗': 'X', '𝐘': 'Y', '𝐙': 'Z',
        '𝐚': 'a', '𝐛': 'b', '𝐜': 'c', '𝐝': 'd', '𝐞': 'e', '𝐟': 'f', '𝐠': 'g',
        '𝐡': 'h', '𝐢': 'i', '𝐣': 'j', '𝐤': 'k', '𝐥': 'l', '𝐦': 'm', '𝐧': 'n',
        '𝐨': 'o', '𝐩': 'p', '𝐪': 'q', '𝐫': 'r', '𝐬': 's', '𝐭': 't', '𝐮': 'u',
        '𝐯': 'v', '𝐰': 'w', '𝐱': 'x', '𝐲': 'y', '𝐳': 'z',
        '𝟎': '0', '𝟏': '1', '𝟐': '2', '𝟑': '3', '𝟒': '4', '𝟓': '5', '𝟔': '6',
        '𝟕': '7', '𝟖': '8', '𝟗': '9'
    }
    result = []
    for char in str(text):
        result.append(bold_to_normal.get(char, char))
    return ''.join(result)


# ================================
# ╔═══════════════════════════════════╗
# ║  🎨 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍 𝐌𝐀𝐍𝐀𝐆𝐄𝐑    ║
# ║  Cyberpunk + Hacker Terminal      ║
# ║  Server Rack UI                   ║
# ╚═══════════════════════════════════╝
# ================================

# Animation lock to prevent concurrent edits on same message
_animation_locks = {}
_animation_lock_global = threading.Lock()

def _get_animation_lock(chat_id, message_id):
    key = f"{chat_id}_{message_id}"
    with _animation_lock_global:
        if key not in _animation_locks:
            _animation_locks[key] = threading.Lock()
        return _animation_locks[key]

def run_edit_animation(chat_id, message_id, frames, delay=0.3):
    """
    Run an edit_message_text animation on a single message.
    Uses threading lock to prevent race conditions.
    Each frame is edited every `delay` seconds.
    """
    lock = _get_animation_lock(chat_id, message_id)
    if not lock.acquire(blocking=False):
        # Another animation already running on this message
        return

    def _do_animation():
        try:
            for frame in frames:
                try:
                    bot.edit_message_text(frame, chat_id, message_id)
                except Exception:
                    pass
                time.sleep(delay)
        finally:
            lock.release()
            # Cleanup lock
            key = f"{chat_id}_{message_id}"
            with _animation_lock_global:
                if key in _animation_locks:
                    del _animation_locks[key]

    t = threading.Thread(target=_do_animation, daemon=True)
    t.start()
    return t


class AnimationManager:
    """
    ╔═══════════════════════════════════╗
    ║  𝐑𝐞𝐮𝐬𝐚𝐛𝐥𝐞 𝐀𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧 𝐌𝐚𝐧𝐚𝐠𝐞𝐫       ║
    ║  Premium Cyberpunk / Terminal     ║
    ║  animations for every bot action  ║
    ╚═══════════════════════════════════╝
    """

    # ═══════════════════════════════════
    # 🚀 𝐔𝐏𝐋𝐎𝐀𝐃 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍
    # ═══════════════════════════════════
    @staticmethod
    def animate_upload(chat_id, message_id):
        """Animated rocket upload with cyberpunk terminal header"""
        frames = [
            f"""╔══════════════════════════════════╗
║    🚀 𝐔𝐏𝐋𝐎𝐀𝐃 𝐒𝐄𝐐𝐔𝐄𝐍𝐂𝐄 𝐈𝐍𝐈𝐓𝐈𝐀𝐓𝐄𝐃  ║
╚══════════════════════════════════╝

> 𝐑𝐞𝐜𝐞𝐢𝐯𝐢𝐧𝐠 𝐩𝐚𝐜𝐤𝐞𝐭...
━━━━━━━━━━━━━━━━━━━━━━
🚀□□□□□□□□□□
[▰· · · · · · · · ·] 0%""",

            f"""╔══════════════════════════════════╗
║    🚀 𝐔𝐏𝐋𝐎𝐀𝐃 𝐒𝐄𝐐𝐔𝐄𝐍𝐂𝐄 𝐀𝐂𝐓𝐈𝐕𝐄     ║
╚══════════════════════════════════╝

> 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐝𝐚𝐭𝐚 𝐛𝐥𝐨𝐜𝐤𝐬...
━━━━━━━━━━━━━━━━━━━━━━
□🚀□□□□□□□□□
[▰▰· · · · · · · ·] 15%""",

            f"""╔══════════════════════════════════╗
║    🚀 𝐓𝐑𝐀𝐍𝐒𝐅𝐄𝐑 𝐈𝐍 𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒        ║
╚══════════════════════════════════╝

> 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠...
━━━━━━━━━━━━━━━━━━━━━━
□□🚀□□□□□□□□
[▰▰▰· · · · · · ·] 30%""",

            f"""╔══════════════════════════════════╗
║    🚀 𝐓𝐑𝐀𝐍𝐒𝐅𝐄𝐑 𝐈𝐍 𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒        ║
╚══════════════════════════════════╝

> 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠...
━━━━━━━━━━━━━━━━━━━━━━
□□□🚀□□□□□□□
[▰▰▰▰▰· · · · ·] 50%""",

            f"""╔══════════════════════════════════╗
║    🚀 𝐍𝐄𝐀𝐑𝐈𝐍𝐆 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐈𝐎𝐍          ║
╚══════════════════════════════════╝

> 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠...
━━━━━━━━━━━━━━━━━━━━━━
□□□□🚀□□□□□□
[▰▰▰▰▰▰▰· · ·] 70%""",

            f"""╔══════════════════════════════════╗
║    🚀 𝐍𝐄𝐀𝐑𝐈𝐍𝐆 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐈𝐎𝐍          ║
╚══════════════════════════════════╝

> 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠...
━━━━━━━━━━━━━━━━━━━━━━
□□□□□🚀□□□□□
[▰▰▰▰▰▰▰▰▰·] 85%""",

            f"""╔══════════════════════════════════╗
║    🚀 𝐅𝐈𝐍𝐀𝐋𝐈𝐙𝐈𝐍𝐆 𝐓𝐑𝐀𝐍𝐒𝐅𝐄𝐑         ║
╚══════════════════════════════════╝

> 𝐒𝐜𝐚𝐧𝐧𝐢𝐧𝐠 𝐢𝐦𝐩𝐨𝐫𝐭𝐬...
━━━━━━━━━━━━━━━━━━━━━━
□□□□□□🚀□□□□
[▰▰▰▰▰▰▰▰▰▰] 90%""",

            f"""╔══════════════════════════════════╗
║    📋 𝐂𝐑𝐄𝐀𝐓𝐈𝐍𝐆 𝐏𝐑𝐎𝐂𝐅𝐈𝐋𝐄...        ║
╚══════════════════════════════════╝

> 𝐂𝐫𝐞𝐚𝐭𝐢𝐧𝐠 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐦𝐞𝐧𝐭𝐬.𝐭𝐱𝐭...
> 𝐂𝐫𝐞𝐚𝐭𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐟𝐢𝐥𝐞...
━━━━━━━━━━━━━━━━━━━━━━
□□□□□□□🚀□□□
[▰▰▰▰▰▰▰▰▰▰] 98%""",

            f"""╔══════════════════════════════════╗
║    ✅ 𝐔𝐏𝐋𝐎𝐀𝐃 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄              ║
╠══════════════════════════════════╣
║  🎉 𝐅𝐢𝐥𝐞 𝐫𝐞𝐚𝐝𝐲 𝐟𝐨𝐫 𝐡𝐨𝐬𝐭𝐢𝐧𝐠!       ║
╚══════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━
□□□□□□□□🚀□□
[▰▰▰▰▰▰▰▰▰▰] 100%"""
        ]
        run_edit_animation(chat_id, message_id, frames, delay=0.3)

    # ═══════════════════════════════════
    # 💻 𝐁𝐎𝐓 𝐒𝐓𝐀𝐑𝐓𝐈𝐍𝐆 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍
    # ═══════════════════════════════════
    @staticmethod
    def animate_start(chat_id, message_id):
        """Terminal-style boot sequence animation"""
        frames = [
            f"""╔══════════════════════════════════╗
║  💻 𝐒𝐘𝐒𝐓𝐄𝐌 𝐁𝐎𝐎𝐓 𝐒𝐄𝐐𝐔𝐄𝐍𝐂𝐄         ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐈𝐍𝐈𝐓𝐈𝐀𝐋𝐈𝐙𝐈𝐍𝐆              ║
╚══════════════════════════════════╝

> 𝐁𝐨𝐨𝐭𝐢𝐧𝐠 𝐬𝐲𝐬𝐭𝐞𝐦...
[▰· · · · · · · · ·] 10%""",

            f"""╔══════════════════════════════════╗
║  💻 𝐒𝐘𝐒𝐓𝐄𝐌 𝐁𝐎𝐎𝐓 𝐒𝐄𝐐𝐔𝐄𝐍𝐂𝐄         ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐋𝐎𝐀𝐃𝐈𝐍𝐆                  ║
╚══════════════════════════════════╝

> 𝐁𝐨𝐨𝐭𝐢𝐧𝐠 𝐬𝐲𝐬𝐭𝐞𝐦...
> 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐦𝐨𝐝𝐮𝐥𝐞𝐬...
[▰▰▰· · · · · · ·] 30%""",

            f"""╔══════════════════════════════════╗
║  💻 𝐒𝐘𝐒𝐓𝐄𝐌 𝐁𝐎𝐎𝐓 𝐒𝐄𝐐𝐔𝐄𝐍𝐂𝐄         ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐋𝐎𝐀𝐃𝐈𝐍𝐆                  ║
╚══════════════════════════════════╝

> 𝐁𝐨𝐨𝐭𝐢𝐧𝐠 𝐬𝐲𝐬𝐭𝐞𝐦...
> 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐦𝐨𝐝𝐮𝐥𝐞𝐬...
> 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐧𝐠 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞...
[▰▰▰▰▰· · · · ·] 50%""",

            f"""╔══════════════════════════════════╗
║  💻 𝐒𝐘𝐒𝐓𝐄𝐌 𝐁𝐎𝐎𝐓 𝐒𝐄𝐐𝐔𝐄𝐍𝐂𝐄         ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐂𝐎𝐍𝐍𝐄𝐂𝐓𝐈𝐍𝐆               ║
╚══════════════════════════════════╝

> 𝐁𝐨𝐨𝐭𝐢𝐧𝐠 𝐬𝐲𝐬𝐭𝐞𝐦...
> 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐦𝐨𝐝𝐮𝐥𝐞𝐬...
> 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐧𝐠 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞...
> 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐬𝐞𝐫𝐯𝐢𝐜𝐞𝐬...
[▰▰▰▰▰▰▰· · ·] 70%""",

            f"""╔══════════════════════════════════╗
║  💻 𝐒𝐘𝐒𝐓𝐄𝐌 𝐁𝐎𝐎𝐓 𝐒𝐄𝐐𝐔𝐄𝐍𝐂𝐄         ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐕𝐄𝐑𝐈𝐅𝐘𝐈𝐍𝐆                ║
╚══════════════════════════════════╝

> 𝐁𝐨𝐨𝐭𝐢𝐧𝐠 𝐬𝐲𝐬𝐭𝐞𝐦...
> 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐦𝐨𝐝𝐮𝐥𝐞𝐬...
> 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐧𝐠 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞...
> 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐬𝐞𝐫𝐯𝐢𝐜𝐞𝐬...
> 𝐕𝐞𝐫𝐢𝐟𝐲𝐢𝐧𝐠 𝐞𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭...
[▰▰▰▰▰▰▰▰▰·] 90%""",

            f"""╔══════════════════════════════════╗
║  💻 𝐒𝐘𝐒𝐓𝐄𝐌 𝐁𝐎𝐎𝐓 𝐒𝐄𝐐𝐔𝐄𝐍𝐂𝐄         ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐋𝐀𝐔𝐍𝐂𝐇𝐈𝐍𝐆                ║
╚══════════════════════════════════╝

> 𝐋𝐚𝐮𝐧𝐜𝐡𝐢𝐧𝐠 𝐚𝐩𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐨𝐧...
[▰▰▰▰▰▰▰▰▰▰] 100%

━━━━━━━━━━━━━━━━━━━━━━
🟢 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐎𝐍𝐋𝐈𝐍𝐄"""
        ]
        run_edit_animation(chat_id, message_id, frames, delay=0.3)

    # ═══════════════════════════════════
    # 🛑 𝐒𝐓𝐎𝐏 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍
    # ═══════════════════════════════════
    @staticmethod
    def animate_stop(chat_id, message_id):
        """Stop script animation"""
        frames = [
            f"""╔══════════════════════════════════╗
║  🛑 𝐓𝐄𝐑𝐌𝐈𝐍𝐀𝐓𝐈𝐎𝐍 𝐒𝐄𝐐𝐔𝐄𝐍𝐂𝐄         ║
╚══════════════════════════════════╝

> 𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐬𝐭𝐨𝐩 𝐬𝐢𝐠𝐧𝐚𝐥...
[▰▰▰▰▰▰▰▰▰▰] 100%""",

            f"""╔══════════════════════════════════╗
║  🛑 𝐓𝐄𝐑𝐌𝐈𝐍𝐀𝐓𝐈𝐍𝐆 𝐏𝐑𝐎𝐂𝐄𝐒𝐒           ║
╚══════════════════════════════════╝

> 𝐓𝐞𝐫𝐦𝐢𝐧𝐚𝐭𝐢𝐧𝐠 𝐩𝐫𝐨𝐜𝐞𝐬𝐬...
[▰▰▰▰▰▰▰▰▰▰] 100%""",

            f"""╔══════════════════════════════════╗
║  🟢 𝐒𝐂𝐑𝐈𝐏𝐓 𝐒𝐓𝐎𝐏𝐏𝐄𝐃               ║
╚══════════════════════════════════╝

> 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐭𝐞𝐫𝐦𝐢𝐧𝐚𝐭𝐞𝐝.
[▰▰▰▰▰▰▰▰▰▰] 100%"""
        ]
        run_edit_animation(chat_id, message_id, frames, delay=0.3)

    # ═══════════════════════════════════
    # 🔄 𝐑𝐄𝐒𝐓𝐀𝐑𝐓 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍
    # ═══════════════════════════════════
    @staticmethod
    def animate_restart(chat_id, message_id):
        """Restart animation with spinning indicator"""
        frames = [
            f"""╔══════════════════════════════════╗
║  🔄 𝐑𝐄𝐒𝐓𝐀𝐑𝐓 𝐈𝐍𝐈𝐓𝐈𝐀𝐓𝐄𝐃            ║
╚══════════════════════════════════╝

◐ 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐬𝐞𝐫𝐯𝐢𝐜𝐞𝐬...
━━━━━━━━━━━━━━━━━━━━━━
[▰▰▰▰▰▰▰▰▰▰] 100%""",

            f"""╔══════════════════════════════════╗
║  🔄 𝐑𝐄𝐒𝐓𝐀𝐑𝐓 𝐈𝐍 𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒          ║
╚══════════════════════════════════╝

◓ 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐬𝐞𝐫𝐯𝐢𝐜𝐞𝐬...
━━━━━━━━━━━━━━━━━━━━━━
[▰▰▰▰▰▰▰▰▰▰] 100%""",

            f"""╔══════════════════════════════════╗
║  🔄 𝐑𝐄𝐒𝐓𝐀𝐑𝐓 𝐈𝐍 𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒          ║
╚══════════════════════════════════╝

◑ 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐬𝐞𝐫𝐯𝐢𝐜𝐞𝐬...
━━━━━━━━━━━━━━━━━━━━━━
[▰▰▰▰▰▰▰▰▰▰] 100%""",

            f"""╔══════════════════════════════════╗
║  🔄 𝐑𝐄𝐂𝐎𝐍𝐍𝐄𝐂𝐓𝐈𝐍𝐆 𝐒𝐄𝐑𝐕𝐈𝐂𝐄𝐒        ║
╚══════════════════════════════════╝

◒ 𝐑𝐞𝐜𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐧𝐠 𝐬𝐞𝐫𝐯𝐢𝐜𝐞𝐬...
━━━━━━━━━━━━━━━━━━━━━━
[▰▰▰▰▰▰▰▰▰▰] 100%""",

            f"""╔══════════════════════════════════╗
║  🟢 𝐑𝐄𝐒𝐓𝐀𝐑𝐓 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄             ║
╚══════════════════════════════════╝

🔄 𝐒𝐞𝐫𝐯𝐢𝐜𝐞𝐬 𝐫𝐞𝐜𝐨𝐧𝐧𝐞𝐜𝐭𝐞𝐝.
━━━━━━━━━━━━━━━━━━━━━━
🟢 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞"""
        ]
        run_edit_animation(chat_id, message_id, frames, delay=0.3)

    # ═══════════════════════════════════
    # 📦 𝐌𝐎𝐃𝐔𝐋𝐄 𝐈𝐍𝐒𝐓𝐀𝐋𝐋 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍
    # ═══════════════════════════════════
    @staticmethod
    def animate_install(chat_id, message_id):
        """Module installation animation"""
        frames = [
            f"""╔══════════════════════════════════╗
║  📦 𝐌𝐎𝐃𝐔𝐋𝐄 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐀𝐓𝐈𝐎𝐍          ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐈𝐍𝐆              ║
╚══════════════════════════════════╝

📦 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐩𝐚𝐜𝐤𝐚𝐠𝐞𝐬...
[▰▰▰· · · · · · ·] 30%""",

            f"""╔══════════════════════════════════╗
║  📦 𝐌𝐎𝐃𝐔𝐋𝐄 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐀𝐓𝐈𝐎𝐍          ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐄𝐗𝐓𝐑𝐀𝐂𝐓𝐈𝐍𝐆               ║
╚══════════════════════════════════╝

📥 𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐢𝐧𝐠...
[▰▰▰▰▰▰· · · ·] 60%""",

            f"""╔══════════════════════════════════╗
║  📦 𝐌𝐎𝐃𝐔𝐋𝐄 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐀𝐓𝐈𝐎𝐍          ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐈𝐍𝐆               ║
╚══════════════════════════════════╝

⚙ 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐢𝐧𝐠...
[▰▰▰▰▰▰▰▰▰·] 90%""",

            f"""╔══════════════════════════════════╗
║  📦 𝐌𝐎𝐃𝐔𝐋𝐄 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐀𝐓𝐈𝐎𝐍          ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐂𝐎𝐍𝐅𝐈𝐆𝐔𝐑𝐈𝐍𝐆              ║
╚══════════════════════════════════╝

🧩 𝐂𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐢𝐧𝐠...
[▰▰▰▰▰▰▰▰▰▰] 100%""",

            f"""╔══════════════════════════════════╗
║  ✅ 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐀𝐓𝐈𝐎𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄        ║
╚══════════════════════════════════╝

🟢 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲
━━━━━━━━━━━━━━━━━━━━━━
[▰▰▰▰▰▰▰▰▰▰] 100%"""
        ]
        run_edit_animation(chat_id, message_id, frames, delay=0.3)

    # ═══════════════════════════════════
    # 🔍 𝐒𝐂𝐀𝐍 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍
    # ═══════════════════════════════════
    @staticmethod
    def animate_scan(chat_id, message_id):
        """File scan / requirements detection animation"""
        frames = [
            f"""╔══════════════════════════════════╗
║  🔍 𝐅𝐈𝐋𝐄 𝐒𝐂𝐀𝐍 𝐈𝐍𝐈𝐓𝐈𝐀𝐓𝐄𝐃          ║
╚══════════════════════════════════╝

> 𝐒𝐜𝐚𝐧𝐧𝐢𝐧𝐠 𝐅𝐢𝐥𝐞𝐬...
████████████ 20%""",

            f"""╔══════════════════════════════════╗
║  🔍 𝐒𝐂𝐀𝐍 𝐈𝐍 𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒             ║
╚══════════════════════════════════╝

> 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐈𝐦𝐩𝐨𝐫𝐭𝐬...
████████████ 50%""",

            f"""╔══════════════════════════════════╗
║  🔍 𝐃𝐄𝐓𝐄𝐂𝐓𝐈𝐍𝐆 𝐃𝐄𝐏𝐄𝐍𝐃𝐄𝐍𝐂𝐈𝐄𝐒       ║
╚══════════════════════════════════╝

> 𝐃𝐞𝐭𝐞𝐜𝐭𝐢𝐧𝐠 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐦𝐞𝐧𝐭𝐬...
████████████ 75%""",

            f"""╔══════════════════════════════════╗
║  🔍 𝐎𝐏𝐓𝐈𝐌𝐈𝐙𝐈𝐍𝐆                    ║
╚══════════════════════════════════╝

> 𝐎𝐩𝐭𝐢𝐦𝐢𝐳𝐢𝐧𝐠...
████████████ 100%

✅ 𝐒𝐜𝐚𝐧 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞"""
        ]
        run_edit_animation(chat_id, message_id, frames, delay=0.3)

    # ═══════════════════════════════════
    # 🗑 𝐃𝐄𝐋𝐄𝐓𝐄 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍
    # ═══════════════════════════════════
    @staticmethod
    def animate_delete(chat_id, message_id):
        """Delete file animation"""
        frames = [
            f"""╔══════════════════════════════════╗
║  🗑 𝐃𝐄𝐋𝐄𝐓𝐈𝐎𝐍 𝐒𝐄𝐐𝐔𝐄𝐍𝐂𝐄           ║
╚══════════════════════════════════╝

📄 𝐅𝐢𝐥𝐞 𝐅𝐨𝐮𝐧𝐝
━━━━━━━━━━━━━━━━━━━━━━""",

            f"""╔══════════════════════════════════╗
║  💥 𝐑𝐄𝐌𝐎𝐕𝐈𝐍𝐆 𝐅𝐈𝐋𝐄                ║
╚══════════════════════════════════╝

💥 𝐑𝐞𝐦𝐨𝐯𝐢𝐧𝐠...
━━━━━━━━━━━━━━━━━━━━━━""",

            f"""╔══════════════════════════════════╗
║  🔥 𝐂𝐋𝐄𝐀𝐍𝐈𝐍𝐆 𝐃𝐀𝐓𝐀               ║
╚══════════════════════════════════╝

🔥 𝐂𝐥𝐞𝐚𝐧𝐢𝐧𝐠...
━━━━━━━━━━━━━━━━━━━━━━""",

            f"""╔══════════════════════════════════╗
║  ✅ 𝐃𝐄𝐋𝐄𝐓𝐈𝐎𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄           ║
╚══════════════════════════════════╝

🗑 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲
━━━━━━━━━━━━━━━━━━━━━━"""
        ]
        run_edit_animation(chat_id, message_id, frames, delay=0.3)

    # ═══════════════════════════════════
    # 📜 𝐋𝐎𝐆𝐒 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍
    # ═══════════════════════════════════
    @staticmethod
    def animate_logs(chat_id, message_id):
        """Logs loading animation"""
        frames = [
            f"""╔══════════════════════════════════╗
║  📜 𝐋𝐎𝐆 𝐑𝐄𝐀𝐃𝐄𝐑 𝐈𝐍𝐈𝐓𝐈𝐀𝐋𝐈𝐙𝐄𝐃       ║
╚══════════════════════════════════╝

> 𝐎𝐩𝐞𝐧𝐢𝐧𝐠 𝐥𝐨𝐠𝐬...""",

            f"""╔══════════════════════════════════╗
║  📜 𝐑𝐄𝐀𝐃𝐈𝐍𝐆 𝐋𝐎𝐆 𝐅𝐈𝐋𝐄            ║
╚══════════════════════════════════╝

> 𝐎𝐩𝐞𝐧𝐢𝐧𝐠 𝐥𝐨𝐠𝐬...
>> 𝐑𝐞𝐚𝐝𝐢𝐧𝐠 𝐥𝐚𝐭𝐞𝐬𝐭 𝐨𝐮𝐭𝐩𝐮𝐭...""",

            f"""╔══════════════════════════════════╗
║  📜 𝐃𝐈𝐒𝐏𝐋𝐀𝐘𝐈𝐍𝐆 𝐋𝐎𝐆𝐒              ║
╚══════════════════════════════════╝

> 𝐎𝐩𝐞𝐧𝐢𝐧𝐠 𝐥𝐨𝐠𝐬...
>> 𝐑𝐞𝐚𝐝𝐢𝐧𝐠 𝐥𝐚𝐭𝐞𝐬𝐭 𝐨𝐮𝐭𝐩𝐮𝐭...
>>> 𝐃𝐢𝐬𝐩𝐥𝐚𝐲𝐢𝐧𝐠 𝐥𝐨𝐠𝐬..."""
        ]
        run_edit_animation(chat_id, message_id, frames, delay=0.3)

    # ═══════════════════════════════════
    # 🛰 𝐑𝐄𝐂𝐎𝐕𝐄𝐑𝐘 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍
    # ═══════════════════════════════════
    @staticmethod
    def animate_recovery(chat_id, message_id):
        """Server recovery animation with server rack UI"""
        frames = [
            f"""╔══════════════════════════════════╗
║  🛰 𝐒𝐄𝐑𝐕𝐄𝐑 𝐑𝐄𝐂𝐎𝐕𝐄𝐑𝐘 𝐒𝐘𝐒𝐓𝐄𝐌      ║
╚══════════════════════════════════╝

🖥 𝐒𝐞𝐫𝐯𝐞𝐫 𝟏   🟢
🖥 𝐒𝐞𝐫𝐯𝐞𝐫 𝟐   🟢
🖥 𝐒𝐞𝐫𝐯𝐞𝐫 𝟑   🟡
🖥 𝐒𝐞𝐫𝐯𝐞𝐫 𝟒   🔄

> 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐢𝐧𝐠...""",

            f"""╔══════════════════════════════════╗
║  🛰 𝐒𝐄𝐑𝐕𝐄𝐑 𝐑𝐄𝐂𝐎𝐕𝐄𝐑𝐘 𝐒𝐘𝐒𝐓𝐄𝐌      ║
╚══════════════════════════════════╝

🖥 𝐒𝐞𝐫𝐯𝐞𝐫 𝟏   🟢
🖥 𝐒𝐞𝐫𝐯𝐞𝐫 𝟐   🟢
🖥 𝐒𝐞𝐫𝐯𝐞𝐫 𝟑   🟢
🖥 𝐒𝐞𝐫𝐯𝐞𝐫 𝟒   🟢

𝐂𝐏𝐔      ███████░░
𝐑𝐀𝐌      ██████░░░
𝐍𝐄𝐓𝐖𝐎𝐑𝐊  ████████░

> 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐢𝐧𝐠...""",

            f"""╔══════════════════════════════════╗
║  ✅ 𝐑𝐄𝐂𝐎𝐕𝐄𝐑𝐘 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄           ║
╚══════════════════════════════════╝

🖥 𝐒𝐞𝐫𝐯𝐞𝐫 𝟏   🟢
🖥 𝐒𝐞𝐫𝐯𝐞𝐫 𝟐   🟢
🖥 𝐒𝐞𝐫𝐯𝐞𝐫 𝟑   🟢
🖥 𝐒𝐞𝐫𝐯𝐞𝐫 𝟒   🟢

𝐂𝐏𝐔      ███████░░
𝐑𝐀𝐌      ██████░░░
𝐍𝐄𝐓𝐖𝐎𝐑𝐊  ████████░

𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞 ✅"""
        ]
        run_edit_animation(chat_id, message_id, frames, delay=0.3)

    # ═══════════════════════════════════
    # 📊 𝐃𝐀𝐒𝐇𝐁𝐎𝐀𝐑𝐃 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍
    # ═══════════════════════════════════
    @staticmethod
    def animate_dashboard(chat_id, message_id):
        """Premium hosting dashboard animation"""
        frames = [
            f"""╔══════════════════════════════════╗
║    ⚡ 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐃𝐀𝐒𝐇𝐁𝐎𝐀𝐑𝐃         ║
╚══════════════════════════════════╝

📡 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐧𝐠 𝐭𝐨 𝐬𝐞𝐫𝐯𝐞𝐫...
━━━━━━━━━━━━━━━━━━━━━━""",

            f"""╔══════════════════════════════════╗
║    ⚡ 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐃𝐀𝐒𝐇𝐁𝐎𝐀𝐑𝐃         ║
╚══════════════════════════════════╝

📡 𝐒𝐜𝐚𝐧𝐧𝐢𝐧𝐠 𝐦𝐞𝐭𝐫𝐢𝐜𝐬...
━━━━━━━━━━━━━━━━━━━━━━""",

            f"""╔══════════════════════════════════╗
║    ⚡ 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐃𝐀𝐒𝐇𝐁𝐎𝐀𝐑𝐃         ║
╚══════════════════════════════════╝

📊 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐝𝐚𝐬𝐡𝐛𝐨𝐚𝐫𝐝...
━━━━━━━━━━━━━━━━━━━━━━"""
        ]
        run_edit_animation(chat_id, message_id, frames, delay=0.25)

    # ═══════════════════════════════════
    # 🔄 𝐑𝐄𝐒𝐓𝐀𝐑𝐓 𝐁𝐎𝐓 (𝐅𝐔𝐋𝐋) 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍
    # ═══════════════════════════════════
    @staticmethod
    def animate_full_restart(chat_id, message_id):
        """Full bot restart animation with notifications"""
        frames = [
            f"""╔══════════════════════════════════╗
║  🚀 𝐅𝐔𝐋𝐋 𝐁𝐎𝐓 𝐑𝐄𝐒𝐓𝐀𝐑𝐓             ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐏𝐑𝐄𝐏𝐀𝐑𝐈𝐍𝐆                ║
╚══════════════════════════════════╝

📢 𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬...
[▰▰· · · · · · · ·] 20%""",

            f"""╔══════════════════════════════════╗
║  🚀 𝐅𝐔𝐋𝐋 𝐁𝐎𝐓 𝐑𝐄𝐒𝐓𝐀𝐑𝐓             ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐍𝐎𝐓𝐈𝐅𝐘𝐈𝐍𝐆                ║
╚══════════════════════════════════╝

📢 𝐍𝐨𝐭𝐢𝐟𝐲𝐢𝐧𝐠 𝐮𝐬𝐞𝐫𝐬...
[▰▰▰▰· · · · · ·] 40%""",

            f"""╔══════════════════════════════════╗
║  🚀 𝐅𝐔𝐋𝐋 𝐁𝐎𝐓 𝐑𝐄𝐒𝐓𝐀𝐑𝐓             ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐂𝐋𝐄𝐀𝐍𝐈𝐍𝐆                ║
╚══════════════════════════════════╝

🔧 𝐂𝐥𝐞𝐚𝐧𝐢𝐧𝐠 𝐮𝐩...
[▰▰▰▰▰▰· · · ·] 60%""",

            f"""╔══════════════════════════════════╗
║  🚀 𝐅𝐔𝐋𝐋 𝐁𝐎𝐓 𝐑𝐄𝐒𝐓𝐀𝐑𝐓             ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐒𝐇𝐔𝐓𝐓𝐈𝐍𝐆 𝐃𝐎𝐖𝐍           ║
╚══════════════════════════════════╝

🔧 𝐒𝐡𝐮𝐭𝐭𝐢𝐧𝐠 𝐝𝐨𝐰𝐧...
[▰▰▰▰▰▰▰▰· ·] 80%""",

            f"""╔══════════════════════════════════╗
║  🚀 𝐅𝐔𝐋𝐋 𝐁𝐎𝐓 𝐑𝐄𝐒𝐓𝐀𝐑𝐓             ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐑𝐄𝐒𝐓𝐀𝐑𝐓𝐈𝐍𝐆               ║
╚══════════════════════════════════╝

🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠...
[▰▰▰▰▰▰▰▰▰▰] 100%"""
        ]
        run_edit_animation(chat_id, message_id, frames, delay=0.5)

    # ═══════════════════════════════════
    # 📊 𝐃𝐀𝐒𝐇𝐁𝐎𝐀𝐑𝐃 𝐃𝐈𝐒𝐏𝐋𝐀𝐘 (𝐅𝐈𝐍𝐀𝐋)
    # ═══════════════════════════════════
    @staticmethod
    def show_dashboard(total_files, running_count, ram_pct, cpu_pct, total_users):
        """Generate the final premium dashboard text"""
        ram_bar = "█" * int(ram_pct / 10) + "░" * (10 - int(ram_pct / 10))
        cpu_bar = "█" * int(cpu_pct / 10) + "░" * (10 - int(cpu_pct / 10))
        
        return f"""╔══════════════════════════════════╗
║    ⚡ 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐃𝐀𝐒𝐇𝐁𝐎𝐀𝐑𝐃         ║
╚══════════════════════════════════╝

🟢 𝐒𝐭𝐚𝐭𝐮𝐬   : 𝐎𝐍𝐋𝐈𝐍𝐄
📂 𝐅𝐢𝐥𝐞𝐬    : {total_files:02}
🚀 𝐑𝐮𝐧𝐧𝐢𝐧𝐠  : {running_count:02}
💾 𝐑𝐀𝐌     : {ram_pct:.0f}% {ram_bar}
⚙ 𝐂𝐏𝐔     : {cpu_pct:.0f}% {cpu_bar}
👥 𝐔𝐬𝐞𝐫𝐬   : {total_users}
🌐 𝐍𝐞𝐭𝐰𝐨𝐫𝐤 : 𝐒𝐭𝐚𝐛𝐥𝐞

━━━━━━━━━━━━━━━━━━━━━━"""


# ================================
# 𝐀𝐔𝐓𝐎-𝐑𝐄𝐂𝐎𝐕𝐄𝐑𝐘 𝐒𝐘𝐒𝐓𝐄𝐌
# ================================
class AutoRecoverySystem:
    def __init__(self):
        self.running_scripts_file = RUNNING_SCRIPTS_DB
        
    def save_running_script(self, user_id: int, file_name: str, file_path: str, process_pid: int):
        """𝐒𝐚𝐯𝐞 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭 𝐢𝐧𝐟𝐨 𝐭𝐨 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
        try:
            if os.path.exists(self.running_scripts_file):
                with open(self.running_scripts_file, 'r') as f:
                    data = json.load(f)
            else:
                data = {"running_scripts": []}
            
            # 𝐑𝐞𝐦𝐨𝐯𝐞 𝐝𝐮𝐩𝐥𝐢𝐜𝐚𝐭𝐞𝐬
            data["running_scripts"] = [script for script in data["running_scripts"] 
                                     if not (script["user_id"] == user_id and script["file_name"] == file_name)]
            
            # 𝐀𝐝𝐝 𝐧𝐞𝐰 𝐬𝐜𝐫𝐢𝐩𝐭
            script_info = {
                "user_id": user_id,
                "file_name": file_name,
                "file_path": file_path,
                "process_pid": process_pid,
                "start_time": datetime.now().isoformat(),
                "status": "running",
                "last_updated": datetime.now().isoformat()
            }
            
            data["running_scripts"].append(script_info)
            
            with open(self.running_scripts_file, 'w') as f:
                json.dump(data, f, indent=4)
                
            logger.info(f"💾 𝐒𝐚𝐯𝐞𝐝 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {user_id}/{file_name}")
            
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐚𝐯𝐢𝐧𝐠 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {e}")
    
    def remove_running_script(self, user_id: int, file_name: str):
        """𝐑𝐞𝐦𝐨𝐯𝐞 𝐬𝐜𝐫𝐢𝐩𝐭 𝐟𝐫𝐨𝐦 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
        try:
            if os.path.exists(self.running_scripts_file):
                with open(self.running_scripts_file, 'r') as f:
                    data = json.load(f)
                
                initial_count = len(data["running_scripts"])
                data["running_scripts"] = [script for script in data["running_scripts"] 
                                         if not (script["user_id"] == user_id and script["file_name"] == file_name)]
                
                if len(data["running_scripts"]) < initial_count:
                    with open(self.running_scripts_file, 'w') as f:
                        json.dump(data, f, indent=4)
                    logger.info(f"🗑️ 𝐑𝐞𝐦𝐨𝐯𝐞𝐝 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {user_id}/{file_name}")
                    
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐦𝐨𝐯𝐢𝐧𝐠 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {e}")
    
    def recover_all_scripts(self):
        """𝐑𝐞𝐜𝐨𝐯𝐞𝐫 𝐚𝐥𝐥 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐚𝐟𝐭𝐞𝐫 𝐜𝐫𝐚𝐬𝐡/𝐫𝐞𝐬𝐭𝐚𝐫𝐭"""
        try:
            if not os.path.exists(self.running_scripts_file):
                logger.info("📭 𝐍𝐨 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫")
                return []
            
            with open(self.running_scripts_file, 'r') as f:
                data = json.load(f)
            
            recovered = []
            for script in data.get("running_scripts", []):
                try:
                    user_id = script["user_id"]
                    file_name = script["file_name"]
                    file_path = script["file_path"]
                    
                    # Never recover a verified live process twice.
                    if is_bot_running(user_id, file_name):
                        logger.info(f"Skipping duplicate recovery for {user_id}/{file_name}")
                        continue

                    # 𝐂𝐡𝐞𝐜𝐤 𝐢𝐟 𝐟𝐢𝐥𝐞 𝐬𝐭𝐢𝐥𝐥 𝐞𝐱𝐢𝐬𝐭𝐬
                    if not os.path.exists(file_path):
                        logger.warning(f"⚠️ 𝐅𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝 𝐟𝐨𝐫 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲: {file_path}")
                        continue
                    
                    # 𝐂𝐡𝐞𝐜𝐤 𝐢𝐟 𝐮𝐬𝐞𝐫 𝐬𝐭𝐢𝐥𝐥 𝐡𝐚𝐬 𝐟𝐢𝐥𝐞 𝐢𝐧 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
                    user_has_file = False
                    for fname, ftype in user_files.get(user_id, []):
                        if fname == file_name:
                            user_has_file = True
                            break
                    
                    if not user_has_file:
                        logger.warning(f"⚠️ 𝐔𝐬𝐞𝐫 {user_id} 𝐧𝐨 𝐥𝐨𝐧𝐠𝐞𝐫 𝐡𝐚𝐬 𝐟𝐢𝐥𝐞: {file_name}")
                        continue
                    
                    # 𝐂𝐡𝐞𝐜𝐤 𝐢𝐟 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐢𝐬 𝐞𝐧𝐚𝐛𝐥𝐞𝐝 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫
                    tier = get_user_tier(user_id)
                    auto_restart_enabled = TIER_SYSTEM[tier]['auto_restart']
                    
                    if not auto_restart_enabled:
                        logger.info(f"⏸️ 𝐀𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐝𝐢𝐬𝐚𝐛𝐥𝐞𝐝 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫 {user_id}")
                        continue
                    
                    # 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐬𝐜𝐫𝐢𝐩𝐭
                    user_folder = os.path.join(UPLOAD_BOTS_DIR, str(user_id))
                    file_ext = os.path.splitext(file_name)[1].lower()
                    
                    if file_ext == '.py':
                        threading.Thread(target=self._restart_py_script, 
                                       args=(user_id, file_path, user_folder, file_name)).start()
                    elif file_ext == '.js':
                        threading.Thread(target=self._restart_js_script,
                                       args=(user_id, file_path, user_folder, file_name)).start()
                    
                    recovered.append({
                        "user_id": user_id,
                        "file_name": file_name,
                        "status": "recovering"
                    })
                    
                    logger.info(f"🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {user_id}/{file_name}")
                    
                    time.sleep(1)  # 𝐀𝐯𝐨𝐢𝐝 𝐨𝐯𝐞𝐫𝐥𝐨𝐚𝐝
                    
                except Exception as e:
                    logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭 {script}: {e}")
            
            return recovered
            
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐢𝐧 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐬𝐲𝐬𝐭𝐞𝐦: {e}")
            return []
    
    def _restart_py_script(self, user_id: int, file_path: str, user_folder: str, file_name: str):
        """𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐏𝐲𝐭𝐡𝐨𝐧 𝐬𝐜𝐫𝐢𝐩𝐭"""
        try:
            script_key = f"{user_id}_{file_name}"
            
            if script_key in bot_scripts:
                logger.info(f"✅ 𝐒𝐜𝐫𝐢𝐩𝐭 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠: {file_name}")
                return
            
            log_file_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
            log_file = open(log_file_path, 'a', encoding='utf-8', errors='ignore')
            
            startupinfo = None
            if os.name == 'nt':
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE
            
            process = subprocess.Popen(
                [sys.executable, file_path],
                cwd=user_folder,
                stdout=log_file,
                stderr=log_file,
                stdin=subprocess.PIPE,
                startupinfo=startupinfo,
                encoding='utf-8',
                errors='ignore'
            )
            
            bot_scripts[script_key] = {
                'process': process,
                'log_file': log_file,
                'file_name': file_name,
                'user_id': user_id,
                'start_time': datetime.now(),
                'type': 'py',
                'script_key': script_key
            }
            
            # 𝐒𝐚𝐯𝐞 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
            self.save_running_script(user_id, file_name, file_path, process.pid)
            
            logger.info(f"✅ 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐞𝐝 𝐏𝐲𝐭𝐡𝐨𝐧 𝐬𝐜𝐫𝐢𝐩𝐭: {file_name} (𝐏𝐈𝐃: {process.pid})")
            
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐏𝐲𝐭𝐡𝐨𝐧 𝐬𝐜𝐫𝐢𝐩𝐭 {file_name}: {e}")
    
    def _restart_js_script(self, user_id: int, file_path: str, user_folder: str, file_name: str):
        """𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐉𝐒 𝐬𝐜𝐫𝐢𝐩𝐭"""
        try:
            script_key = f"{user_id}_{file_name}"
            
            if script_key in bot_scripts:
                logger.info(f"✅ 𝐒𝐜𝐫𝐢𝐩𝐭 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠: {file_name}")
                return
            
            log_file_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
            log_file = open(log_file_path, 'a', encoding='utf-8', errors='ignore')
            
            startupinfo = None
            if os.name == 'nt':
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE
            
            process = subprocess.Popen(
                ['node', file_path],
                cwd=user_folder,
                stdout=log_file,
                stderr=log_file,
                stdin=subprocess.PIPE,
                startupinfo=startupinfo,
                encoding='utf-8',
                errors='ignore'
            )
            
            bot_scripts[script_key] = {
                'process': process,
                'log_file': log_file,
                'file_name': file_name,
                'user_id': user_id,
                'start_time': datetime.now(),
                'type': 'js',
                'script_key': script_key
            }
            
            # 𝐒𝐚𝐯𝐞 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
            self.save_running_script(user_id, file_name, file_path, process.pid)
            
            logger.info(f"✅ 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐞𝐝 𝐉𝐒 𝐬𝐜𝐫𝐢𝐩𝐭: {file_name} (𝐏𝐈𝐃: {process.pid})")
            
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐉𝐒 𝐬𝐜𝐫𝐢𝐩𝐭 {file_name}: {e}")
    
    def get_running_count(self):
        """𝐆𝐞𝐭 𝐜𝐨𝐮𝐧𝐭 𝐨𝐟 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭𝐬"""
        try:
            if os.path.exists(self.running_scripts_file):
                with open(self.running_scripts_file, 'r') as f:
                    data = json.load(f)
                return len(data.get("running_scripts", []))
            return 0
        except:
            return 0

# 𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐬𝐲𝐬𝐭𝐞𝐦
recovery_system = AutoRecoverySystem()

# ================================
# 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 𝐒𝐄𝐓𝐔𝐏
# ================================
def init_db():
    """𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞 𝐭𝐡𝐞 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
    logger.info(f"📊 𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐢𝐧𝐠 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐚𝐭: {DATABASE_PATH}")
    try:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
        
        # 𝐂𝐫𝐞𝐚𝐭𝐞 𝐭𝐚𝐛𝐥𝐞𝐬
        
        
        c.execute('''CREATE TABLE IF NOT EXISTS user_files
                     (user_id INTEGER, file_name TEXT, file_type TEXT, uploaded_at TEXT,
                      PRIMARY KEY (user_id, file_name))''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS active_users
                     (user_id INTEGER PRIMARY KEY, username TEXT, first_join TEXT, last_seen TEXT)''')
        
        
        
        c.execute('''CREATE TABLE IF NOT EXISTS user_stats
                     (user_id INTEGER PRIMARY KEY, uploads_count INTEGER, 
                      scripts_run INTEGER, total_upload_size INTEGER)''')
        
        
        
        conn.commit()
        conn.close()
        logger.info("✅ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐢𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲.")
        
    except Exception as e:
        logger.error(f"❌ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐢𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐚𝐭𝐢𝐨𝐧 𝐞𝐫𝐫𝐨𝐫: {e}", exc_info=True)

def load_data():
    """𝐋𝐨𝐚𝐝 𝐝𝐚𝐭𝐚 𝐟𝐫𝐨𝐦 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
    logger.info("📥 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐝𝐚𝐭𝐚 𝐟𝐫𝐨𝐦 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞...")
    try:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
        
        
        
        # 𝐋𝐨𝐚𝐝 𝐮𝐬𝐞𝐫 𝐟𝐢𝐥𝐞𝐬
        c.execute('SELECT user_id, file_name, file_type FROM user_files')
        for user_id, file_name, file_type in c.fetchall():
            if user_id not in user_files:
                user_files[user_id] = []
            user_files[user_id].append((file_name, file_type))
        
        # 𝐋𝐨𝐚𝐝 𝐚𝐜𝐭𝐢𝐯𝐞 𝐮𝐬𝐞𝐫𝐬
        c.execute('SELECT user_id FROM active_users')
        active_users.update(user_id for (user_id,) in c.fetchall())
        
        
        
        conn.close()
        
        logger.info(f"✅ 𝐃𝐚𝐭𝐚 𝐥𝐨𝐚𝐝𝐞𝐝: {len(active_users)} 𝐮𝐬𝐞𝐫𝐬")
        
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐝𝐚𝐭𝐚: {e}", exc_info=True)

# 𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞 𝐃𝐁 𝐚𝐧𝐝 𝐋𝐨𝐚𝐝 𝐃𝐚𝐭𝐚
init_db()
load_data()

# ================================
# 𝐇𝐄𝐋𝐏𝐄𝐑 𝐅𝐔𝐍𝐂𝐓𝐈𝐎𝐍𝐒
# ================================
def get_user_folder(user_id):
    """𝐆𝐞𝐭 𝐨𝐫 𝐜𝐫𝐞𝐚𝐭𝐞 𝐮𝐬𝐞𝐫'𝐬 𝐟𝐨𝐥𝐝𝐞𝐫"""
    user_folder = os.path.join(UPLOAD_BOTS_DIR, str(user_id))
    os.makedirs(user_folder, exist_ok=True)
    return user_folder

def get_user_tier(user_id):
    return "full"

def get_user_file_limit(user_id):
    """𝐆𝐞𝐭 𝐟𝐢𝐥𝐞 𝐮𝐩𝐥𝐨𝐚𝐝 𝐥𝐢𝐦𝐢𝐭 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫"""
    tier = get_user_tier(user_id)
    return TIER_SYSTEM[tier]["upload_limit"]

def get_user_file_count(user_id):
    """𝐆𝐞𝐭 𝐧𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐟𝐢𝐥𝐞𝐬 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐛𝐲 𝐮𝐬𝐞𝐫"""
    return len(user_files.get(user_id, []))

def is_bot_running(user_id, file_name):
    """𝐂𝐡𝐞𝐜𝐤 𝐢𝐟 𝐚 𝐛𝐨𝐭 𝐬𝐜𝐫𝐢𝐩𝐭 𝐢𝐬 𝐜𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠"""
    script_key = f"{user_id}_{file_name}"
    script_info = bot_scripts.get(script_key)
    
    if script_info and script_info.get('process'):
        try:
            proc = psutil.Process(script_info['process'].pid)
            return proc.is_running() and proc.status() != psutil.STATUS_ZOMBIE
        except psutil.NoSuchProcess:
            # 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝, 𝐜𝐥𝐞𝐚𝐧 𝐮𝐩
            recovery_system.remove_running_script(user_id, file_name)
            if script_key in bot_scripts:
                del bot_scripts[script_key]
            return False
    return False

def kill_process_tree(process_info):
    """𝐊𝐢𝐥𝐥 𝐚 𝐩𝐫𝐨𝐜𝐞𝐬𝐬 𝐚𝐧𝐝 𝐚𝐥𝐥 𝐢𝐭𝐬 𝐜𝐡𝐢𝐥𝐝𝐫𝐞𝐧"""
    try:
        process = process_info.get('process')
        if process and hasattr(process, 'pid'):
            pid = process.pid
            try:
                parent = psutil.Process(pid)
                children = parent.children(recursive=True)
                
                for child in children:
                    try:
                        child.terminate()
                    except:
                        pass
                
                try:
                    parent.terminate()
                    parent.wait(timeout=3)
                except:
                    try:
                        parent.kill()
                    except:
                        pass
                
                # 𝐑𝐞𝐦𝐨𝐯𝐞 𝐟𝐫𝐨𝐦 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
                if 'user_id' in process_info and 'file_name' in process_info:
                    recovery_system.remove_running_script(
                        process_info['user_id'], 
                        process_info['file_name']
                    )
                
            except psutil.NoSuchProcess:
                pass
                
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐤𝐢𝐥𝐥𝐢𝐧𝐠 𝐩𝐫𝐨𝐜𝐞𝐬𝐬: {e}")

def send_restart_notification():
    """𝐒𝐞𝐧𝐝 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐭𝐨 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬"""
    logger.info("📢 𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬...")
    
    notification_text = B("""
🚨 *𝐈𝐌𝐏𝐎𝐑𝐓𝐀𝐍𝐓 𝐀𝐍𝐍𝐎𝐔𝐍𝐂𝐄𝐌𝐄𝐍𝐓*

𝐁𝐨𝐭 𝐢𝐬 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐟𝐨𝐫 𝐦𝐚𝐢𝐧𝐭𝐞𝐧𝐚𝐧𝐜𝐞.

🔄 *𝐘𝐨𝐮𝐫 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜𝐚𝐥𝐥𝐲 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝 𝐢𝐟:*
✅ 𝐘𝐨𝐮 𝐚𝐫𝐞 𝐏𝐫𝐞𝐦𝐢𝐮𝐦/𝐎𝐰𝐧𝐞𝐫 𝐮𝐬𝐞𝐫
✅ 𝐘𝐨𝐮 𝐡𝐚𝐯𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐞𝐝 𝟑+ 𝐟𝐫𝐢𝐞𝐧𝐝𝐬 (𝐅𝐫𝐞𝐞 𝐮𝐬𝐞𝐫𝐬)

📊 *𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐬𝐭𝐚𝐭𝐮𝐬:*
• 𝐀𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 ✅




⏱️ *𝐁𝐨𝐭 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐛𝐚𝐜𝐤 𝐨𝐧𝐥𝐢𝐧𝐞 𝐢𝐧:*
• 𝟑𝟎 𝐬𝐞𝐜𝐨𝐧𝐝𝐬

𝐓𝐡𝐚𝐧𝐤 𝐲𝐨𝐮 𝐟𝐨𝐫 𝐲𝐨𝐮𝐫 𝐩𝐚𝐭𝐢𝐞𝐧𝐜𝐞! 😊
""")
    
    sent = 0
    failed = 0
    
    for user_id in list(active_users):
        try:
            bot.send_message(user_id, notification_text, parse_mode='Markdown')
            sent += 1
        except Exception as e:
            failed += 1
            logger.error(f"❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐬𝐞𝐧𝐝 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐭𝐨 {user_id}: {e}")
        
        # 𝐀𝐯𝐨𝐢𝐝 𝐫𝐚𝐭𝐞 𝐥𝐢𝐦𝐢𝐭𝐢𝐧𝐠
        time.sleep(0.1)
    
    logger.info(f"📤 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬: 𝐒𝐞𝐧𝐭={sent}, 𝐅𝐚𝐢𝐥𝐞𝐝={failed}")

# ================================
# 𝐁𝐔𝐓𝐓𝐎𝐍 𝐋𝐀𝐘𝐎𝐔𝐓𝐒 (𝐰𝐢𝐭𝐡 𝐁𝐎𝐋𝐃 𝐅𝐎𝐍𝐓)
# ================================


def create_reply_keyboard_main_menu(user_id):
    """𝐂𝐫𝐞𝐚𝐭𝐞 𝐫𝐞𝐩𝐥𝐲 𝐤𝐞𝐲𝐛𝐨𝐚𝐫𝐝 𝐰𝐢𝐭𝐡 𝐛𝐨𝐥𝐝 𝐟𝐨𝐧𝐭"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        B("📤 𝐔𝐩𝐥𝐨𝐚𝐝"),
        B("📂 𝐌𝐚𝐧𝐚𝐠𝐞 𝐒𝐜𝐫𝐢𝐩𝐭𝐬"),
        B("⚡ 𝐒𝐩𝐞𝐞𝐝"),
        B("📊 𝐒𝐭𝐚𝐭𝐬"),
        B("👤 𝐏𝐫𝐨𝐟𝐢𝐥𝐞"),
        B("📦 𝐌𝐨𝐝𝐮𝐥𝐞"),
        B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫"),
        B("🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐁𝐨𝐭"),
    ]
    if user_id in admin_ids:
        buttons.append(B("🗄️ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞"))
    for i in range(0, len(buttons), 2):
        row = buttons[i:i+2]
        markup.add(*[types.KeyboardButton(text) for text in row])
    return markup

def create_control_buttons(user_id, file_name, is_running=True):
    """𝐂𝐫𝐞𝐚𝐭𝐞 𝐜𝐨𝐧𝐭𝐫𝐨𝐥 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐟𝐨𝐫 𝐟𝐢𝐥𝐞𝐬 (𝐑𝐞𝐩𝐥𝐲 𝐊𝐞𝐲𝐛𝐨𝐚𝐫𝐝)"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    
    if is_running:
        markup.add(
            types.KeyboardButton(B(f"🔴 𝐒𝐭𝐨𝐩 {file_name}")),
            types.KeyboardButton(B(f"🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 {file_name}"))
        )
        markup.add(
            types.KeyboardButton(B(f"🗑️ 𝐃𝐞𝐥𝐞𝐭𝐞 {file_name}")),
            types.KeyboardButton(B(f"📜 𝐋𝐨𝐠𝐬 {file_name}"))
        )
        markup.add(
            types.KeyboardButton(B(f"🧹 𝐂𝐥𝐞𝐚𝐫 𝐋𝐨𝐠𝐬 {file_name}")),
            types.KeyboardButton(B(f"🧹 𝐅𝐮𝐥𝐥 𝐑𝐞𝐬𝐞𝐭 {file_name}"))
        )
    else:
        markup.add(
            types.KeyboardButton(B(f"🟢 𝐒𝐭𝐚𝐫𝐭 {file_name}")),
            types.KeyboardButton(B(f"🗑️ 𝐃𝐞𝐥𝐞𝐭𝐞 {file_name}"))
        )
        markup.add(
            types.KeyboardButton(B(f"📜 𝐕𝐢𝐞𝐰 𝐋𝐨𝐠𝐬 {file_name}"))
        )
        markup.add(
            types.KeyboardButton(B(f"🧹 𝐂𝐥𝐞𝐚𝐫 𝐋𝐨𝐠𝐬 {file_name}")),
            types.KeyboardButton(B(f"🧹 𝐅𝐮𝐥𝐥 𝐑𝐞𝐬𝐞𝐭 {file_name}"))
        )
    
    markup.add(types.KeyboardButton(B("🔙 𝐁𝐚𝐜𝐤")))
    return markup





# ================================
# 𝐒𝐂𝐑𝐈𝐏𝐓 𝐑𝐔𝐍𝐍𝐈𝐍𝐆 𝐒𝐘𝐒𝐓𝐄𝐌
# ================================
TELEGRAM_MODULES = {
    'telebot': 'pyTelegramBotAPI',
    'telegram': 'python-telegram-bot',
    'aiogram': 'aiogram',
    'pyrogram': 'pyrogram',
    'telethon': 'telethon',
    'requests': 'requests',
    'flask': 'Flask',
    'psutil': 'psutil',
    'qrcode': 'qrcode',
    'pillow': 'Pillow',
    'cryptography': 'cryptography',
    'bs4': 'beautifulsoup4',
    'pandas': 'pandas',
    'numpy': 'numpy',
    'dotenv': 'python-dotenv',
    'aiohttp': 'aiohttp',
    'discord': 'discord.py',
    'openai': 'openai',
    'anthropic': 'anthropic',
    'google': 'google-api-python-client',
    'pymongo': 'pymongo',
    'redis': 'redis',
    'sqlalchemy': 'SQLAlchemy',
    'asyncio': '',  # stdlib
    'json': '',     # stdlib
    'os': '',       # stdlib
    'sys': '',      # stdlib
    'time': '',     # stdlib
    're': '',       # stdlib
    'math': '',     # stdlib
    'random': '',   # stdlib
    'datetime': '', # stdlib
    'collections': '', # stdlib
    'itertools': '',   # stdlib
    'functools': '',   # stdlib
    'pathlib': '',     # stdlib
    'subprocess': '',  # stdlib
    'threading': '',   # stdlib
    'logging': '',     # stdlib
    'io': '',          # stdlib
    'hashlib': '',     # stdlib
    'base64': '',      # stdlib
    'urllib': '',      # stdlib
    'http': '',        # stdlib
    'socket': '',      # stdlib
    'signal': '',      # stdlib
    'string': '',      # stdlib
    'typing': '',      # stdlib
    'dataclasses': '', # stdlib
    'enum': '',        # stdlib
    'abc': '',         # stdlib
    'copy': '',        # stdlib
    'pickle': '',      # stdlib
    'struct': '',      # stdlib
    'gzip': '',        # stdlib
    'tarfile': '',     # stdlib
    'shutil': '',      # stdlib
    'tempfile': '',    # stdlib
    'glob': '',        # stdlib
    'fnmatch': '',     # stdlib
    'sqlite3': '',     # stdlib
    'sqlite': '',      # stdlib
    'csv': '',         # stdlib
    'xml': '',         # stdlib
    'html': '',        # stdlib
    'email': '',       # stdlib
    'smtplib': '',     # stdlib
    'ssl': '',         # stdlib
    'cryptography': 'cryptography',
    'jwt': 'PyJWT',
    'PIL': 'Pillow',
    'cv2': 'opencv-python',
    'sklearn': 'scikit-learn',
    'skimage': 'scikit-image',
    'scipy': 'scipy',
    'matplotlib': 'matplotlib',
    'seaborn': 'seaborn',
    'plotly': 'plotly',
    'selenium': 'selenium',
    'beautifulsoup': 'beautifulsoup4',
    'lxml': 'lxml',
    'pydantic': 'pydantic',
    'fastapi': 'fastapi',
    'uvicorn': 'uvicorn',
    'starlette': 'starlette',
    'jinja2': 'Jinja2',
    'werkzeug': 'Werkzeug',
    'click': 'click',
    'celery': 'celery',
    'kombu': 'kombu',
    'boto3': 'boto3',
    'botocore': 'botocore',
    'stripe': 'stripe',
    'decouple': 'python-decouple',
    'schedule': 'schedule',
    'apscheduler': 'APScheduler',
    'pytz': 'pytz',
    'pycountry': 'pycountry',
    'phonenumbers': 'phonenumbers',
    'PIL.Image': 'Pillow',
    'PIL.ImageDraw': 'Pillow',
    'PIL.ImageFont': 'Pillow',
}

# ================================
# 📄 𝐀𝐔𝐓𝐎-𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐑𝐄𝐐𝐔𝐈𝐑𝐄𝐌𝐄𝐍𝐓𝐒.𝐓𝐗𝐓 & 𝐏𝐑𝐎𝐂𝐅𝐈𝐋𝐄
# ================================
def auto_generate_requirements(file_path, user_folder):
    """𝐒𝐜𝐚𝐧 .𝐩𝐲 𝐟𝐢𝐥𝐞 𝐢𝐦𝐩𝐨𝐫𝐭𝐬 𝐚𝐧𝐝 𝐚𝐮𝐭𝐨-𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐦𝐞𝐧𝐭𝐬.𝐭𝐱𝐭"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # 𝐄𝐱𝐭𝐫𝐚𝐜𝐭 𝐚𝐥𝐥 𝐢𝐦𝐩𝐨𝐫𝐭𝐬
        imports = set(re.findall(r'^\s*import\s+([a-zA-Z0-9_\.]+)', content, re.MULTILINE))
        imports |= set(re.findall(r'^\s*from\s+([a-zA-Z0-9_\.]+)\s+import', content, re.MULTILINE))
        
        # 𝐆𝐞𝐭 𝐭𝐨𝐩-𝐥𝐞𝐯𝐞𝐥 𝐦𝐨𝐝𝐮𝐥𝐞 𝐧𝐚𝐦𝐞𝐬
        top_level = sorted(set(i.split('.')[0] for i in imports))
        
        # 𝐆𝐞𝐭 𝐬𝐭𝐝𝐥𝐢𝐛
        stdlib = set(getattr(sys, 'stdlib_module_names', []))
        
        # 𝐅𝐢𝐥𝐭𝐞𝐫 𝐨𝐮𝐭 𝐬𝐭𝐝𝐥𝐢𝐛 𝐚𝐧𝐝 𝐦𝐚𝐩 𝐭𝐨 𝐩𝐢𝐩 𝐧𝐚𝐦𝐞𝐬
        requirements = []
        seen = set()
        for mod in top_level:
            if mod in stdlib or mod in seen:
                continue
            seen.add(mod)
            # 𝐂𝐡𝐞𝐜𝐤 𝐢𝐟 𝐦𝐨𝐝𝐮𝐥𝐞 𝐢𝐬 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐢𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝
            try:
                __import__(mod)
            except ImportError:
                pass
            
            pip_name = TELEGRAM_MODULES.get(mod.lower(), mod)
            if pip_name:  # 𝐒𝐤𝐢𝐩 𝐞𝐦𝐩𝐭𝐲 𝐦𝐚𝐩𝐩𝐢𝐧𝐠𝐬 (𝐬𝐭𝐝𝐥𝐢𝐛)
                requirements.append(pip_name)
        
        # 𝐖𝐫𝐢𝐭𝐞 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐦𝐞𝐧𝐭𝐬.𝐭𝐱𝐭
        req_path = os.path.join(user_folder, 'requirements.txt')
        with open(req_path, 'w') as f:
            if requirements:
                f.write('\n'.join(sorted(set(requirements))) + '\n')
            else:
                f.write('# 𝐍𝐨 𝐞𝐱𝐭𝐞𝐫𝐧𝐚𝐥 𝐦𝐨𝐝𝐮𝐥𝐞𝐬 𝐝𝐞𝐭𝐞𝐜𝐭𝐞𝐝\n')
        
        logger.info(f"✅ 𝐀𝐮𝐭𝐨-𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐦𝐞𝐧𝐭𝐬.𝐭𝐱𝐭: {requirements}")
        return requirements
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐦𝐞𝐧𝐭𝐬: {e}")
        return []

def auto_generate_procfile(user_folder, file_name):
    """𝐀𝐮𝐭𝐨-𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐏𝐫𝐨𝐜𝐟𝐢𝐥𝐞 𝐟𝐨𝐫 𝐭𝐡𝐞 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝 .𝐩𝐲 𝐟𝐢𝐥𝐞"""
    try:
        procfile_path = os.path.join(user_folder, 'Procfile')
        with open(procfile_path, 'w') as f:
            f.write(f'web: python {file_name}\n')
        logger.info(f"✅ 𝐀𝐮𝐭𝐨-𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐏𝐫𝐨𝐜𝐟𝐢𝐥𝐞: 𝐰𝐞𝐛: 𝐩𝐲𝐭𝐡𝐨𝐧 {file_name}")
        return True
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐟𝐢𝐥𝐞: {e}")
        return False

def auto_setup_user_env(user_id, file_name):
    """𝐀𝐮𝐭𝐨-𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐦𝐞𝐧𝐭𝐬.𝐭𝐱𝐭 𝐚𝐧𝐝 𝐏𝐫𝐨𝐜𝐟𝐢𝐥𝐞 𝐰𝐡𝐞𝐧 𝐮𝐬𝐞𝐫 𝐮𝐩𝐥𝐨𝐚𝐝𝐬 .𝐩𝐲 𝐟𝐢𝐥𝐞"""
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    
    # 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐦𝐞𝐧𝐭𝐬.𝐭𝐱𝐭
    requirements = auto_generate_requirements(file_path, user_folder)
    
    # 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐏𝐫𝐨𝐜𝐟𝐢𝐥𝐞
    auto_generate_procfile(user_folder, file_name)
    
    # 𝐀𝐮𝐭𝐨-𝐢𝐧𝐬𝐭𝐚𝐥𝐥 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐦𝐞𝐧𝐭𝐬
    if requirements:
        for pip_name in sorted(set(requirements)):
            try:
                subprocess.run(
                    [sys.executable, '-m', 'pip', 'install', pip_name],
                    capture_output=True, text=True, check=False
                )
            except Exception:
                pass
    
    return requirements

def attempt_install_pip(module_name, message):
    """𝐀𝐭𝐭𝐞𝐦𝐩𝐭 𝐭𝐨 𝐢𝐧𝐬𝐭𝐚𝐥𝐥 𝐏𝐲𝐭𝐡𝐨𝐧 𝐦𝐨𝐝𝐮𝐥𝐞"""
    package_name = TELEGRAM_MODULES.get(module_name.lower(), module_name)
    if package_name is None:
        return False
    
    try:
        bot.reply_to(message, B(f"🐍 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐢𝐧𝐠 `{module_name}`..."))
        command = [sys.executable, '-m', 'pip', 'install', package_name]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            bot.reply_to(message, B(f"✅ 𝐏𝐚𝐜𝐤𝐚𝐠𝐞 `{package_name}` 𝐢𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝."))
            return True
        else:
            bot.reply_to(message, B(f"❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐢𝐧𝐬𝐭𝐚𝐥𝐥 `{package_name}`."))
            return False
    except Exception as e:
        bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫: {str(e)}"))
        return False

# ================================
# 📦 𝐌𝐎𝐃𝐔𝐋𝐄 𝐌𝐀𝐍𝐀𝐆𝐄𝐑
# ================================
pending_module_installs = {}

def scan_required_modules(file_path):
    """𝐒𝐜𝐚𝐧 𝐚 .𝐩𝐲 𝐟𝐢𝐥𝐞'𝐬 𝐢𝐦
port𝐬 𝐟𝐨𝐫 𝐦𝐢𝐬𝐬𝐢𝐧𝐠 𝐦𝐨𝐝𝐮𝐥𝐞𝐬"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        imports = set(re.findall(r'^\s*import\s+([a-zA-Z0-9_\.]+)', content, re.MULTILINE))
        imports |= set(re.findall(r'^\s*from\s+([a-zA-Z0-9_\.]+)\s+import', content, re.MULTILINE))
        
        top_level = sorted(set(i.split('.')[0] for i in imports))
        stdlib = set(getattr(sys, 'stdlib_module_names', []))
        
        required = []
        for mod in top_level:
            if mod in stdlib:
                continue
            try:
                __import__(mod)
            except ImportError:
                pip_name = TELEGRAM_MODULES.get(mod.lower(), mod)
                if pip_name:
                    required.append(pip_name)
        
        return sorted(set(required))
    except Exception:
        return []

# ================================
# 𝐃𝐁 𝐎𝐏𝐄𝐑𝐀𝐓𝐈𝐎𝐍𝐒
# ================================
def add_active_user(user_id, username=None):
    """𝐀𝐝𝐝 𝐨𝐫 𝐮𝐩𝐝𝐚𝐭𝐞 𝐚𝐜𝐭𝐢𝐯𝐞 𝐮𝐬𝐞𝐫"""
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    now = datetime.now().isoformat()
    c.execute('''INSERT OR IGNORE INTO active_users (user_id, username, first_join, last_seen)
                 VALUES (?, ?, ?, ?)''', (user_id, username, now, now))
    c.execute('''UPDATE active_users SET last_seen = ?, username = COALESCE(?, username)
                 WHERE user_id = ?''', (now, username, user_id))
    conn.commit()
    conn.close()
    active_users.add(user_id)


    



def save_user_file_db(user_id, file_name, file_type):
    """𝐒𝐚𝐯𝐞 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('''INSERT OR REPLACE INTO user_files (user_id, file_name, file_type, uploaded_at)
                 VALUES (?, ?, ?, ?)''', (user_id, file_name, file_type, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    if user_id not in user_files:
        user_files[user_id] = []
    if not any(fname == file_name for fname, _ in user_files[user_id]):
        user_files[user_id].append((file_name, file_type))

def remove_user_file_db(user_id, file_name):
    """𝐑𝐞𝐦𝐨𝐯𝐞 𝐟𝐢𝐥𝐞 𝐟𝐫𝐨𝐦 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM user_files WHERE user_id = ? AND file_name = ?', (user_id, file_name))
    conn.commit()
    conn.close()
    if user_id in user_files:
        user_files[user_id] = [(fname, ftype) for fname, ftype in user_files[user_id] if fname != file_name]
    recovery_system.remove_running_script(user_id, file_name)




    return True

def add_active_user_db(user_id, username=None):
    """𝐀𝐝𝐝 𝐚𝐜𝐭𝐢𝐯𝐞 𝐮𝐬𝐞𝐫 𝐭𝐨 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    now = datetime.now().isoformat()
    c.execute('''INSERT OR IGNORE INTO active_users (user_id, username, first_join, last_seen)
                 VALUES (?, ?, ?, ?)''', (user_id, username, now, now))
    conn.commit()
    conn.close()




def increment_referral(referrer_id):
    """𝐈𝐧𝐜𝐫𝐞𝐦𝐞𝐧𝐭 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐜𝐨𝐮𝐧𝐭"""
    if not hasattr(get_referral_count, '_counts'):
        get_referral_count._counts = {}
    get_referral_count._counts[referrer_id] = get_referral_count._counts.get(referrer_id, 0) + 1

# ================================
# 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐇𝐀𝐍𝐃𝐋𝐄𝐑𝐒
# ================================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """𝐇𝐚𝐧𝐝𝐥𝐞 /start 𝐜𝐨𝐦𝐦𝐚𝐧𝐝"""
    user_id = message.from_user.id
    add_active_user(user_id, message.from_user.username)
    user_tier = get_user_tier(user_id)
    tier_info = TIER_SYSTEM[user_tier]
    
    welcome_text = f"""☁️ 𝘿𝘼𝙍𝙇𝙄𝙉𝙂 𝙃𝙊𝙎𝙏𝙄𝙉𝙂 𝘽𝙊𝙏

🟢 𝗙𝗨𝗟𝗟 𝗔𝗖𝗖𝗘𝗦𝗦
📂 𝗙𝗶𝗹𝗲𝘀 • {tier_info['upload_limit'] if tier_info['upload_limit'] != float('inf') else '∞ Unlimited'}
💾 𝗦𝗶𝘇𝗲 • {str(tier_info['max_file_size'] // (1024*1024)) + ' MB' if tier_info['max_file_size'] != float('inf') else '∞ Unlimited'}

📤 𝗨𝗽𝗹𝗼𝗮𝗱 & 𝗛𝗼𝘀𝘁
🚀 𝟮𝟰/𝟳 𝗛𝗼𝘀𝘁𝗶𝗻𝗴
📦 𝗔𝘂𝘁𝗼 𝗠𝗼𝗱𝘂𝗹𝗲𝘀
🔄 𝗔𝘂𝘁𝗼 𝗥𝗲𝗰𝗼𝘃𝗲𝗿𝘆
📜 𝗟𝗶𝘃𝗲 𝗟𝗼𝗴𝘀
⚡ 𝗦𝗽𝗲𝗲𝗱 𝗧𝗲𝘀𝘁

🐍 Python • 🟢 Node.js

━━━━━━━━━━━━━━━━━━━━
      ᴍᴀᴅᴇ ʙʏ 𝗔𝗫𝗫𝗨
━━━━━━━━━━━━━━━━━━━━"""
    
    msg = bot.reply_to(message, welcome_text, parse_mode='Markdown',
                       reply_markup=create_reply_keyboard_main_menu(user_id))
    
    # Run the short dashboard animation, then keep the clean dashboard visible.
    try:
        animation = AnimationManager.animate_dashboard(message.chat.id, msg.message_id)
        if animation:
            def _restore_dashboard():
                animation.join(timeout=3.0)
                try:
                    bot.edit_message_text(welcome_text, message.chat.id, msg.message_id, parse_mode='Markdown', reply_markup=create_reply_keyboard_main_menu(user_id))
                except Exception:
                    pass
            threading.Thread(target=_restore_dashboard, daemon=True).start()
    except Exception:
        pass

@bot.message_handler(commands=['help'])
def send_help(message):
    """𝐒𝐞𝐧𝐝 𝐡𝐞𝐥𝐩 𝐦𝐞𝐧𝐮"""
    user_id = message.from_user.id
    help_text = f"""╔══════════════════════════════════╗
║    📋 𝐇𝐄𝐋𝐏 𝐆𝐔𝐈𝐃𝐄               ║
╚══════════════════════════════════╝

*𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬:*
/start — 𝐎𝐩𝐞𝐧 𝐦𝐚𝐢𝐧 𝐦𝐞𝐧𝐮
/help — 𝐓𝐡𝐢𝐬 𝐡𝐞𝐥𝐩 𝐦𝐞𝐧𝐮
/stats — 𝐘𝐨𝐮𝐫 𝐬𝐭𝐚𝐭𝐬
/profile — 𝐘𝐨𝐮𝐫 𝐩𝐫𝐨𝐟𝐢𝐥𝐞
/speed — 𝐒𝐩𝐞𝐞𝐝 𝐭𝐞𝐬𝐭
 — 𝐓𝐨𝐩 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬

*𝐇𝐨𝐰 𝐭𝐨 𝐮𝐬𝐞:*
1️⃣ 𝐔𝐩𝐥𝐨𝐚𝐝 𝐚 .𝐩𝐲 𝐨𝐫 .𝐣𝐬 𝐟𝐢𝐥𝐞
2️⃣ 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐮𝐭𝐨-𝐢𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝
3️⃣ 𝐂𝐥𝐢𝐜𝐤 𝐒𝐭𝐚𝐫𝐭 𝐭𝐨 𝐫𝐮𝐧
4️⃣ 𝐕𝐢𝐞𝐰 𝐥𝐢𝐯𝐞 𝐥𝐨𝐠𝐬
5️⃣ 𝐑𝐞𝐬𝐭𝐚𝐫𝐭/𝐒𝐭𝐨𝐩/𝐃𝐞𝐥𝐞𝐭𝐞 𝐚𝐧𝐲𝐭𝐢𝐦𝐞

*𝐀𝐮𝐭𝐨-𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲:* ✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝"""
    
    bot.reply_to(message, help_text, parse_mode='Markdown',
                 reply_markup=create_reply_keyboard_main_menu(user_id))

@bot.message_handler(commands=['stats'])
def show_stats(message):
    """𝐒𝐡𝐨𝐰 𝐮𝐬𝐞𝐫 𝐬𝐭𝐚𝐭𝐬"""
    user_id = message.from_user.id
    add_active_user(user_id)
    
    user_tier = get_user_tier(user_id)
    tier_info = TIER_SYSTEM[user_tier]
    file_count = get_user_file_count(user_id)
    file_limit = get_user_file_limit(user_id)
    
    stats_text = f"""╔══════════════════════════════════╗
║    📊 𝐘𝐎𝐔𝐑 𝐒𝐓𝐀𝐓𝐒                ║
╚══════════════════════════════════╝

{tier_info['icon']} *𝐓𝐢𝐞𝐫: {tier_info['name']}*
📂 *𝐅𝐢𝐥𝐞𝐬:* {file_count}/{file_limit if file_limit != float('inf') else '∞'}
🚀 *𝐑𝐮𝐧𝐧𝐢𝐧𝐠:* {sum(1 for key, info in bot_scripts.items() if info['user_id'] == user_id and is_bot_running(user_id, info['file_name']))}

*𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐈𝐧𝐟𝐨:*
🆔 𝐔𝐬𝐞𝐫 𝐈𝐃: {user_id}
👤 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: @{message.from_user.username or '𝐍𝐎𝐓 𝐒𝐄𝐓'}
📅 𝐉𝐨𝐢𝐧𝐞𝐝: {datetime.now().strftime('%Y-%m-%d')}"""
    
    msg = bot.reply_to(message, stats_text, parse_mode='Markdown',
                       reply_markup=create_reply_keyboard_main_menu(user_id))
    try:
        AnimationManager.animate_dashboard(message.chat.id, msg.message_id)
    except Exception:
        pass

@bot.message_handler(commands=['profile'])
def show_profile(message):
    """𝐒𝐡𝐨𝐰 𝐮𝐬𝐞𝐫 𝐩𝐫𝐨𝐟𝐢𝐥𝐞"""
    user_id = message.from_user.id
    add_active_user(user_id)
    
    user_tier = get_user_tier(user_id)
    tier_info = TIER_SYSTEM[user_tier]
    
    profile_text = f"""╔══════════════════════════════════╗
║    👤 𝐘𝐎𝐔𝐑 𝐏𝐑𝐎𝐅𝐈𝐋𝐄              ║
╚══════════════════════════════════╝

👤 *𝐍𝐚𝐦𝐞:* {message.from_user.first_name}
🆔 *𝐔𝐬𝐞𝐫 𝐈𝐃:* {user_id}
@ *𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:* @{message.from_user.username or '𝐍𝐎𝐓 𝐒𝐄𝐓'}
{tier_info['icon']} *𝐓𝐢𝐞𝐫:* {tier_info['name']}"""
    
    bot.reply_to(message, profile_text, parse_mode='Markdown',
                 reply_markup=create_reply_keyboard_main_menu(user_id))

_speed_test_locks = {}
_speed_test_locks_guard = threading.Lock()
_SPEED_TEST_DOWNLOAD_URL = 'https://speed.cloudflare.com/__down?bytes=10000000'
_SPEED_TEST_UPLOAD_URL = 'https://speed.cloudflare.com/__up'
_SPEED_TEST_LATENCY_URL = 'https://speed.cloudflare.com/cdn-cgi/trace'
_SPEED_TEST_TIMEOUT = (5, 20)

def _speed_lock(user_id):
    with _speed_test_locks_guard:
        return _speed_test_locks.setdefault(int(user_id), threading.Lock())

def _edit_speed_message(chat_id, message_id, text, user_id=None):
    try:
        bot.edit_message_text(text, chat_id, message_id, reply_markup=create_reply_keyboard_main_menu(user_id) if user_id is not None else None)
    except Exception as exc:
        if 'message is not modified' not in str(exc).lower():
            logger.debug('Speed-test message edit failed: %s', exc)

def _animation_manager_speed(chat_id, message_id, frames):
    """Run a short speed-test animation through the existing edit engine."""
    return run_edit_animation(chat_id, message_id, frames, delay=0.45)

AnimationManager.animate_speed_test = staticmethod(_animation_manager_speed)

def _speed_animation(chat_id, message_id, frames, user_id):
    """Use the existing AnimationManager architecture for ordered live edits."""
    animation = AnimationManager.animate_speed_test(chat_id, message_id, frames)
    if animation:
        animation.join(timeout=(len(frames) * 0.45) + 1.0)

def _measure_download():
    started = time.monotonic()
    received = 0
    with requests.get(_SPEED_TEST_DOWNLOAD_URL, stream=True, timeout=_SPEED_TEST_TIMEOUT) as response:
        response.raise_for_status()
        for chunk in response.iter_content(chunk_size=256 * 1024):
            if chunk:
                received += len(chunk)
    elapsed = max(time.monotonic() - started, 0.001)
    return received * 8 / elapsed / 1_000_000

def _measure_upload():
    payload = os.urandom(4 * 1024 * 1024)
    started = time.monotonic()
    response = requests.post(_SPEED_TEST_UPLOAD_URL, data=payload, timeout=_SPEED_TEST_TIMEOUT)
    response.raise_for_status()
    elapsed = max(time.monotonic() - started, 0.001)
    return len(payload) * 8 / elapsed / 1_000_000

def _measure_latency():
    samples = []
    for _ in range(3):
        started = time.monotonic()
        response = requests.get(_SPEED_TEST_LATENCY_URL, timeout=(5, 8))
        response.raise_for_status()
        samples.append((time.monotonic() - started) * 1000)
    return sum(samples) / len(samples) if samples else None

def _run_real_speed_test(chat_id, message_id, user_id):
    lock = _speed_lock(user_id)
    if not lock.acquire(blocking=False):
        _edit_speed_message(chat_id, message_id, '⚠️ 𝗦𝗣𝗘𝗘𝗗 𝗧𝗘𝗦𝗧 𝗔𝗟𝗥𝗘𝗔𝗗𝗬 𝗥𝗨𝗡𝗡𝗜𝗡𝗚\n\nPlease wait for the current test to finish.', user_id)
        return
    try:
        download = upload = latency = None
        _speed_animation(chat_id, message_id, [
            '⚡ 𝗦𝗣𝗘𝗘𝗗 𝗧𝗘𝗦𝗧\n━━━━━━━━━━━━━━━━━━━━\n◐ Connecting to test server...',
            '⚡ 𝗦𝗣𝗘𝗘𝗗 𝗧𝗘𝗦𝗧\n━━━━━━━━━━━━━━━━━━━━\n◓ Connecting to test server...',
        ], user_id)
        try:
            _speed_animation(chat_id, message_id, [
                '📥 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗧𝗘𝗦𝗧\n━━━━━━━━━━━━━━━━━━━━\n◐ Measuring download speed...',
                '📥 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗧𝗘𝗦𝗧\n━━━━━━━━━━━━━━━━━━━━\n◓ Measuring download speed...',
                '📥 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗧𝗘𝗦𝗧\n━━━━━━━━━━━━━━━━━━━━\n◑ Measuring download speed...',
            ], user_id)
            download = _measure_download()
        except Exception as exc:
            logger.error('Real download test failed: %s', exc, exc_info=True)
        _edit_speed_message(chat_id, message_id, f'📥 Download: {download:.2f} Mbps' if download is not None else '📥 Download: N/A', user_id)
        time.sleep(0.45)
        try:
            _speed_animation(chat_id, message_id, [
                '📤 𝗨𝗣𝗟𝗢𝗔𝗗 𝗧𝗘𝗦𝗧\n━━━━━━━━━━━━━━━━━━━━\n◐ Measuring upload speed...',
                '📤 𝗨𝗣𝗟𝗢𝗔𝗗 𝗧𝗘𝗦𝗧\n━━━━━━━━━━━━━━━━━━━━\n◓ Measuring upload speed...',
                '📤 𝗨𝗣𝗟𝗢𝗔𝗗 𝗧𝗘𝗦𝗧\n━━━━━━━━━━━━━━━━━━━━\n◑ Measuring upload speed...',
            ], user_id)
            upload = _measure_upload()
        except Exception as exc:
            logger.warning('Real upload test unavailable: %s', exc, exc_info=True)
        _edit_speed_message(chat_id, message_id, f'📤 Upload: {upload:.2f} Mbps' if upload is not None else '📤 Upload: N/A', user_id)
        time.sleep(0.45)
        try:
            _speed_animation(chat_id, message_id, [
                '⏱️ 𝗟𝗔𝗧𝗘𝗡𝗖𝗬 𝗧𝗘𝗦𝗧\n━━━━━━━━━━━━━━━━━━━━\n◐ Measuring latency...',
                '⏱️ 𝗟𝗔𝗧𝗘𝗡𝗖𝗬 𝗧𝗘𝗦𝗧\n━━━━━━━━━━━━━━━━━━━━\n◓ Measuring latency...',
            ], user_id)
            latency = _measure_latency()
        except Exception as exc:
            logger.warning('Real latency test unavailable: %s', exc, exc_info=True)
        if download is None and upload is None and latency is None:
            _edit_speed_message(chat_id, message_id, '❌ 𝗦𝗣𝗘𝗘𝗗 𝗧𝗘𝗦𝗧 𝗙𝗔𝗜𝗟𝗘𝗗\n━━━━━━━━━━━━━━━━━━━━\nUnable to connect to a speed-test server.\n\nPlease try again.', user_id)
            return
        tested = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result = (
            '╭━━━━━━━━━━━━━━━━━━━━╮\n'
            '│   ⚡ 𝗦𝗣𝗘𝗘𝗗 𝗧𝗘𝗦𝗧    │\n'
            '╰━━━━━━━━━━━━━━━━━━━━╯\n\n'
            + (f'📥 Download   : {download:.2f} Mbps\n' if download is not None else '📥 Download   : N/A\n')
        )
        result += f'📤 Upload     : {upload:.2f} Mbps\n' if upload is not None else '📤 Upload     : N/A\n'
        result += f'⏱️ Latency    : {latency:.0f} ms\n' if latency is not None else '⏱️ Latency    : N/A\n'
        result += f'\n🌐 Server     : Cloudflare Speed Test\n📍 Location   : N/A\n🕐 Tested     : {tested}\n\n━━━━━━━━━━━━━━━━━━━━\n✅ 𝗧𝗘𝗦𝗧 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘'
        _edit_speed_message(chat_id, message_id, result, user_id)
    except Exception as exc:
        logger.error('Speed test failed unexpectedly: %s', exc, exc_info=True)
        _edit_speed_message(chat_id, message_id, '❌ 𝗦𝗣𝗘𝗘𝗗 𝗧𝗘𝗦𝗧 𝗙𝗔𝗜𝗟𝗘𝗗\n━━━━━━━━━━━━━━━━━━━━\nUnable to complete the network test.\n\nPlease try again.', user_id)
    finally:
        lock.release()

@bot.message_handler(commands=['speed'])
def run_speedtest(message):
    """Run a real server-side speed test without blocking Telegram polling."""
    user_id = message.from_user.id
    add_active_user(user_id)
    msg = bot.reply_to(message, '⚡ 𝗦𝗣𝗘𝗘𝗗 𝗧𝗘𝗦𝗧\n━━━━━━━━━━━━━━━━━━━━\n◐ Connecting to test server...')
    threading.Thread(target=_run_real_speed_test, args=(message.chat.id, msg.message_id, user_id), daemon=True).start()

# 𝐃𝐎𝐂𝐔𝐌𝐄𝐍𝐓 (𝐔𝐏𝐋𝐎𝐀𝐃) 𝐇𝐀𝐍𝐃𝐋𝐄𝐑
# ================================
@bot.message_handler(content_types=['document'])
def handle_document(message):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐟𝐢𝐥𝐞 𝐮𝐩𝐥𝐨𝐚𝐝"""
    user_id = message.from_user.id
    add_active_user(user_id)
    
    if bot_locked and user_id != OWNER_ID:
        bot.reply_to(message, "🔒 𝐁𝐨𝐭 𝐢𝐬 𝐥𝐨𝐜𝐤𝐞𝐝.")
        return
    
    doc = message.document
    file_name = doc.file_name
    file_ext = os.path.splitext(file_name)[1].lower()
    
    if file_ext not in ['.py', '.js', '.zip']:
        bot.reply_to(message, B("❌ 𝐎𝐧𝐥𝐲 .𝐩𝐲, .𝐣𝐬, 𝐚𝐧𝐝 .𝐳𝐢𝐩 𝐟𝐢𝐥𝐞𝐬 𝐚𝐥𝐥𝐨𝐰𝐞𝐝."))
        return
    
    # 𝐂𝐡𝐞𝐜𝐤 𝐟𝐢𝐥𝐞 𝐬𝐢𝐳𝐞
    user_tier = get_user_tier(user_id)
    max_size = TIER_SYSTEM[user_tier]['max_file_size']
    if doc.file_size > max_size:
        max_mb = max_size // (1024 * 1024) if max_size != float('inf') else '∞'
        bot.reply_to(message, B(f"❌ 𝐅𝐢𝐥𝐞 𝐭𝐨𝐨 𝐥𝐚𝐫𝐠𝐞. 𝐌𝐚𝐱: {max_mb} 𝐌𝐁"))
        return
    
    # 𝐂𝐡𝐞𝐜𝐤 𝐟𝐢𝐥𝐞 𝐥𝐢𝐦𝐢𝐭
    file_count = get_user_file_count(user_id)
    file_limit = get_user_file_limit(user_id)
    if file_count >= file_limit:
        bot.reply_to(message, B(f"❌ 𝐅𝐢𝐥𝐞 𝐥𝐢𝐦𝐢𝐭 𝐫𝐞𝐚𝐜𝐡𝐞𝐝 ({file_limit}). 𝐃𝐞𝐥𝐞𝐭𝐞 𝐚 𝐟𝐢𝐥𝐞 𝐟𝐢𝐫𝐬𝐭."))
        return
    
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    
    # 𝐒𝐞𝐧𝐝 𝐢𝐧𝐢𝐭𝐢𝐚𝐥 𝐦𝐞𝐬𝐬𝐚𝐠𝐞
    msg = bot.reply_to(message, B("🚀 𝐈𝐧𝐢𝐭𝐢𝐚𝐭𝐢𝐧𝐠 𝐮𝐩𝐥𝐨𝐚𝐝 𝐬𝐞𝐪𝐮𝐞𝐧𝐜𝐞..."))
    
    # 𝐒𝐭𝐚𝐫𝐭 𝐮𝐩𝐥𝐨𝐚𝐝 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
    try:
        AnimationManager.animate_upload(message.chat.id, msg.message_id)
    except Exception:
        pass
    
    # 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐟𝐢𝐥𝐞
    try:
        file_info = bot.get_file(doc.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        with open(file_path, 'wb') as f:
            f.write(downloaded_file)
        
        # 𝐒𝐚𝐯𝐞 𝐭𝐨 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
        file_type = 'py' if file_ext == '.py' else 'js'
        save_user_file_db(user_id, file_name, file_type)
        
        # 𝐀𝐮𝐭𝐨-𝐬𝐞𝐭𝐮𝐩 𝐟𝐨𝐫 .𝐩𝐲 𝐟𝐢𝐥𝐞𝐬
        if file_ext == '.py':
            try:
                reqs = auto_setup_user_env(user_id, file_name)
            except Exception:
                pass
        
        time.sleep(3)  # 𝐖𝐚𝐢𝐭 𝐟𝐨𝐫 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧 𝐭𝐨 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞
        
        tier_info = TIER_SYSTEM[get_user_tier(user_id)]
        upload_text = f"""╔══════════════════════════════════╗
║    ✅ 𝐔𝐏𝐋𝐎𝐀𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋         ║
╠══════════════════════════════════╣
║    📂 {file_name}
║    💾 {doc.file_size / 1024:.1f} 𝐊𝐁
║    {tier_info['icon']} {tier_info['name']} 𝐓𝐈𝐄𝐑
╚══════════════════════════════════╝

📊 *𝐒𝐭𝐚𝐭𝐮𝐬:* 𝐑𝐞𝐚𝐝𝐲 𝐭𝐨 𝐡𝐨𝐬𝐭
🔄 *𝐀𝐮𝐭𝐨-𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲:* {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if tier_info['auto_restart'] else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}
📦 *𝐌𝐨𝐝𝐮𝐥𝐞𝐬:* 𝐀𝐮𝐭𝐨-𝐢𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝"""
        
        # 𝐒𝐞𝐧𝐝 𝐟𝐢𝐧𝐚𝐥 𝐬𝐮𝐜𝐜𝐞𝐬𝐬 𝐦𝐞𝐬𝐬𝐚𝐠𝐞
        bot.edit_message_text(upload_text, message.chat.id, msg.message_id, parse_mode='Markdown',
                             reply_markup=create_reply_keyboard_main_menu(user_id))
        
    except Exception as e:
        bot.edit_message_text(B(f"❌ 𝐔𝐩𝐥𝐨𝐚𝐝 𝐅𝐚𝐢𝐥𝐞𝐝: {str(e)}"), message.chat.id, msg.message_id,
                             reply_markup=create_reply_keyboard_main_menu(user_id))

# ================================
# 𝐅𝐈𝐋𝐄 𝐂𝐎𝐍𝐓𝐑𝐎𝐋 𝐇𝐀𝐍𝐃𝐋𝐄𝐑𝐒
# ================================
def handle_file_control_text(message):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐟𝐢𝐥𝐞 𝐜𝐨𝐧𝐭𝐫𝐨𝐥 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬 (𝐒𝐭𝐚𝐫𝐭, 𝐒𝐭𝐨𝐩, 𝐑𝐞𝐬𝐭𝐚𝐫𝐭, 𝐃𝐞𝐥𝐞𝐭𝐞, 𝐋𝐨𝐠𝐬)"""
    user_id = message.from_user.id
    add_active_user(user_id)
    
    text = message.text
    user_folder = get_user_folder(user_id)
    
    # 𝐁𝐚𝐜𝐤 𝐛𝐮𝐭𝐭𝐨𝐧
    if B("🔙 𝐁𝐚𝐜𝐤") in text:
        bot.reply_to(message, B("🏠 𝐑𝐞𝐭𝐮𝐫𝐧𝐢𝐧𝐠 𝐭𝐨 𝐦𝐚𝐢𝐧 𝐦𝐞𝐧𝐮..."),
                     reply_markup=create_reply_keyboard_main_menu(user_id))
        return
    
    # 𝐏𝐚𝐫𝐬𝐞 𝐟𝐢𝐥𝐞 𝐧𝐚𝐦𝐞 𝐟𝐫𝐨𝐦 𝐛𝐮𝐭𝐭𝐨𝐧 𝐭𝐞𝐱𝐭
    raw_file_name = text.split(' ', 2)[-1] if ' ' in text else ''
    file_name = unbold(raw_file_name)
    
    # 𝐒𝐭𝐚𝐫𝐭
    if "🟢" in text and "𝐒𝐭𝐚𝐫𝐭" in text:
        _start_script(message, user_id, file_name)
    # 𝐒𝐭𝐨𝐩
    elif "🔴" in text and "𝐒𝐭𝐨𝐩" in text:
        _stop_script(message, user_id, file_name)
    # 𝐑𝐞𝐬𝐭𝐚𝐫𝐭
    elif "🔄" in text and "𝐑𝐞𝐬𝐭𝐚𝐫𝐭" in text:
        _restart_script(message, user_id, file_name)
    # 𝐃𝐞𝐥𝐞𝐭𝐞
    elif "🗑️" in text and "𝐃𝐞𝐥𝐞𝐭𝐞" in text:
        _delete_script(message, user_id, file_name)
    # 𝐋𝐨𝐠𝐬
    elif "📜" in text and ("𝐋𝐨𝐠𝐬" in text or "𝐕𝐢𝐞𝐰" in text):
        _show_logs(message, user_id, file_name)
    elif "🧹" in text and "𝐂𝐥𝐞𝐚𝐫 𝐋𝐨𝐠𝐬" in text:
        _clear_logs(message, user_id, file_name)
    elif "🧹" in text and "𝐅𝐮𝐥𝐥 𝐑𝐞𝐬𝐞𝐭" in text:
        _request_full_reset(message, user_id, file_name)

def _start_script(message, user_id, file_name):
    """𝐒𝐭𝐚𝐫𝐭 𝐚 𝐬𝐜𝐫𝐢𝐩𝐭"""
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    
    if not os.path.exists(file_path):
        bot.reply_to(message, B(f"❌ 𝐅𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝: `{file_name}`"), parse_mode='Markdown')
        return
    
    if is_bot_running(user_id, file_name):
        bot.reply_to(message, B(f"⚠️ `{file_name}` 𝐢𝐬 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠."), parse_mode='Markdown')
        return
    
    file_type = 'py'
    for fname, ftype in user_files.get(user_id, []):
        if fname == file_name:
            file_type = ftype
            break
    
    msg = bot.reply_to(message, B(f"🚀 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 `{file_name}`..."))
    
    # 𝐒𝐭𝐚𝐫𝐭 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
    try:
        AnimationManager.animate_start(message.chat.id, msg.message_id)
    except Exception:
        pass
    
    # 𝐒𝐭𝐚𝐫𝐭 𝐬𝐜𝐫𝐢𝐩𝐭 𝐢𝐧 𝐭𝐡𝐫𝐞𝐚𝐝
    if file_type == 'py':
        threading.Thread(target=run_script, args=(file_path, user_id, user_folder, file_name, msg)).start()
    elif file_type == 'js':
        threading.Thread(target=run_js_script, args=(file_path, user_id, user_folder, file_name, msg)).start()

def _stop_script(message, user_id, file_name):
    """𝐒𝐭𝐨𝐩 𝐚 𝐬𝐜𝐫𝐢𝐩𝐭"""
    script_key = f"{user_id}_{file_name}"
    if not is_bot_running(user_id, file_name):
        bot.reply_to(message, B(f"⚠️ `{file_name}` 𝐢𝐬 𝐧𝐨𝐭 𝐫𝐮𝐧𝐧𝐢𝐧𝐠."), parse_mode='Markdown')
        return
    
    msg = bot.reply_to(message, B(f"🛑 𝐒𝐭𝐨𝐩𝐩𝐢𝐧𝐠 `{file_name}`..."))
    
    # 𝐒𝐭𝐨𝐩 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
    try:
        AnimationManager.animate_stop(message.chat.id, msg.message_id)
    except Exception:
        pass
    
    if script_key in bot_scripts:
        kill_process_tree(bot_scripts[script_key])
        if script_key in bot_scripts:
            del bot_scripts[script_key]
    
    recovery_system.remove_running_script(user_id, file_name)
    
    # 𝐒𝐞𝐧𝐝 𝐟𝐢𝐧𝐚𝐥 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐚𝐟𝐭𝐞𝐫 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
    time.sleep(1.2)
    try:
        bot.edit_message_text(
            B(f"🛑 `{file_name}` 𝐬𝐭𝐨𝐩𝐩𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲."),
            message.chat.id, msg.message_id, parse_mode='Markdown',
            reply_markup=create_reply_keyboard_main_menu(user_id)
        )
    except Exception:
        pass

def _restart_script(message, user_id, file_name):
    """𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐚 𝐬𝐜𝐫𝐢𝐩𝐭"""
    script_key = f"{user_id}_{file_name}"
    if is_bot_running(user_id, file_name):
        if script_key in bot_scripts:
            kill_process_tree(bot_scripts[script_key])
            if script_key in bot_scripts:
                del bot_scripts[script_key]
        time.sleep(1)
    
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    if not os.path.exists(file_path):
        bot.reply_to(message, B(f"❌ 𝐅𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝: `{file_name}`"), parse_mode='Markdown')
        return
    
    file_type = 'py'
    for fname, ftype in user_files.get(user_id, []):
        if fname == file_name:
            file_type = ftype
            break
    
    msg = bot.reply_to(message, B(f"🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 `{file_name}`..."))
    
    # 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
    try:
        AnimationManager.animate_restart(message.chat.id, msg.message_id)
    except Exception:
        pass
    
    if file_type == 'py':
        threading.Thread(target=run_script, args=(file_path, user_id, user_folder, file_name, msg)).start()
    elif file_type == 'js':
        threading.Thread(target=run_js_script, args=(file_path, user_id, user_folder, file_name, msg)).start()

def _delete_script(message, user_id, file_name):
    """𝐃𝐞𝐥𝐞𝐭𝐞 𝐚 𝐬𝐜𝐫𝐢𝐩𝐭"""
    msg = bot.reply_to(message, B(f"🗑️ 𝐃𝐞𝐥𝐞𝐭𝐢𝐧𝐠 `{file_name}`..."))
    
    # 𝐃𝐞𝐥𝐞𝐭𝐞 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
    try:
        AnimationManager.animate_delete(message.chat.id, msg.message_id)
    except Exception:
        pass
    
    if is_bot_running(user_id, file_name):
        script_key = f"{user_id}_{file_name}"
        if script_key in bot_scripts:
            kill_process_tree(bot_scripts[script_key])
            if script_key in bot_scripts:
                del bot_scripts[script_key]
    
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    log_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
    
    if os.path.exists(file_path):
        os.remove(file_path)
    if os.path.exists(log_path):
        os.remove(log_path)
    remove_user_file_db(user_id, file_name)
    
    time.sleep(1.5)
    try:
        bot.edit_message_text(
            B(f"🗑️ `{file_name}` 𝐝𝐞𝐥𝐞𝐭𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲."),
            message.chat.id, msg.message_id, parse_mode='Markdown',
            reply_markup=create_reply_keyboard_main_menu(user_id)
        )
    except Exception:
        pass

def _show_logs(message, user_id, file_name):
    """𝐒𝐡𝐨𝐰 𝐥𝐨𝐠𝐬 𝐟𝐨𝐫 𝐚 𝐬𝐜𝐫𝐢𝐩𝐭"""
    user_folder = get_user_folder(user_id)
    log_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
    
    msg = bot.reply_to(message, B(f"📜 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐥𝐨𝐠𝐬..."))
    
    # 𝐋𝐨𝐠𝐬 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
    try:
        AnimationManager.animate_logs(message.chat.id, msg.message_id)
    except Exception:
        pass
    
    if not os.path.exists(log_path):
        time.sleep(1)
        try:
            bot.edit_message_text(
                B(f"📭 𝐍𝐨 𝐥𝐨𝐠𝐬 𝐟𝐨𝐮𝐧𝐝 𝐟𝐨𝐫 `{file_name}`"),
                message.chat.id, msg.message_id, parse_mode='Markdown',
                reply_markup=create_reply_keyboard_main_menu(user_id)
            )
        except Exception:
            pass
        return
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            log_content = f.read()
        if len(log_content) > 3000:
            log_content = log_content[-3000:]
            log_content = "...\n" + log_content
        
        time.sleep(1.4)
        try:
            bot.edit_message_text(
                B(f"📜 𝐋𝐨𝐠𝐬 𝐟𝐨𝐫 `{file_name}`:\n```\n{log_content}\n```"),
                message.chat.id, msg.message_id, parse_mode='Markdown',
                reply_markup=create_reply_keyboard_main_menu(user_id)
            )
        except Exception:
            pass
    except Exception as e:
        bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐚𝐝𝐢𝐧𝐠 𝐥𝐨𝐠𝐬: {str(e)}"))


def _start_script_silent(user_id, file_name):
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    if not os.path.exists(file_path): return
    file_type = 'py'
    for fname, ftype in user_files.get(user_id, []):
        if fname == file_name:
            file_type = ftype
            break
    if file_type == 'py':
        threading.Thread(target=run_script_silent, args=(file_path, user_id, user_folder, file_name)).start()
    elif file_type == 'js':
        threading.Thread(target=run_js_script_silent, args=(file_path, user_id, user_folder, file_name)).start()

def _stop_script_silent(user_id, file_name):
    script_key = f"{user_id}_{file_name}"
    if script_key in bot_scripts:
        kill_process_tree(bot_scripts[script_key])
        if script_key in bot_scripts:
            del bot_scripts[script_key]
    recovery_system.remove_running_script(user_id, file_name)

def _delete_script_silent(user_id, file_name):
    _stop_script_silent(user_id, file_name)
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    log_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
    if os.path.exists(file_path): os.remove(file_path)
    if os.path.exists(log_path): os.remove(log_path)
    remove_user_file_db(user_id, file_name)

def run_script_silent(file_path, user_id, user_folder, file_name):
    script_key = f"{user_id}_{file_name}"
    log_file_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
    try:
        log_file = open(log_file_path, 'a', encoding='utf-8', errors='ignore')
        process = subprocess.Popen([sys.executable, file_path], cwd=user_folder, stdout=log_file, stderr=log_file, stdin=subprocess.PIPE, encoding='utf-8', errors='ignore')
        bot_scripts[script_key] = {'process': process, 'log_file': log_file, 'file_name': file_name, 'user_id': user_id, 'start_time': datetime.now(), 'type': 'py', 'script_key': script_key}
        recovery_system.save_running_script(user_id, file_name, file_path, process.pid)
        process.wait()
    except: pass
    finally:
        recovery_system.remove_running_script(user_id, file_name)
        if script_key in bot_scripts: del bot_scripts[script_key]
        try: log_file.close()
        except: pass

def run_js_script_silent(file_path, user_id, user_folder, file_name):
    script_key = f"{user_id}_{file_name}"
    log_file_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
    try:
        log_file = open(log_file_path, 'a', encoding='utf-8', errors='ignore')
        process = subprocess.Popen(['node', file_path], cwd=user_folder, stdout=log_file, stderr=log_file, stdin=subprocess.PIPE, encoding='utf-8', errors='ignore')
        bot_scripts[script_key] = {'process': process, 'log_file': log_file, 'file_name': file_name, 'user_id': user_id, 'start_time': datetime.now(), 'type': 'js', 'script_key': script_key}
        recovery_system.save_running_script(user_id, file_name, file_path, process.pid)
        process.wait()
    except: pass
    finally:
        recovery_system.remove_running_script(user_id, file_name)
        if script_key in bot_scripts: del bot_scripts[script_key]
        try: log_file.close()
        except: pass

# ================================
# 𝐒𝐂𝐑𝐈𝐏𝐓 𝐑𝐔𝐍𝐍𝐈𝐍𝐆 𝐅𝐔𝐍𝐂𝐓𝐈𝐎𝐍𝐒
# ================================
def run_script(file_path, user_id, user_folder, file_name, message):
    """𝐑𝐮𝐧 𝐚 𝐏𝐲𝐭𝐡𝐨𝐧 𝐬𝐜𝐫𝐢𝐩𝐭"""
    script_key = f"{user_id}_{file_name}"
    
    if script_key in bot_scripts:
        try:
            bot.reply_to(message, B(f"⚠️ `{file_name}` 𝐢𝐬 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠."))
        except Exception:
            pass
        return
    
    log_file_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
    
    try:
        log_file = open(log_file_path, 'a', encoding='utf-8', errors='ignore')
    except Exception as e:
        try:
            bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫: {str(e)}"))
        except Exception:
            pass
        return
    
    startupinfo = None
    if os.name == 'nt':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
    
    try:
        process = subprocess.Popen(
            [sys.executable, file_path],
            cwd=user_folder,
            stdout=log_file,
            stderr=log_file,
            stdin=subprocess.PIPE,
            startupinfo=startupinfo,
            encoding='utf-8',
            errors='ignore'
        )
        
        bot_scripts[script_key] = {
            'process': process,
            'log_file': log_file,
            'file_name': file_name,
            'user_id': user_id,
            'start_time': datetime.now(),
            'type': 'py',
            'script_key': script_key
        }
        
        # 𝐒𝐚𝐯𝐞 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
        recovery_system.save_running_script(user_id, file_name, file_path, process.pid)
        
        # 𝐒𝐞𝐧𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬 𝐦𝐞𝐬𝐬𝐚𝐠𝐞
        try:
            time.sleep(2)
            bot.edit_message_text(
                B(f"🟢 `{file_name}` 𝐢𝐬 𝐧𝐨𝐰 𝐫𝐮𝐧𝐧𝐢𝐧𝐠!\n📋 𝐏𝐈𝐃: {process.pid}"),
                message.chat.id, message.message_id, parse_mode='Markdown',
                reply_markup=create_reply_keyboard_main_menu(user_id)
            )
        except Exception:
            pass
        
        # 𝐌𝐨𝐧𝐢𝐭𝐨𝐫 𝐩𝐫𝐨𝐜𝐞𝐬𝐬
        try:
            process.wait()
            exit_code = process.returncode
            if exit_code != 0:
                try:
                    bot.send_message(user_id, B(f"⚠️ `{file_name}` 𝐞𝐱𝐢𝐭𝐞𝐝 𝐰𝐢𝐭𝐡 𝐜𝐨𝐝𝐞 {exit_code}."))
                except Exception:
                    pass
        except Exception:
            pass
        finally:
            # 𝐂𝐥𝐞𝐚𝐧𝐮𝐩
            recovery_system.remove_running_script(user_id, file_name)
            if script_key in bot_scripts:
                del bot_scripts[script_key]
            try:
                log_file.close()
            except Exception:
                pass
    
    except Exception as e:
        try:
            bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 `{file_name}`: {str(e)}"))
        except Exception:
            pass
        try:
            log_file.close()
        except Exception:
            pass

def run_js_script(file_path, user_id, user_folder, file_name, message):
    """𝐑𝐮𝐧 𝐚 𝐍𝐨𝐝𝐞.𝐣𝐬 𝐬𝐜𝐫𝐢𝐩𝐭"""
    script_key = f"{user_id}_{file_name}"
    
    if script_key in bot_scripts:
        try:
            bot.reply_to(message, B(f"⚠️ `{file_name}` 𝐢𝐬 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠."))
        except Exception:
            pass
        return
    
    log_file_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
    
    try:
        log_file = open(log_file_path, 'a', encoding='utf-8', errors='ignore')
    except Exception as e:
        try:
            bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫: {str(e)}"))
        except Exception:
            pass
        return
    
    startupinfo = None
    if os.name == 'nt':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
    
    try:
        process = subprocess.Popen(
            ['node', file_path],
            cwd=user_folder,
            stdout=log_file,
            stderr=log_file,
            stdin=subprocess.PIPE,
            startupinfo=startupinfo,
            encoding='utf-8',
            errors='ignore'
        )
        
        bot_scripts[script_key] = {
            'process': process,
            'log_file': log_file,
            'file_name': file_name,
            'user_id': user_id,
            'start_time': datetime.now(),
            'type': 'js',
            'script_key': script_key
        }
        
        # 𝐒𝐚𝐯𝐞 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
        recovery_system.save_running_script(user_id, file_name, file_path, process.pid)
        
        # 𝐒𝐞𝐧𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬 𝐦𝐞𝐬𝐬𝐚𝐠𝐞
        try:
            time.sleep(2)
            bot.edit_message_text(
                B(f"🟢 `{file_name}` 𝐢𝐬 𝐧𝐨𝐰 𝐫𝐮𝐧𝐧𝐢𝐧𝐠!\n📋 𝐏𝐈𝐃: {process.pid}"),
                message.chat.id, message.message_id, parse_mode='Markdown',
                reply_markup=create_reply_keyboard_main_menu(user_id)
            )
        except Exception:
            pass
        
        # 𝐌𝐨𝐧𝐢𝐭𝐨𝐫 𝐩𝐫𝐨𝐜𝐞𝐬𝐬
        try:
            process.wait()
            exit_code = process.returncode
            if exit_code != 0:
                try:
                    bot.send_message(user_id, B(f"⚠️ `{file_name}` 𝐞𝐱𝐢𝐭𝐞𝐝 𝐰𝐢𝐭𝐡 𝐜𝐨𝐝𝐞 {exit_code}."))
                except Exception:
                    pass
        except Exception:
            pass
        finally:
            recovery_system.remove_running_script(user_id, file_name)
            if script_key in bot_scripts:
                del bot_scripts[script_key]
            try:
                log_file.close()
            except Exception:
                pass
    
    except Exception as e:
        try:
            bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 `{file_name}`: {str(e)}"))
        except Exception:
            pass
        try:
            log_file.close()
        except Exception:
            pass


# ================================

# ================================
# ⚡ 𝐋𝐈𝐕𝐄 𝐃𝐘𝐍𝐀𝐌𝐈𝐂 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍 𝐏𝐀𝐓𝐂𝐇
# ================================
# Keep the original AnimationManager and its message-edit engine. These
# compact methods only replace frame content/timing; hosting behavior remains unchanged.
def _live_animation(chat_id, message_id, frames):
    return run_edit_animation(chat_id, message_id, frames, delay=0.45)

def _live_start(chat_id, message_id):
    _live_animation(chat_id, message_id, [
        '⚡ 𝗦𝗧𝗔𝗥𝗧𝗜𝗡𝗚 𝗕𝗢𝗧\n━━━━━━━━━━━━━━\n◐ Initializing runtime...',
        '⚡ 𝗦𝗧𝗔𝗥𝗧𝗜𝗡𝗚 𝗕𝗢𝗧\n━━━━━━━━━━━━━━\n◓ Loading environment...',
        '⚡ 𝗦𝗧𝗔𝗥𝗧𝗜𝗡𝗚 𝗕𝗢𝗧\n━━━━━━━━━━━━━━\n◑ Starting process...',
        '⚡ 𝗦𝗧𝗔𝗥𝗧𝗜𝗡𝗚 𝗕𝗢𝗧\n━━━━━━━━━━━━━━\n◒ Verifying startup...',
        '🟢 𝗕𝗢𝗧 𝗢𝗡𝗟𝗜𝗡𝗘\n━━━━━━━━━━━━━━\nRuntime active'
    ])

def _live_stop(chat_id, message_id):
    _live_animation(chat_id, message_id, [
        '🔴 𝗦𝗧𝗢𝗣𝗣𝗜𝗡𝗚\n━━━━━━━━━━━━━━\n◐ Closing process...',
        '🔴 𝗦𝗧𝗢𝗣𝗣𝗜𝗡𝗚\n━━━━━━━━━━━━━━\n◓ Cleaning workers...',
        '🔴 𝗦𝗧𝗢𝗣𝗣𝗜𝗡𝗚\n━━━━━━━━━━━━━━\n◑ Updating state...',
        '🔴 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣𝗣𝗘𝗗\n━━━━━━━━━━━━━━\nShutdown complete'
    ])

def _live_restart(chat_id, message_id):
    _live_animation(chat_id, message_id, [
        '🔄 𝗥𝗘𝗦𝗧𝗔𝗥𝗧\n━━━━━━━━━━━━━━\n◐ Stopping old instance...',
        '🔄 𝗥𝗘𝗦𝗧𝗔𝗥𝗧\n━━━━━━━━━━━━━━\n◓ Cleaning state...',
        '🔄 𝗥𝗘𝗦𝗧𝗔𝗥𝗧\n━━━━━━━━━━━━━━\n◑ Starting fresh process...',
        '🟢 𝗥𝗘𝗦𝗧𝗔𝗥𝗧𝗘𝗗\n━━━━━━━━━━━━━━\nNew instance online'
    ])

def _live_full_reset(chat_id, message_id):
    _live_animation(chat_id, message_id, [
        '🧹 𝗙𝗨𝗟𝗟 𝗥𝗘𝗦𝗘𝗧\n━━━━━━━━━━━━━━\n◐ Stopping process...',
        '🧹 𝗙𝗨𝗟𝗟 𝗥𝗘𝗦𝗘𝗧\n━━━━━━━━━━━━━━\n◓ Cleaning workers...',
        '🧹 𝗙𝗨𝗟𝗟 𝗥𝗘𝗦𝗘𝗧\n━━━━━━━━━━━━━━\n◑ Clearing runtime...',
        '🧹 𝗙𝗨𝗟𝗟 𝗥𝗘𝗦𝗘𝗧\n━━━━━━━━━━━━━━\n◒ Clearing logs...',
        '✅ 𝗥𝗘𝗦𝗘𝗧 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘\n━━━━━━━━━━━━━━\nReady for fresh run'
    ])

def _live_upload(chat_id, message_id):
    _live_animation(chat_id, message_id, [
        '📤 𝗨𝗣𝗟𝗢𝗔𝗗\n━━━━━━━━━━━━━━\n⠋ Receiving file...',
        '📤 𝗨𝗣𝗟𝗢𝗔𝗗\n━━━━━━━━━━━━━━\n⠙ Processing...',
        '📤 𝗨𝗣𝗟𝗢𝗔𝗗\n━━━━━━━━━━━━━━\n⠹ Preparing runtime...',
        '✅ 𝗨𝗣𝗟𝗢𝗔𝗗𝗘𝗗\n━━━━━━━━━━━━━━\nDeployment ready'
    ])

def _live_logs(chat_id, message_id):
    _live_animation(chat_id, message_id, [
        '📜 𝗟𝗢𝗚 𝗦𝗧𝗥𝗘𝗔𝗠\n━━━━━━━━━━━━━━\n⠋ Reading latest output...',
        '📜 𝗟𝗢𝗚 𝗦𝗧𝗥𝗘𝗔𝗠\n━━━━━━━━━━━━━━\n⠙ Reading latest output...',
        '📜 𝗟𝗢𝗚 𝗦𝗧𝗥𝗘𝗔𝗠\n━━━━━━━━━━━━━━\n⠹ Reading latest output...'
    ])

def _live_dashboard(chat_id, message_id):
    _live_animation(chat_id, message_id, [
        '⚡ 𝗗𝗔𝗦𝗛𝗕𝗢𝗔𝗥𝗗\n━━━━━━━━━━━━━━\n◐ Syncing stats...',
        '⚡ 𝗗𝗔𝗦𝗛𝗕𝗢𝗔𝗥𝗗\n━━━━━━━━━━━━━━\n◓ Loading processes...',
        '⚡ 𝗗𝗔𝗦𝗛𝗕𝗢𝗔𝗥𝗗\n━━━━━━━━━━━━━━\n◑ Checking resources...'
    ])

AnimationManager.animate_start = staticmethod(_live_start)
AnimationManager.animate_stop = staticmethod(_live_stop)
AnimationManager.animate_restart = staticmethod(_live_restart)
AnimationManager.animate_full_reset = staticmethod(_live_full_reset)
AnimationManager.animate_upload = staticmethod(_live_upload)
AnimationManager.animate_logs = staticmethod(_live_logs)
AnimationManager.animate_dashboard = staticmethod(_live_dashboard)

# 𝐒𝐀𝐅𝐄 𝐑𝐔𝐍𝐓𝐈𝐌𝐄 𝐂𝐎𝐍𝐓𝐑𝐎𝐋 𝐀𝐍𝐃 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 𝐌𝐀𝐍𝐀𝐆𝐄𝐑
# ================================
def _script_lock(script_key):
    with _script_locks_guard:
        return _script_locks.setdefault(script_key, threading.RLock())

def _script_key(user_id, file_name):
    return f"{int(user_id)}_{file_name}"

def _user_owns_file(user_id, file_name):
    return any(fname == file_name for fname, _ in user_files.get(user_id, []))

def _process_alive(pid):
    try:
        proc = psutil.Process(int(pid))
        return proc.is_running() and proc.status() != psutil.STATUS_ZOMBIE
    except (psutil.NoSuchProcess, psutil.AccessDenied, ValueError, TypeError):
        return False

def _pid_matches_script(pid, file_path, user_folder):
    try:
        proc = psutil.Process(int(pid))
        if not proc.is_running() or proc.status() == psutil.STATUS_ZOMBIE:
            return False
        cwd = os.path.abspath(proc.cwd()) if proc.cwd() else ''
        if cwd and os.path.abspath(user_folder) != cwd:
            return False
        cmd = ' '.join(proc.cmdline())
        return os.path.basename(file_path) in cmd or os.path.abspath(file_path) in cmd
    except (psutil.Error, OSError, ValueError, TypeError):
        return False

def _load_recovery_records():
    try:
        with _state_file_lock:
            if not os.path.exists(RUNNING_SCRIPTS_DB):
                return []
            with open(RUNNING_SCRIPTS_DB, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            return list(data.get('running_scripts', []))
    except Exception as exc:
        logger.error(f"Recovery state read failed: {exc}")
        return []

def _write_recovery_records(records):
    tmp = f"{RUNNING_SCRIPTS_DB}.tmp"
    with _state_file_lock:
        with open(tmp, 'w', encoding='utf-8') as fh:
            json.dump({'running_scripts': records}, fh, indent=4)
        os.replace(tmp, RUNNING_SCRIPTS_DB)

def _recovery_record(user_id, file_name):
    for record in _load_recovery_records():
        if record.get('user_id') == user_id and record.get('file_name') == file_name:
            return record
    return None

def _remove_runtime_files(user_folder, file_name):
    """Remove only hosting-created temporary runtime artifacts, never the upload."""
    stem = os.path.splitext(file_name)[0]
    for name in (f'{stem}.pid', f'{stem}.runtime.json', f'{stem}.state.json', f'.{stem}.lock'):
        path = os.path.join(user_folder, name)
        try:
            if os.path.isfile(path):
                os.remove(path)
        except Exception as exc:
            logger.warning(f"Could not remove runtime file {path}: {exc}")

def _verify_stopped(pid, timeout=4.0):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if not _process_alive(pid):
            return True
        time.sleep(0.15)
    return not _process_alive(pid)

def kill_process_tree(process_info):
    """Terminate only the known process and its descendants, then verify exit."""
    try:
        process = process_info.get('process') if isinstance(process_info, dict) else None
        pid = getattr(process, 'pid', None) or (process_info.get('process_pid') if isinstance(process_info, dict) else None)
        if not pid:
            return True
        try:
            parent = psutil.Process(int(pid))
            children = parent.children(recursive=True)
        except psutil.NoSuchProcess:
            return True
        targets = children + [parent]
        for child in children:
            try:
                child.terminate()
            except psutil.Error:
                pass
        try:
            parent.terminate()
        except psutil.Error:
            pass
        _, alive = psutil.wait_procs(targets, timeout=3)
        for proc in alive:
            try:
                proc.kill()
            except psutil.Error:
                pass
        _, alive = psutil.wait_procs(alive, timeout=2)
        return not alive and _verify_stopped(pid)
    except Exception as exc:
        logger.error(f"Process-tree cleanup failed: {exc}")
        return False

def is_bot_running(user_id, file_name):
    """Return true only for a verified live process belonging to this user's file."""
    key = _script_key(user_id, file_name)
    info = bot_scripts.get(key)
    if info and getattr(info.get('process'), 'pid', None):
        pid = info['process'].pid
        if _process_alive(pid):
            return True
        bot_scripts.pop(key, None)
        recovery_system.remove_running_script(user_id, file_name)
    record = _recovery_record(user_id, file_name)
    if record:
        path = record.get('file_path') or os.path.join(get_user_folder(user_id), file_name)
        if _pid_matches_script(record.get('process_pid'), path, get_user_folder(user_id)):
            return True
        recovery_system.remove_running_script(user_id, file_name)
    return False

def _cleanup_script_runtime(user_id, file_name, clear_log=False):
    key = _script_key(user_id, file_name)
    user_folder = get_user_folder(user_id)
    info = bot_scripts.get(key)
    record = _recovery_record(user_id, file_name)
    if not info and record:
        info = {'process_pid': record.get('process_pid'), 'user_id': user_id, 'file_name': file_name}
    ok = True
    if info:
        ok = kill_process_tree(info) and ok
        log_file = info.get('log_file')
        try:
            if log_file:
                log_file.close()
        except Exception:
            pass
    bot_scripts.pop(key, None)
    recovery_system.remove_running_script(user_id, file_name)
    _remove_runtime_files(user_folder, file_name)
    if clear_log:
        log_path = os.path.join(user_folder, f'{os.path.splitext(file_name)[0]}.log')
        try:
            with open(log_path, 'w', encoding='utf-8'):
                pass
        except Exception as exc:
            logger.error(f'Could not clear log {log_path}: {exc}')
            ok = False
    return ok

def _launch_script(file_path, user_id, user_folder, file_name, file_type='py', message=None):
    key = _script_key(user_id, file_name)
    with _script_lock(key):
        if not _user_owns_file(user_id, file_name) or not os.path.isfile(file_path):
            return False
        if is_bot_running(user_id, file_name):
            if message:
                try:
                    bot.reply_to(message, B(f'⚠️ 𝐁𝐎𝐓 𝐀𝐋𝐑𝐄𝐀𝐃𝐘 𝐑𝐔𝐍𝐍𝐈𝐍𝐆\n━━━━━━━━━━━━━━━━━━━━\n🤖 {file_name}\n\n𝐀 𝐬𝐞𝐜𝐨𝐧𝐝 𝐢𝐧𝐬𝐭𝐚𝐧𝐜𝐞 𝐰𝐚𝐬 𝐧𝐨𝐭 𝐬𝐭𝐚𝐫𝐭𝐞𝐝.'))
                except Exception:
                    pass
            return False
        log_path = os.path.join(user_folder, f'{os.path.splitext(file_name)[0]}.log')
        log_file = open(log_path, 'a', encoding='utf-8', errors='ignore')
        cmd = [sys.executable, file_path] if file_type == 'py' else ['node', file_path]
        try:
            process = subprocess.Popen(cmd, cwd=user_folder, stdout=log_file, stderr=log_file, stdin=subprocess.PIPE, encoding='utf-8', errors='ignore')
        except Exception:
            log_file.close()
            raise
        bot_scripts[key] = {'process': process, 'log_file': log_file, 'file_name': file_name, 'user_id': user_id, 'start_time': datetime.now(), 'type': file_type, 'script_key': key}
        recovery_system.save_running_script(user_id, file_name, file_path, process.pid)
        return process, log_file

def _monitor_launched(process, log_file, user_id, file_name):
    key = _script_key(user_id, file_name)
    try:
        process.wait()
    except Exception:
        pass
    finally:
        try:
            log_file.close()
        except Exception:
            pass
        current = bot_scripts.get(key)
        if current and getattr(current.get('process'), 'pid', None) == getattr(process, 'pid', None):
            bot_scripts.pop(key, None)
            recovery_system.remove_running_script(user_id, file_name)

def run_script(file_path, user_id, user_folder, file_name, message):
    try:
        launched = _launch_script(file_path, user_id, user_folder, file_name, 'py', message)
        if launched:
            process, log_file = launched
            _monitor_launched(process, log_file, user_id, file_name)
    except Exception as exc:
        logger.error(f'Python launch failed for {file_name}: {exc}', exc_info=True)
        try:
            bot.reply_to(message, B(f'❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 `{file_name}`.'))
        except Exception:
            pass

def run_js_script(file_path, user_id, user_folder, file_name, message):
    try:
        launched = _launch_script(file_path, user_id, user_folder, file_name, 'js', message)
        if launched:
            process, log_file = launched
            _monitor_launched(process, log_file, user_id, file_name)
    except Exception as exc:
        logger.error(f'Node launch failed for {file_name}: {exc}', exc_info=True)
        try:
            bot.reply_to(message, B(f'❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 `{file_name}`.'))
        except Exception:
            pass

def run_script_silent(file_path, user_id, user_folder, file_name):
    run_script(file_path, user_id, user_folder, file_name, None)

def run_js_script_silent(file_path, user_id, user_folder, file_name):
    run_js_script(file_path, user_id, user_folder, file_name, None)

def _stop_script(message, user_id, file_name):
    if not _user_owns_file(user_id, file_name):
        return
    status = bot.reply_to(message, B(f'🔴 𝗦𝗧𝗢𝗣𝗣𝗜𝗡𝗚\n━━━━━━━━━━━━━━\n◐ Closing process...'))
    AnimationManager.animate_stop(status.chat.id, status.message_id)
    with _script_lock(_script_key(user_id, file_name)):
        ok = _cleanup_script_runtime(user_id, file_name)
    time.sleep(1.9)
    try:
        bot.edit_message_text(B(f'🔴 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣𝗣𝗘𝗗\n━━━━━━━━━━━━━━\nShutdown complete\n\n🤖 {file_name}'), status.chat.id, status.message_id, reply_markup=create_reply_keyboard_main_menu(user_id))
    except Exception:
        pass

def _stop_script_silent(user_id, file_name):
    with _script_lock(_script_key(user_id, file_name)):
        if _user_owns_file(user_id, file_name):
            _cleanup_script_runtime(user_id, file_name)

def _restart_script(message, user_id, file_name):
    with _script_lock(_script_key(user_id, file_name)):
        if not _user_owns_file(user_id, file_name):
            return
        user_folder = get_user_folder(user_id)
        file_path = os.path.join(user_folder, file_name)
        if not os.path.isfile(file_path):
            bot.reply_to(message, B(f'❌ 𝐅𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝: `{file_name}`'))
            return
        _cleanup_script_runtime(user_id, file_name)
        time.sleep(0.4)
        file_type = next((ftype for fname, ftype in user_files.get(user_id, []) if fname == file_name), 'py')
        launched = _launch_script(file_path, user_id, user_folder, file_name, file_type, message)
        if launched:
            threading.Thread(target=lambda: _monitor_launched(*launched, user_id, file_name), daemon=True).start()

def _clear_logs(message, user_id, file_name):
    if not _user_owns_file(user_id, file_name):
        return
    path = os.path.join(get_user_folder(user_id), f'{os.path.splitext(file_name)[0]}.log')
    try:
        if not os.path.exists(path):
            bot.reply_to(message, B(f'📜 𝐍𝐎 𝐋𝐎𝐆𝐒 𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄\n\n🤖 {file_name}'))
            return
        with open(path, 'w', encoding='utf-8'):
            pass
        bot.reply_to(message, B(f'🧹 𝐋𝐎𝐆𝐒 𝐂𝐋𝐄𝐀𝐑𝐄𝐃\n━━━━━━━━━━━━━━━━━━━━\n🤖 {file_name}\n\n📜 𝐏𝐫𝐞𝐯𝐢𝐨𝐮𝐬 𝐥𝐨𝐠𝐬 𝐜𝐥𝐞𝐚𝐫𝐞𝐝.\n🟢 𝐁𝐨𝐭 𝐩𝐫𝐨𝐜𝐞𝐬𝐬 𝐰𝐚𝐬 𝐧𝐨𝐭 𝐬𝐭𝐨𝐩𝐩𝐞𝐝.'))
    except Exception as exc:
        logger.error(f'Clear logs failed: {exc}', exc_info=True)
        bot.reply_to(message, B('❌ 𝐂𝐋𝐄𝐀𝐑 𝐋𝐎𝐆𝐒 𝐅𝐀𝐈𝐋𝐄𝐃'))

def _request_full_reset(message, user_id, file_name):
    if not _user_owns_file(user_id, file_name):
        return
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('✅ CONFIRM RESET', callback_data=f'confirm_reset_{file_name}'), types.InlineKeyboardButton('❌ CANCEL', callback_data='cancel_reset'))
    bot.reply_to(message, B(f'⚠️ 𝐂𝐎𝐍𝐅𝐈𝐑𝐌 𝐅𝐔𝐋𝐋 𝐑𝐄𝐒𝐄𝐓\n━━━━━━━━━━━━━━━━━━━━\n🤖 𝐁𝐨𝐭: {file_name}\n\n𝐓𝐡𝐢𝐬 𝐰𝐢𝐥𝐥 𝐜𝐥𝐞𝐚𝐧 𝐭𝐡𝐞 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐩𝐫𝐨𝐜𝐞𝐬𝐬, 𝐰𝐨𝐫𝐤𝐞𝐫𝐬, 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐬𝐭𝐚𝐭𝐞, 𝐫𝐮𝐧𝐭𝐢𝐦𝐞 𝐬𝐭𝐚𝐭𝐞 𝐚𝐧𝐝 𝐥𝐨𝐠𝐬.\n\n𝐘𝐨𝐮𝐫 𝐟𝐢𝐥𝐞, 𝐚𝐜𝐜𝐨𝐮𝐧𝐭 𝐚𝐧𝐝 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐰𝐢𝐥𝐥 𝐍𝐎𝐓 𝐛𝐞 𝐝𝐞𝐥𝐞𝐭𝐞𝐝.\n\n𝐂𝐨𝐧𝐭𝐢𝐧𝐮𝐞?'), reply_markup=markup)

def _perform_full_reset(call, user_id, file_name):
    if not _user_owns_file(user_id, file_name):
        bot.answer_callback_query(call.id, 'Not authorized', show_alert=True)
        return
    AnimationManager.animate_full_reset(call.message.chat.id, call.message.message_id)
    with _script_lock(_script_key(user_id, file_name)):
        ok = _cleanup_script_runtime(user_id, file_name, clear_log=True)
    bot.answer_callback_query(call.id, 'Reset complete' if ok else 'Reset completed with warnings', show_alert=not ok)
    try:
        bot.edit_message_text(B(f'✅ 𝐑𝐄𝐒𝐄𝐓 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄\n━━━━━━━━━━━━━━━━━━━━\n🤖 {file_name}\n\n🛑 𝐏𝐫𝐨𝐜𝐞𝐬𝐬: 𝐒𝐭𝐨𝐩𝐩𝐞𝐝\n👶 𝐖𝐨𝐫𝐤𝐞𝐫𝐬: 𝐂𝐥𝐞𝐚𝐧𝐞𝐝\n🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲: 𝐂𝐥𝐞𝐚𝐫𝐞𝐝\n📜 𝐋𝐨𝐠𝐬: 𝐂𝐥𝐞𝐚𝐫𝐞𝐝\n\n📁 𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐟𝐢𝐥𝐞 𝐫𝐞𝐦𝐚𝐢𝐧𝐬 𝐢𝐧𝐭𝐚𝐜𝐭.'), call.message.chat.id, call.message.message_id, reply_markup=create_reply_keyboard_main_menu(user_id))
    except Exception:
        pass

def _safe_database_copy():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    destination = os.path.join(tempfile.gettempdir(), f'hosting_backup_{timestamp}.db')
    source_conn = sqlite3.connect(DATABASE_PATH, timeout=30)
    destination_conn = sqlite3.connect(destination)
    try:
        source_conn.backup(destination_conn)
        destination_conn.commit()
    finally:
        destination_conn.close()
        source_conn.close()
    return destination

def create_database_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('👥 Users', callback_data='db_users'), types.InlineKeyboardButton('📁 Files', callback_data='db_files'))
    markup.add(types.InlineKeyboardButton('🟢 Running Scripts', callback_data='db_running'), types.InlineKeyboardButton('💳 Subscriptions', callback_data='db_subscriptions'))
    markup.add(types.InlineKeyboardButton('📤 Export Database', callback_data='db_export'), types.InlineKeyboardButton('💾 Backup Database', callback_data='db_backup'))
    return markup

def _database_summary(call, kind):
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, 'Admin/owner only', show_alert=True)
        return
    queries = {'db_users': ('Users', 'SELECT COUNT(*) FROM active_users'), 'db_files': ('Files', 'SELECT COUNT(*) FROM user_files')}
    title, query = queries.get(kind, ('Database', 'SELECT 1'))
    try:
        with sqlite3.connect(DATABASE_PATH, timeout=30) as conn:
            value = conn.execute(query).fetchone()[0]
        bot.edit_message_text(B(f'🗄️ 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 𝐌𝐀𝐍𝐀𝐆𝐄𝐑\n\n{title}: {value}'), call.message.chat.id, call.message.message_id, reply_markup=create_database_keyboard())
    except Exception as exc:
        logger.error(f'Database summary failed: {exc}', exc_info=True)
        bot.answer_callback_query(call.id, 'Database error', show_alert=True)

def _database_file_action(call, export=False):
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, 'Admin/owner only', show_alert=True)
        return
    path = None
    try:
        path = _safe_database_copy()
        with open(path, 'rb') as fh:
            bot.send_document(call.from_user.id, fh, caption=B('📤 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐞𝐱𝐩𝐨𝐫𝐭 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞.'))
        bot.answer_callback_query(call.id, 'Database sent')
    except Exception as exc:
        logger.error(f'Database export/backup failed: {exc}', exc_info=True)
        bot.answer_callback_query(call.id, 'Database operation failed', show_alert=True)
    finally:
        if path:
            try:
                os.remove(path)
            except OSError:
                pass

# ================================
# 𝐈𝐍𝐋𝐈𝐍𝐄 𝐁𝐔𝐓𝐓𝐎𝐍 (𝐂𝐀𝐋𝐋𝐁𝐀𝐂𝐊) 𝐇𝐀𝐍𝐃𝐋𝐄𝐑𝐒
# ================================
def create_manage_scripts_keyboard(user_id):
    """𝐂𝐫𝐞𝐚𝐭𝐞 𝐢𝐧𝐥𝐢𝐧𝐞 𝐤𝐞𝐲𝐛𝐨𝐚𝐫𝐝 𝐟𝐨𝐫 𝐦𝐚𝐧𝐚𝐠𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭𝐬"""
    markup = types.InlineKeyboardMarkup()
    files = user_files.get(user_id, [])
    if not files:
        return None
    
    for fname, ftype in files:
        running = is_bot_running(user_id, fname)
        status_text = "🟢 Running" if running else "🔴 Stopped"
        
        # Header button (just for display)
        markup.add(types.InlineKeyboardButton(f"📂 {fname} | {status_text}", callback_data=f"info_{fname}"))
        
        # Control buttons
        row = []
        if running:
            row.append(types.InlineKeyboardButton("⏹ Stop", callback_data=f"stop_script_{fname}"))
        else:
            row.append(types.InlineKeyboardButton("▶ Start", callback_data=f"start_script_{fname}"))
        
        row.append(types.InlineKeyboardButton("🗑 Delete", callback_data=f"delete_script_{fname}"))
        row.append(types.InlineKeyboardButton("🧹 Clear Logs", callback_data=f"clear_logs_{fname}"))
        row.append(types.InlineKeyboardButton("🧹 Full Reset", callback_data=f"reset_script_{fname}"))
        markup.add(*row)
        
        # Divider
        markup.add(types.InlineKeyboardButton("━━━━━━━━━━━━━━", callback_data="none"))
        
    markup.add(types.InlineKeyboardButton("🔄 Refresh List", callback_data="manage_scripts"))
    return markup

def show_manage_scripts(message, user_id):
    """𝐃𝐢𝐬𝐩𝐥𝐚𝐲 𝐭𝐡𝐞 𝐌𝐚𝐧𝐚𝐠𝐞 𝐒𝐜𝐫𝐢𝐩𝐭𝐬 𝐩𝐚𝐧𝐞𝐥"""
    files = user_files.get(user_id, [])
    if not files:
        bot.reply_to(message, B("📂 𝐍𝐨 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐲𝐞𝐭."), 
                     reply_markup=create_reply_keyboard_main_menu(user_id))
        return

    kb = create_manage_scripts_keyboard(user_id)
    bot.reply_to(message, B("📂 𝐌𝐀𝐍𝐀𝐆𝐄 𝐒𝐂𝐑𝐈𝐏𝐓𝐒\n\n𝐒𝐞𝐥𝐞𝐜𝐭 𝐚 𝐬𝐜𝐫𝐢𝐩𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐫𝐨𝐥:"), 
                 reply_markup=kb, parse_mode='Markdown')

def update_manage_scripts_message(call, user_id):
    """𝐔𝐩𝐝𝐚𝐭𝐞 𝐭𝐡𝐞 𝐞𝐱𝐢𝐬𝐭𝐢𝐧𝐠 𝐌𝐚𝐧𝐚𝐠𝐞 𝐒𝐜𝐫𝐢𝐩𝐭𝐬 𝐩𝐚𝐧𝐞𝐥"""
    kb = create_manage_scripts_keyboard(user_id)
    if not kb:
        bot.edit_message_text(B("📂 𝐍𝐨 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐲𝐞𝐭."), 
                             call.message.chat.id, call.message.message_id, 
                             reply_markup=create_reply_keyboard_main_menu(user_id))
        return
    
    try:
        bot.edit_message_text(B("📂 𝐌𝐀𝐍𝐀𝐆𝐄 𝐒𝐂𝐑𝐈𝐏𝐓𝐒\n\n𝐒𝐞𝐥𝐞𝐜𝐭 𝐚 𝐬𝐜𝐫𝐢𝐩𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐫𝐨𝐥:"), 
                             call.message.chat.id, call.message.message_id, 
                             reply_markup=kb, parse_mode='Markdown')
    except Exception as e:
        if "message is not modified" not in str(e).lower():
            logger.error(f"Error updating scripts list: {e}")

@bot.callback_query_handler(func=lambda call: True)
def callback_router(call):
    """𝐌𝐚𝐢𝐧 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤 𝐫𝐨𝐮𝐭𝐞𝐫"""
    user_id = call.from_user.id
    add_active_user(user_id)
    data = call.data
    
    try:
        if data == 'manage_scripts':
            update_manage_scripts_message(call, user_id)
            
        elif data.startswith('start_script_'):
            file_name = data.replace('start_script_', '')
            if not _user_owns_file(user_id, file_name):
                bot.answer_callback_query(call.id, 'Not authorized', show_alert=True)
                return
            if is_bot_running(user_id, file_name):
                bot.answer_callback_query(call.id, "⚠️ BOT ALREADY RUNNING — second instance was not started", show_alert=True)
            else:
                bot.answer_callback_query(call.id, "🚀 Starting...")
                _start_script_silent(user_id, file_name)
                time.sleep(1)
                update_manage_scripts_message(call, user_id)

        elif data.startswith('stop_script_'):
            file_name = data.replace('stop_script_', '')
            if not _user_owns_file(user_id, file_name):
                bot.answer_callback_query(call.id, 'Not authorized', show_alert=True)
                return
            if not is_bot_running(user_id, file_name):
                bot.answer_callback_query(call.id, "⚠️ Already Stopped", show_alert=True)
            else:
                bot.answer_callback_query(call.id, "🛑 Stopping...")
                _stop_script_silent(user_id, file_name)
                time.sleep(1)
                update_manage_scripts_message(call, user_id)

        elif data.startswith('delete_script_'):
            file_name = data.replace('delete_script_', '')
            if not _user_owns_file(user_id, file_name):
                bot.answer_callback_query(call.id, 'Not authorized', show_alert=True)
                return
            bot.answer_callback_query(call.id, "🗑 Deleting...")
            _delete_script_silent(user_id, file_name)
            time.sleep(1)
            update_manage_scripts_message(call, user_id)
            
        elif data.startswith('confirm_reset_'):
            _perform_full_reset(call, user_id, data.replace('confirm_reset_', '', 1))

        elif data == 'cancel_reset':
            bot.answer_callback_query(call.id, 'Reset cancelled')
            try: bot.delete_message(call.message.chat.id, call.message.message_id)
            except Exception: pass

        elif data.startswith('reset_script_'):
            _request_full_reset(call.message, user_id, data.replace('reset_script_', '', 1))

        elif data.startswith('clear_logs_'):
            _clear_logs(call.message, user_id, data.replace('clear_logs_', '', 1))
            bot.answer_callback_query(call.id, 'Logs cleared')

        elif data.startswith('db_'):
            if data in ('db_users', 'db_files', 'db_running', 'db_subscriptions'):
                _database_summary(call, data)
            elif data in ('db_export', 'db_backup'):
                _database_file_action(call, export=data == 'db_export')

        elif data == 'upload':
            bot.answer_callback_query(call.id, "📤 𝐔𝐩𝐥𝐨𝐚𝐝 𝐚 .𝐩𝐲 𝐨𝐫 .𝐣𝐬 𝐟𝐢𝐥𝐞")
            bot.edit_message_text(
                B("📤 𝐒𝐞𝐧𝐝 𝐲𝐨𝐮𝐫 .𝐩𝐲 𝐨𝐫 .𝐣𝐬 𝐟𝐢𝐥𝐞 𝐧𝐨𝐰!\\n\\n📋 𝐒𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝: .𝐩𝐲, .𝐣𝐬, .𝐳𝐢𝐩"),
                call.message.chat.id, call.message.message_id, parse_mode='Markdown',
                reply_markup=create_reply_keyboard_main_menu(user_id)
            )
        
        elif data == 'speed':
            bot.answer_callback_query(call.id, "⚡ 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐩𝐞𝐞𝐝 𝐭𝐞𝐬𝐭...")
            run_speedtest_callback(call, user_id)
        
        elif data == 'stats':
            show_stats_callback(call, user_id)
        
        elif data == 'profile':
            show_profile_callback(call, user_id)
        
        elif data == 'module_menu':
            _callback_module_menu(call, user_id)
        
        elif data == 'restart_all':
            _callback_restart_all(call, user_id)
            
        elif data == 'recover_all':
            _callback_recover_all(call, user_id)
            
        elif data == 'restart_bot':
            if user_id == OWNER_ID:
                _callback_restart_bot(call, user_id)
            else:
                bot.answer_callback_query(call.id, "🔒 𝐎𝐰𝐧𝐞𝐫 𝐨𝐧𝐥𝐲.", show_alert=True)
        
        elif data.startswith('info_'):
            file_name = data.replace('info_', '')
            bot.answer_callback_query(call.id, f"📂 {file_name}")
            
        elif data == 'none':
            bot.answer_callback_query(call.id, "━━━━━━━━━━━━━━")
            
        else:
            bot.answer_callback_query(call.id, "🔍 𝐔𝐧𝐤𝐧𝐨𝐰𝐧 𝐚𝐜𝐭𝐢𝐨𝐧")
    
    except Exception as e:
        logger.error(f"❌ 𝐂𝐚𝐥𝐥𝐛𝐚𝐜𝐤 𝐞𝐫𝐫𝐨𝐫: {e}")
        bot.answer_callback_query(call.id, "❌ 𝐄𝐫𝐫𝐨𝐫", show_alert=True)

# ================================
# 𝐂𝐀𝐋𝐋𝐁𝐀𝐂𝐊 𝐈𝐌𝐏𝐋𝐄𝐌𝐄𝐍𝐓𝐀𝐓𝐈𝐎𝐍𝐒
# ================================
def _callback_check_files(call, user_id):
    """𝐒𝐡𝐨𝐰 𝐮𝐬𝐞𝐫'𝐬 𝐟𝐢𝐥𝐞𝐬"""
    files = user_files.get(user_id, [])
    
    if not files:
        bot.edit_message_text(B("📂 𝐍𝐨 𝐟𝐢𝐥𝐞𝐬 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐲𝐞𝐭.\n📤 𝐔𝐩𝐥𝐨𝐚𝐝 𝐚 .𝐩𝐲 𝐨𝐫 .𝐣𝐬 𝐟𝐢𝐥𝐞!"),
                             call.message.chat.id, call.message.message_id,
                             reply_markup=create_reply_keyboard_main_menu(user_id))
        return
    
    bot.answer_callback_query(call.id, "📂 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞𝐬")
    
    files_text = f"╔══════════════════════════════════╗\n"
    files_text += "║    📂 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄𝐒                  ║\n"
    files_text += "╚══════════════════════════════════╝\n\n"
    
    for fname, ftype in files:
        running = "🟢" if is_bot_running(user_id, fname) else "🔴"
        files_text += f"{running} `{fname}` ({ftype})\n"
    
    files_text += f"\n📊 *𝐓𝐨𝐭𝐚𝐥:* {len(files)} 𝐟𝐢𝐥𝐞𝐬"
    
    bot.edit_message_text(files_text, call.message.chat.id, call.message.message_id, parse_mode='Markdown',
                          reply_markup=create_reply_keyboard_main_menu(user_id))

def _callback_module_menu(call, user_id):
    """𝐒𝐡𝐨𝐰 𝐦𝐨𝐝𝐮𝐥𝐞 𝐦𝐞𝐧𝐮"""
    bot.answer_callback_query(call.id, "📦 𝐌𝐨𝐝𝐮𝐥𝐞 𝐌𝐞𝐧𝐮")
    
    module_text = f"""╔══════════════════════════════════╗
║    📦 𝐌𝐎𝐃𝐔𝐋𝐄 𝐌𝐀𝐍𝐀𝐆𝐄𝐑             ║
╚══════════════════════════════════╝

*𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝 𝐌𝐨𝐝𝐮𝐥𝐞𝐬:*
📦 𝐓𝐞𝐥𝐞𝐛𝐨𝐭, 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐬, 𝐏𝐬𝐮𝐭𝐢𝐥, 𝐅𝐥𝐚𝐬𝐤
📦 𝐐𝐫𝐜𝐨𝐝𝐞, 𝐏𝐢𝐥𝐥𝐨𝐰, 𝐂𝐫𝐲𝐩𝐭𝐨𝐠𝐫𝐚𝐩𝐡𝐲

*𝐔𝐩𝐥𝐨𝐚𝐝 𝐚 𝐬𝐜𝐫𝐢𝐩𝐭 𝐭𝐨 𝐚𝐮𝐭𝐨-𝐢𝐧𝐬𝐭𝐚𝐥𝐥 𝐝𝐞𝐩𝐞𝐧𝐝𝐞𝐧𝐜𝐢𝐞𝐬!*"""
    
    bot.edit_message_text(module_text, call.message.chat.id, call.message.message_id, parse_mode='Markdown',
                          reply_markup=create_reply_keyboard_main_menu(user_id))

def _callback_restart_all(call, user_id):
    """𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐚𝐥𝐥 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭𝐬"""
    bot.answer_callback_query(call.id, "🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐚𝐥𝐥 𝐬𝐜𝐫𝐢𝐩𝐭𝐬...")
    
    msg = bot.edit_message_text(B("🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐚𝐥𝐥 𝐬𝐜𝐫𝐢𝐩𝐭𝐬..."),
                                call.message.chat.id, call.message.message_id,
                                reply_markup=create_reply_keyboard_main_menu(user_id))
    
    restarted = 0
    for script_key, script_info in list(bot_scripts.items()):
        if script_info['user_id'] == user_id:
            try:
                if is_bot_running(user_id, script_info['file_name']):
                    kill_process_tree(script_info)
                    del bot_scripts[script_key]
                    time.sleep(0.5)
                    
                    user_folder = get_user_folder(user_id)
                    file_path = os.path.join(user_folder, script_info['file_name'])
                    
                    if os.path.exists(file_path):
                        if script_info['type'] == 'py':
                            threading.Thread(target=run_script,
                                           args=(file_path, user_id, user_folder,
                                                 script_info['file_name'], msg)).start()
                        else:
                            threading.Thread(target=run_js_script,
                                           args=(file_path, user_id, user_folder,
                                                 script_info['file_name'], msg)).start()
                        restarted += 1
            except Exception:
                pass
    
    try:
        bot.edit_message_text(B(f"✅ {restarted} 𝐬𝐜𝐫𝐢𝐩𝐭(𝐬) 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝."),
                             call.message.chat.id, call.message.message_id,
                             reply_markup=create_reply_keyboard_main_menu(user_id))
    except Exception:
        pass

def _callback_recover_all(call, user_id):
    """𝐑𝐞𝐜𝐨𝐯𝐞𝐫 𝐚𝐥𝐥 𝐬𝐜𝐫𝐢𝐩𝐭𝐬"""
    bot.answer_callback_query(call.id, "🛰 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭𝐬...")
    
    msg = bot.edit_message_text(B("🛰 𝐈𝐧𝐢𝐭𝐢𝐚𝐭𝐢𝐧𝐠 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲..."),
                                call.message.chat.id, call.message.message_id)
    
    # 𝐑𝐮𝐧 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
    try:
        AnimationManager.animate_recovery(call.message.chat.id, msg.message_id)
    except Exception:
        pass
    
    time.sleep(2)
    
    recovered = recovery_system.recover_all_scripts()
    
    try:
        if recovered:
            bot.edit_message_text(
                B(f"✅ 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞!\n🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐞𝐝: {len(recovered)} 𝐬𝐜𝐫𝐢𝐩𝐭(𝐬)"),
                call.message.chat.id, msg.message_id,
                reply_markup=create_reply_keyboard_main_menu(user_id)
            )
        else:
            bot.edit_message_text(B("📭 𝐍𝐨 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫."),
                                 call.message.chat.id, msg.message_id,
                                 reply_markup=create_reply_keyboard_main_menu(user_id))
    except Exception:
        pass

def _callback_analytics(call, user_id):
    """𝐒𝐡𝐨𝐰 𝐚𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐬"""
    bot.answer_callback_query(call.id, "📈 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐚𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐬...")
    
    total_files = sum(len(files) for files in user_files.values())
    running_count = len(bot_scripts)
    total_users = len(active_users)
    total_subs = len(user_subscriptions)
    
    analytics_text = f"""╔══════════════════════════════════╗
║    📈 𝐀𝐍𝐀𝐋𝐘𝐓𝐈𝐂𝐒                    ║
╚══════════════════════════════════╝

👥 *𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬:* {total_users}
📂 *𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬:* {total_files}
🚀 *𝐑𝐮𝐧𝐧𝐢𝐧𝐠:* {running_count}
💳 *𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧𝐬:* {total_subs}

*𝐌𝐞𝐦𝐨𝐫𝐲:* {psutil.virtual_memory().percent}%
*𝐂𝐏𝐔:* {psutil.cpu_percent()}%"""
    
    bot.edit_message_text(analytics_text, call.message.chat.id, call.message.message_id, parse_mode='Markdown',
                          reply_markup=create_reply_keyboard_main_menu(user_id))

def _callback_restart_bot(call, user_id):
    """𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐛𝐨𝐭"""
    bot.answer_callback_query(call.id, "🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐛𝐨𝐭...")
    
    msg = bot.edit_message_text(B("🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐛𝐨𝐭..."),
                                call.message.chat.id, call.message.message_id)
    
    # 𝐑𝐮𝐧 𝐟𝐮𝐥𝐥 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
    try:
        AnimationManager.animate_full_restart(call.message.chat.id, msg.message_id)
    except Exception:
        pass
    
    time.sleep(2.5)
    
    # 𝐒𝐞𝐧𝐝 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬
    threading.Thread(target=send_restart_notification).start()
    
    # 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐛𝐨𝐭
    os.execl(sys.executable, sys.executable, *sys.argv)

def _callback_restart_script(call, user_id, file_name):
    """𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐬𝐜𝐫𝐢𝐩𝐭 𝐟𝐫𝐨𝐦 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    bot.answer_callback_query(call.id, f"🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 {file_name}...")
    _restart_script_from_callback(call, user_id, file_name)

def _start_script_from_callback(call, user_id, file_name):
    """𝐒𝐭𝐚𝐫𝐭 𝐬𝐜𝐫𝐢𝐩𝐭 𝐟𝐫𝐨𝐦 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    
    if not os.path.exists(file_path):
        bot.answer_callback_query(call.id, "❌ 𝐅𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝", show_alert=True)
        return
    
    if is_bot_running(user_id, file_name):
        bot.answer_callback_query(call.id, f"⚠️ {file_name} 𝐢𝐬 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠", show_alert=True)
        return
    
    file_type = 'py'
    for fname, ftype in user_files.get(user_id, []):
        if fname == file_name:
            file_type = ftype
            break
    
    msg = bot.edit_message_text(B(f"🚀 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 `{file_name}`..."),
                                call.message.chat.id, call.message.message_id,
                                reply_markup=create_reply_keyboard_main_menu(user_id))
    
    try:
        AnimationManager.animate_start(call.message.chat.id, msg.message_id)
    except Exception:
        pass
    
    if file_type == 'py':
        threading.Thread(target=run_script, args=(file_path, user_id, user_folder, file_name, msg)).start()
    elif file_type == 'js':
        threading.Thread(target=run_js_script, args=(file_path, user_id, user_folder, file_name, msg)).start()

def _stop_script_from_callback(call, user_id, file_name):
    """𝐒𝐭𝐨𝐩 𝐬𝐜𝐫𝐢𝐩𝐭 𝐟𝐫𝐨𝐦 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    script_key = f"{user_id}_{file_name}"
    if not is_bot_running(user_id, file_name):
        bot.answer_callback_query(call.id, f"⚠️ {file_name} 𝐢𝐬 𝐧𝐨𝐭 𝐫𝐮𝐧𝐧𝐢𝐧𝐠", show_alert=True)
        return
    
    bot.answer_callback_query(call.id, f"🛑 𝐒𝐭𝐨𝐩𝐩𝐢𝐧𝐠 {file_name}...")
    
    msg = bot.edit_message_text(B(f"🛑 𝐒𝐭𝐨𝐩𝐩𝐢𝐧𝐠 `{file_name}`..."),
                                call.message.chat.id, call.message.message_id,
                                reply_markup=create_reply_keyboard_main_menu(user_id))
    
    try:
        AnimationManager.animate_stop(call.message.chat.id, msg.message_id)
    except Exception:
        pass
    
    if script_key in bot_scripts:
        kill_process_tree(bot_scripts[script_key])
        if script_key in bot_scripts:
            del bot_scripts[script_key]
    
    recovery_system.remove_running_script(user_id, file_name)

def _restart_script_from_callback(call, user_id, file_name):
    """𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐬𝐜𝐫𝐢𝐩𝐭 𝐟𝐫𝐨𝐦 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    script_key = f"{user_id}_{file_name}"
    if is_bot_running(user_id, file_name):
        if script_key in bot_scripts:
            kill_process_tree(bot_scripts[script_key])
            if script_key in bot_scripts:
                del bot_scripts[script_key]
        time.sleep(1)
    
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    if not os.path.exists(file_path):
        bot.answer_callback_query(call.id, "❌ 𝐅𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝", show_alert=True)
        return
    
    file_type = 'py'
    for fname, ftype in user_files.get(user_id, []):
        if fname == file_name:
            file_type = ftype
            break
    
    msg = bot.edit_message_text(B(f"🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 `{file_name}`..."),
                                call.message.chat.id, call.message.message_id,
                                reply_markup=create_reply_keyboard_main_menu(user_id))
    
    try:
        AnimationManager.animate_restart(call.message.chat.id, msg.message_id)
    except Exception:
        pass
    
    if file_type == 'py':
        threading.Thread(target=run_script, args=(file_path, user_id, user_folder, file_name, msg)).start()
    elif file_type == 'js':
        threading.Thread(target=run_js_script, args=(file_path, user_id, user_folder, file_name, msg)).start()

def _delete_script_from_callback(call, user_id, file_name):
    """𝐃𝐞𝐥𝐞𝐭𝐞 𝐬𝐜𝐫𝐢𝐩𝐭 𝐟𝐫𝐨𝐦 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    bot.answer_callback_query(call.id, f"🗑️ 𝐃𝐞𝐥𝐞𝐭𝐢𝐧𝐠 {file_name}...")
    
    if is_bot_running(user_id, file_name):
        script_key = f"{user_id}_{file_name}"
        if script_key in bot_scripts:
            kill_process_tree(bot_scripts[script_key])
            if script_key in bot_scripts:
                del bot_scripts[script_key]
    
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    log_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
    
    if os.path.exists(file_path):
        os.remove(file_path)
    if os.path.exists(log_path):
        os.remove(log_path)
    remove_user_file_db(user_id, file_name)
    
    msg = bot.edit_message_text(B(f"🗑️ `{file_name}` 𝐝𝐞𝐥𝐞𝐭𝐞𝐝."),
                                call.message.chat.id, call.message.message_id,
                                reply_markup=create_reply_keyboard_main_menu(user_id))
    
    try:
        AnimationManager.animate_delete(call.message.chat.id, msg.message_id)
    except Exception:
        pass

def _show_logs_from_callback(call, user_id, file_name):
    """𝐒𝐡𝐨𝐰 𝐥𝐨𝐠𝐬 𝐟𝐫𝐨𝐦 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    user_folder = get_user_folder(user_id)
    log_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
    
    bot.answer_callback_query(call.id, f"📜 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 {file_name}...")
    
    msg = bot.edit_message_text(B(f"📜 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐥𝐨𝐠𝐬..."),
                                call.message.chat.id, call.message.message_id)
    
    try:
        AnimationManager.animate_logs(call.message.chat.id, msg.message_id)
    except Exception:
        pass
    
    if not os.path.exists(log_path):
        time.sleep(1)
        try:
            bot.edit_message_text(
                B(f"📭 𝐍𝐨 𝐥𝐨𝐠𝐬 𝐟𝐨𝐮𝐧𝐝 𝐟𝐨𝐫 `{file_name}`"),
                call.message.chat.id, msg.message_id, parse_mode='Markdown',
                reply_markup=create_reply_keyboard_main_menu(user_id)
            )
        except Exception:
            pass
        return
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            log_content = f.read()
        if len(log_content) > 3000:
            log_content = log_content[-3000:]
            log_content = "...\n" + log_content
        
        time.sleep(1)
        try:
            bot.edit_message_text(
                B(f"📜 𝐋𝐨𝐠𝐬 𝐟𝐨𝐫 `{file_name}`:\n```\n{log_content}\n```"),
                call.message.chat.id, msg.message_id, parse_mode='Markdown',
                reply_markup=create_reply_keyboard_main_menu(user_id)
            )
        except Exception:
            pass
    except Exception as e:
        bot.reply_to(call.message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫: {str(e)}"))

# ================================
# 𝐓𝐄𝐗𝐓 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐇𝐀𝐍𝐃𝐋𝐄𝐑𝐒 (𝐑𝐞𝐩𝐥𝐲 𝐊𝐞𝐲𝐛𝐨𝐚𝐫𝐝)
# ================================




@bot.message_handler(func=lambda message: message.text and (
    message.text == B("📤 𝐔𝐩𝐥𝐨𝐚𝐝") or
    message.text == B("📂 𝐌𝐚𝐧𝐚𝐠𝐞 𝐒𝐜𝐫𝐢𝐩𝐭𝐬") or
    message.text == B("⚡ 𝐒𝐩𝐞𝐞𝐝") or
    message.text == B("📊 𝐒𝐭𝐚𝐭𝐬") or
    message.text == B("👤 𝐏𝐫𝐨𝐟𝐢𝐥𝐞") or
    message.text == B("📦 𝐌𝐨𝐝𝐮𝐥𝐞") or
    message.text == B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫") or
    message.text == B("🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐁𝐨𝐭") or
    message.text == B("🗄️ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞")
))
def handle_main_menu_message(message):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐦𝐚𝐢𝐧 𝐦𝐞𝐧𝐮 𝐑𝐞𝐩𝐥𝐲 𝐊𝐞𝐲𝐛𝐨𝐚𝐫𝐝 𝐛𝐮𝐭𝐭𝐨𝐧 𝐩𝐫𝐞𝐬𝐬𝐞𝐬"""
    user_id = message.from_user.id
    add_active_user(user_id)
    text = message.text

    # ── 🗄️ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 ──
    if text == B("🗄️ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞"):
        if user_id not in admin_ids:
            bot.reply_to(message, B("🔒 𝐀𝐝𝐦𝐢𝐧/𝐨𝐰𝐧𝐞𝐫 𝐨𝐧𝐥𝐲."))
            return
        bot.reply_to(message, B("🗄️ 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 𝐌𝐀𝐍𝐀𝐆𝐄𝐑"), reply_markup=create_database_keyboard())

    # ── 📤 𝐔𝐩𝐥𝐨𝐚𝐝 ──
    elif text == B("📤 𝐔𝐩𝐥𝐨𝐚𝐝"):
        msg = bot.reply_to(message, B("📤 𝐒𝐞𝐧𝐝 𝐲𝐨𝐮𝐫 .𝐩𝐲 𝐨𝐫 .𝐣𝐬 𝐟𝐢𝐥𝐞 𝐧𝐨𝐰!\n\n📋 𝐒𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝: .𝐩𝐲, .𝐣𝐬, .𝐳𝐢𝐩"),
                           reply_markup=create_reply_keyboard_main_menu(user_id))

    # ── 📂 𝐌𝐚𝐧𝐚𝐠𝐞 𝐒𝐜𝐫𝐢𝐩𝐭𝐬 ──
    elif text == B("📂 𝐌𝐚𝐧𝐚𝐠𝐞 𝐒𝐜𝐫𝐢𝐩𝐭𝐬"):
        show_manage_scripts(message, user_id)

    # ── ⚡ 𝐒𝐩𝐞𝐞𝐝 ──
    elif text == B("⚡ 𝐒𝐩𝐞𝐞𝐝"):
        run_speedtest(message)

    # ── 📊 𝐒𝐭𝐚𝐭𝐬 ──
    elif text == B("📊 𝐒𝐭𝐚𝐭𝐬"):
        show_stats(message)

    # ── 👤 𝐏𝐫𝐨𝐟𝐢𝐥𝐞 ──
    elif text == B("👤 𝐏𝐫𝐨𝐟𝐢𝐥𝐞"):
        show_profile(message)

    # ── 📦 𝐌𝐨𝐝𝐮𝐥𝐞 ──
    elif text == B("📦 𝐌𝐨𝐝𝐮𝐥𝐞"):
        user_tier = get_user_tier(user_id)
        tier_info = TIER_SYSTEM[user_tier]
        module_text = f"""╔══════════════════════════════════╗
║    📦 𝐌𝐎𝐃𝐔𝐋𝐄 𝐌𝐀𝐍𝐀𝐆𝐄𝐑             ║
╚══════════════════════════════════╝

*𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝 𝐌𝐨𝐝𝐮𝐥𝐞𝐬:*
📦 𝐓𝐞𝐥𝐞𝐛𝐨𝐭, 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐬, 𝐏𝐬𝐮𝐭𝐢𝐥, 𝐅𝐥𝐚𝐬𝐤
📦 𝐐𝐫𝐜𝐨𝐝𝐞, 𝐏𝐢𝐥𝐥𝐨𝐰, 𝐂𝐫𝐲𝐩𝐭𝐨𝐠𝐫𝐚𝐩𝐡𝐲

*𝐔𝐩𝐥𝐨𝐚𝐝 𝐚 𝐬𝐜𝐫𝐢𝐩𝐭 𝐭𝐨 𝐚𝐮𝐭𝐨-𝐢𝐧𝐬𝐭𝐚𝐥𝐥 𝐝𝐞𝐩𝐞𝐧𝐝𝐞𝐧𝐜𝐢𝐞𝐬!*"""

        msg = bot.reply_to(message, module_text, parse_mode='Markdown',
                           reply_markup=create_reply_keyboard_main_menu(user_id))
        # 𝐑𝐮𝐧 𝐢𝐧𝐬𝐭𝐚𝐥𝐥 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
        try:
            AnimationManager.animate_install(message.chat.id, msg.message_id)
        except Exception:
            pass

    # ── 🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫 ──
    elif text == B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫"):
        msg = bot.reply_to(message, B("🛰 𝐈𝐧𝐢𝐭𝐢𝐚𝐭𝐢𝐧𝐠 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲..."))
        try:
            AnimationManager.animate_recovery(message.chat.id, msg.message_id)
        except Exception:
            pass
        time.sleep(2)
        recovered = recovery_system.recover_all_scripts()
        try:
            if recovered:
                bot.edit_message_text(
                    B(f"✅ 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞!\n🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐞𝐝: {len(recovered)} 𝐬𝐜𝐫𝐢𝐩𝐭(𝐬)"),
                    message.chat.id, msg.message_id,
                    reply_markup=create_reply_keyboard_main_menu(user_id))
            else:
                bot.edit_message_text(B("📭 𝐍𝐨 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫."),
                                     message.chat.id, msg.message_id,
                                     reply_markup=create_reply_keyboard_main_menu(user_id))
        except Exception:
            pass

    # ── 🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐁𝐨𝐭 ──
    elif text == B("🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐁𝐨𝐭"):
        if user_id != OWNER_ID:
            bot.reply_to(message, B("🔒 𝐎𝐰𝐧𝐞𝐫 𝐨𝐧𝐥𝐲."))
            return
        msg = bot.reply_to(message, B("🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐛𝐨𝐭..."))
        try:
            AnimationManager.animate_full_restart(message.chat.id, msg.message_id)
        except Exception:
            pass
        time.sleep(2.5)
        threading.Thread(target=send_restart_notification).start()
        os.execl(sys.executable, sys.executable, *sys.argv)




@bot.message_handler(func=lambda message: message.text and B("𝐓𝐡𝐢𝐬 𝐢𝐬 𝐩𝐫𝐢𝐯𝐚𝐭𝐞") in message.text)
def handle_private_message(message):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐩𝐫𝐢𝐯𝐚𝐭𝐞 𝐮𝐬𝐚𝐠𝐞 𝐧𝐨𝐭𝐢𝐜𝐞"""
    pass

# ================================
# 𝐑𝐄𝐏𝐋𝐘 𝐊𝐄𝐘𝐁𝐎𝐀𝐑𝐃 𝐂𝐎𝐍𝐓𝐑𝐎𝐋 𝐇𝐀𝐍𝐃𝐋𝐄𝐑
# ================================
@bot.message_handler(func=lambda message: message.text and (
    message.text.startswith(B("🔴 𝐒𝐭𝐨𝐩 ")) or
    message.text.startswith(B("🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 ")) or
    message.text.startswith(B("🗑️ 𝐃𝐞𝐥𝐞𝐭𝐞 ")) or
    message.text.startswith(B("📜 𝐋𝐨𝐠𝐬 ")) or
    message.text.startswith(B("📜 𝐕𝐢𝐞𝐰 𝐋𝐨𝐠𝐬 ")) or
    message.text.startswith(B("🟢 𝐒𝐭𝐚𝐫𝐭 "))
))
def handle_file_control_message(message):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐟𝐢𝐥𝐞 𝐜𝐨𝐧𝐭𝐫𝐨𝐥 𝐭𝐞𝐱𝐭 𝐛𝐮𝐭𝐭𝐨𝐧𝐬"""
    handle_file_control_text(message)

# ================================
# 𝐂𝐋𝐄𝐀𝐍𝐔𝐏 𝐀𝐍𝐃 𝐒𝐇𝐔𝐓𝐃𝐎𝐖𝐍
# ================================
def cleanup():
    """𝐂𝐥𝐞𝐚𝐧𝐮𝐩 𝐟𝐮𝐧𝐜𝐭𝐢𝐨𝐧 𝐟𝐨𝐫 𝐬𝐡𝐮𝐭𝐝𝐨𝐰𝐧"""
    logger.warning("🔴 𝐒𝐡𝐮𝐭𝐭𝐢𝐧𝐠 𝐝𝐨𝐰𝐧... 𝐂𝐥𝐞𝐚𝐧𝐢𝐧𝐠 𝐮𝐩 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐞𝐬")
    
    # 𝐊𝐢𝐥𝐥 𝐚𝐥𝐥 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭𝐬
    for script_key, script_info in list(bot_scripts.items()):
        try:
            kill_process_tree(script_info)
        except:
            pass
    
    logger.info("✅ 𝐂𝐥𝐞𝐚𝐧𝐮𝐩 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞")

# 𝐑𝐞𝐠𝐢𝐬𝐭𝐞𝐫 𝐜𝐥𝐞𝐚𝐧𝐮𝐩 𝐟𝐮𝐜𝐭𝐢𝐨𝐧
atexit.register(cleanup)

# ================================
# 𝐁𝐎𝐓 𝐒𝐓𝐀𝐑𝐓𝐔𝐏 𝐀𝐍𝐃 𝐀𝐔𝐓𝐎-𝐑𝐄𝐂𝐎𝐕𝐄𝐑𝐘
# ================================
def startup_recovery():
    """𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜𝐚𝐥𝐥𝐲 𝐫𝐞𝐜𝐨𝐯𝐞𝐫 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐨𝐧 𝐬𝐭𝐚𝐫𝐭𝐮𝐩"""
    logger.info("🚀 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐚𝐮𝐭𝐨-𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐩𝐫𝐨𝐜𝐞𝐬𝐬...")
    
    msg = None
    try:
        # 𝐒𝐞𝐧𝐝 𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐭𝐨 𝐨𝐰𝐧𝐞𝐫
        msg = bot.send_message(OWNER_ID, AnimationManager.animate_recovery.__doc__ or "🛰 𝐒𝐞𝐫𝐯𝐞𝐫 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲...")
        
        # 𝐒𝐞𝐧𝐝 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
        try:
            AnimationManager.animate_recovery(OWNER_ID, msg.message_id)
        except Exception:
            pass
        
        time.sleep(2)
        
        # 𝐑𝐞𝐜𝐨𝐯𝐞𝐫 𝐚𝐥𝐥 𝐬𝐜𝐫𝐢𝐩𝐭𝐬
        recovered = recovery_system.recover_all_scripts()
        
        if recovered:
            bot.edit_message_text(
                B(f"✅ 𝐒𝐭𝐚𝐫𝐭𝐮𝐩 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞!\n🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐞𝐝: {len(recovered)} 𝐬𝐜𝐫𝐢𝐩𝐭𝐬"),
                OWNER_ID, msg.message_id
            )
        else:
            bot.edit_message_text(
                B("📭 𝐍𝐨 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫 𝐨𝐧 𝐬𝐭𝐚𝐫𝐭𝐮𝐩."),
                OWNER_ID, msg.message_id
            )
        
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐢𝐧 𝐬𝐭𝐚𝐫𝐭𝐮𝐩 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲: {e}")
        if msg:
            try:
                bot.edit_message_text(
                    B(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐢𝐧 𝐬𝐭𝐚𝐫𝐭𝐮𝐩 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲: {str(e)[:100]}"),
                    OWNER_ID, msg.message_id
                )
            except:
                pass

# ================================
# 𝐂𝐀𝐋𝐋𝐁𝐀𝐂𝐊 𝐇𝐄𝐋𝐏𝐄𝐑𝐒
# ================================
def show_stats_callback(call, user_id):
    """𝐒𝐭𝐚𝐭𝐬 𝐟𝐫𝐨𝐦 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    bot.answer_callback_query(call.id, "📊 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐬𝐭𝐚𝐭𝐬...")
    
    user_tier = get_user_tier(user_id)
    tier_info = TIER_SYSTEM[user_tier]
    file_count = get_user_file_count(user_id)
    file_limit = get_user_file_limit(user_id)
    
    stats_text = f"""╔══════════════════════════════════╗
║    📊 𝐘𝐎𝐔𝐑 𝐒𝐓𝐀𝐓𝐒                ║
╚══════════════════════════════════╝

{tier_info['icon']} *𝐓𝐢𝐞𝐫: {tier_info['name']}*
📂 *𝐅𝐢𝐥𝐞𝐬:* {file_count}/{file_limit if file_limit != float('inf') else '∞'}
🚀 *𝐑𝐮𝐧𝐧𝐢𝐧𝐠:* {sum(1 for key, info in bot_scripts.items() if info['user_id'] == user_id)}"""
    
    msg = bot.edit_message_text(stats_text, call.message.chat.id, call.message.message_id, parse_mode='Markdown',
                                reply_markup=create_reply_keyboard_main_menu(user_id))
    try:
        AnimationManager.animate_dashboard(call.message.chat.id, msg.message_id)
    except Exception:
        pass

def show_profile_callback(call, user_id):
    """𝐏𝐫𝐨𝐟𝐢𝐥𝐞 𝐟𝐫𝐨𝐦 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    bot.answer_callback_query(call.id, "👤 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐩𝐫𝐨𝐟𝐢𝐥𝐞...")
    
    user_tier = get_user_tier(user_id)
    tier_info = TIER_SYSTEM[user_tier]
    
    profile_text = f"""╔══════════════════════════════════╗
║    👤 𝐘𝐎𝐔𝐑 𝐏𝐑𝐎𝐅𝐈𝐋𝐄              ║
╚══════════════════════════════════╝

👤 *𝐍𝐚𝐦𝐞:* {call.from_user.first_name}
🆔 *𝐔𝐬𝐞𝐫 𝐈𝐃:* {user_id}
@ *𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:* @{call.from_user.username or '𝐍𝐎𝐓 𝐒𝐄𝐓'}
{tier_info['icon']} *𝐓𝐢𝐞𝐫:* {tier_info['name']}"""
    
    bot.edit_message_text(profile_text, call.message.chat.id, call.message.message_id, parse_mode='Markdown',
                          reply_markup=create_reply_keyboard_main_menu(user_id))

def run_speedtest_callback(call, user_id):
    """Run the same real server-side speed test from the Speed callback."""
    bot.answer_callback_query(call.id, '⚡ 𝗦𝗣𝗘𝗘𝗗 𝗧𝗘𝗦𝗧 𝗦𝗧𝗔𝗥𝗧𝗘𝗗')
    threading.Thread(target=_run_real_speed_test, args=(call.message.chat.id, call.message.message_id, user_id), daemon=True).start()

# ================================
# 𝐌𝐀𝐈𝐍 𝐄𝐗𝐄𝐂𝐔𝐓𝐈𝐎𝐍
# ================================
if __name__ == '__main__':
    logger.info("="*50)
    logger.info("🚀 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐁𝐎𝐓 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 𝟒.𝟎")
    logger.info("🎨 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐀𝐍𝐈𝐌𝐀𝐓𝐄𝐃 𝐏𝐀𝐍𝐄𝐋")
    logger.info("📊 𝐀𝐮𝐭𝐨-𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐒𝐲𝐬𝐭𝐞𝐦 𝐄𝐧𝐚𝐛𝐥𝐞𝐝")
    logger.info("🤝 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐒𝐲𝐬𝐭𝐞𝐦 𝐄𝐧𝐚𝐛𝐥𝐞𝐝")
    logger.info("🏆 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝 𝐀𝐝𝐝𝐞𝐝")
    logger.info("🎫 𝐓𝐢𝐞𝐫-𝐁𝐚𝐬𝐞𝐝 𝐇𝐨𝐬𝐭𝐢𝐧𝐠")
    logger.info(f"👑 𝐎𝐰𝐧𝐞𝐫 𝐈𝐃: {OWNER_ID}")
    logger.info(f"🛡️ 𝐀𝐝𝐦𝐢𝐧𝐬: 1")
    logger.info(f"👥 𝐀𝐜𝐭𝐢𝐯𝐞 𝐔𝐬𝐞𝐫𝐬: {len(active_users)}")
    logger.info(f"📁 𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬: {sum(len(files) for files in user_files.values())}")
    
    # 𝐆𝐞𝐭 𝐛𝐨𝐭 𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞
    try:
        bot_username = bot.get_me().username
        logger.info(f"🤖 𝐁𝐨𝐭 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: @{bot_username}")
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐠𝐞𝐭𝐭𝐢𝐧𝐠 𝐛𝐨𝐭 𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {e}")
    
    logger.info("="*50)
    
    # 𝐒𝐭𝐚𝐫𝐭 𝐅𝐥𝐚𝐬𝐤 𝐤𝐞𝐞𝐩-𝐚𝐥𝐢𝐯𝐞
    keep_alive()
    
    # 𝐑𝐮𝐧 𝐬𝐭𝐚𝐫𝐭𝐮𝐩 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲
    threading.Thread(target=startup_recovery).start()
    
    # 𝐒𝐭𝐚𝐫𝐭 𝐛𝐨𝐭 𝐩𝐨𝐥𝐥𝐢𝐧𝐠
    logger.info("🤖 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐛𝐨𝐭 𝐩𝐨𝐥𝐥𝐢𝐧𝐠...")
    
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=30)
        except requests.exceptions.ReadTimeout:
            logger.warning("⚠️ 𝐑𝐞𝐚𝐝 𝐓𝐢𝐦𝐞𝐨𝐮𝐭. 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐢𝐧 𝟓𝐬...")
            time.sleep(5)
        except requests.exceptions.ConnectionError as ce:
            logger.error(f"⚠️ 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧 𝐄𝐫𝐫𝐨𝐫: {ce}. 𝐑𝐞𝐭𝐫𝐲𝐢𝐧𝐠 𝐢𝐧 𝟏𝟓𝐬...")
            time.sleep(15)
        except Exception as e:
            logger.critical(f"💥 𝐔𝐧𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐚𝐛𝐥𝐞 𝐞𝐫𝐫𝐨𝐫: {e}", exc_info=True)
            logger.info("🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐢𝐧 𝟑𝟎𝐬 𝐝𝐮𝐞 𝐭𝐨 𝐜𝐫𝐢𝐭𝐢𝐜𝐚𝐥 𝐞𝐫𝐫𝐨𝐫...")
            time.sleep(30)
        finally:
            logger.warning("🔴 𝐏𝐨𝐥𝐥𝐢𝐧𝐠 𝐬𝐭𝐨𝐩𝐩𝐞𝐝. 𝐖𝐢𝐥𝐥 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐢𝐟 𝐢𝐧 𝐥𝐨𝐨𝐩...")
            time.sleep(1)
