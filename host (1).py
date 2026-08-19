"""
𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐁𝐎𝐓 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 𝟓.𝟎 — 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐏𝐀𝐍𝐄𝐋
𝐂𝐘𝐁𝐄𝐑𝐏𝐔𝐍𝐊 + 𝐇𝐀𝐂𝐊𝐄𝐑 𝐓𝐄𝐑𝐌𝐈𝐍𝐀𝐋 + 𝐒𝐄𝐑𝐕𝐄𝐑 𝐑𝐀𝐂𝐊 𝐔𝐈
𝐀𝐒𝐘𝐍𝐂 + 𝐇𝐓𝐓𝐏𝐗 + 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐋𝐎𝐆𝐆𝐈𝐍𝐆
𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄: 𝐌𝐀𝐓𝐇𝐄𝐌𝐀𝐓𝐈𝐂𝐀𝐋 𝐁𝐎𝐋𝐃 𝐒𝐀𝐍𝐒-𝐒𝐄𝐑𝐈𝐅
"""

import subprocess
import sys
import os

# Dependencies are installed during deployment from requirements.txt.
# Runtime package installation is intentionally disabled for reliable Railway starts.
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
import asyncio
import httpx
import aiofiles
import anyio
from logging.handlers import RotatingFileHandler
from concurrent.futures import ThreadPoolExecutor
import traceback

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
TOKEN = os.environ.get('BOT_TOKEN')
try:
    OWNER_ID = int(os.environ['OWNER_ID'])
except (KeyError, ValueError):
    OWNER_ID = 0
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
LOGS_DIR = os.path.join(HOSTING_DATA_DIR, 'logs')
BOT_LOG_PATH = os.path.join(LOGS_DIR, 'bot.log')
SYSTEM_LOG_PATH = os.path.join(LOGS_DIR, 'system.log')
ERROR_LOG_PATH = os.path.join(LOGS_DIR, 'error.log')
SCRIPTS_LOG_DIR = os.path.join(LOGS_DIR, 'scripts')

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
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(SCRIPTS_LOG_DIR, exist_ok=True)

# ================================
# 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐋𝐎𝐆𝐆𝐈𝐍𝐆 𝐒𝐘𝐒𝐓𝐄𝐌
# ================================
def setup_logging():
    """Setup advanced logging with rotation"""
    # Bot logs
    bot_logger = logging.getLogger('bot')
    bot_logger.setLevel(logging.INFO)
    bot_handler = RotatingFileHandler(BOT_LOG_PATH, maxBytes=10*1024*1024, backupCount=5)
    bot_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    bot_logger.addHandler(bot_handler)
    
    # System logs
    system_logger = logging.getLogger('system')
    system_logger.setLevel(logging.INFO)
    system_handler = RotatingFileHandler(SYSTEM_LOG_PATH, maxBytes=10*1024*1024, backupCount=5)
    system_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    system_logger.addHandler(system_handler)
    
    # Error logs
    error_logger = logging.getLogger('error')
    error_logger.setLevel(logging.ERROR)
    error_handler = RotatingFileHandler(ERROR_LOG_PATH, maxBytes=10*1024*1024, backupCount=5)
    error_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    error_logger.addHandler(error_handler)
    
    # Root logger for console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(console_handler)
    
    return bot_logger, system_logger, error_logger

bot_logger, system_logger, error_logger = setup_logging()

# ================================
# 𝐀𝐒𝐘𝐍𝐂 𝐇𝐓𝐓𝐏𝐗 𝐂𝐋𝐈𝐄𝐍𝐓
# ================================
class HTTPXClientManager:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._client = None
        self._loop = None
        self._tasks = []
        self._semaphore = asyncio.Semaphore(20)  # MAX_CONCURRENT_REQUESTS
        self._executor = ThreadPoolExecutor(max_workers=10)
        self._lock = asyncio.Lock()
        self._closed = False
        
    def _ensure_loop(self):
        """Ensure we have an event loop"""
        if self._loop is None or self._loop.is_closed():
            try:
                self._loop = asyncio.get_running_loop()
            except RuntimeError:
                self._loop = asyncio.new_event_loop()
                asyncio.set_event_loop(self._loop)
        return self._loop
    
    async def _get_client(self):
        """Get or create HTTPX AsyncClient with connection pooling"""
        if self._closed:
            raise RuntimeError("HTTPX client is closed")
            
        if self._client is None:
            timeout = httpx.Timeout(30.0, connect=10.0)
            limits = httpx.Limits(max_keepalive_connections=20, max_connections=50)
            self._client = httpx.AsyncClient(
                timeout=timeout,
                limits=limits,
                http2=True,
                follow_redirects=True,
                headers={'User-Agent': 'HostingBot/5.0'}
            )
            bot_logger.info("✅ HTTPX AsyncClient created with connection pooling")
        
        return self._client
    
    async def request(self, method, url, **kwargs):
        """Make async HTTP request with retries and logging"""
        if self._closed:
            raise RuntimeError("HTTPX client is closed")
        
        async with self._semaphore:
            client = await self._get_client()
            max_retries = 3
            retry_count = 0
            backoff = 1.0
            
            # Sanitize URL for logging
            safe_url = url.split('?')[0] if '?' in url else url
            safe_url = safe_url[:100]  # Truncate for safety
            
            while retry_count <= max_retries:
                try:
                    start_time = time.time()
                    response = await client.request(method, url, **kwargs)
                    duration = time.time() - start_time
                    
                    # Log the request
                    status_emoji = "🟢" if response.status_code < 400 else "🟡" if response.status_code < 500 else "🔴"
                    bot_logger.info(f"🌐 {method} {safe_url} | ⏱️ {duration:.2f}s | {status_emoji} {response.status_code}")
                    
                    if response.status_code >= 500 and retry_count < max_retries:
                        retry_count += 1
                        bot_logger.warning(f"⚠️ Retry {retry_count}/{max_retries} for {safe_url} (status {response.status_code})")
                        await asyncio.sleep(backoff)
                        backoff *= 2
                        continue
                    
                    return response
                    
                except (httpx.TimeoutException, httpx.ConnectError, httpx.ConnectTimeout) as e:
                    if retry_count < max_retries:
                        retry_count += 1
                        bot_logger.warning(f"⚠️ Retry {retry_count}/{max_retries} for {safe_url}: {str(e)[:100]}")
                        await asyncio.sleep(backoff)
                        backoff *= 2
                    else:
                        error_logger.error(f"❌ Request failed after {max_retries} retries: {url} - {str(e)}")
                        raise
                
                except Exception as e:
                    error_logger.exception(f"❌ Request error for {safe_url}: {str(e)}")
                    raise
            
            raise RuntimeError(f"Max retries exceeded for {url}")
    
    async def get(self, url, **kwargs):
        return await self.request('GET', url, **kwargs)
    
    async def post(self, url, **kwargs):
        return await self.request('POST', url, **kwargs)
    
    async def close(self):
        """Close the HTTPX client and cleanup"""
        if self._closed:
            return
        
        self._closed = True
        
        # Cancel all pending tasks
        for task in self._tasks:
            if not task.done():
                task.cancel()
        
        if self._tasks:
            await asyncio.gather(*self._tasks, return_exceptions=True)
        
        if self._client:
            await self._client.aclose()
            bot_logger.info("✅ HTTPX AsyncClient closed")
        
        self._executor.shutdown(wait=False)
    
    def run_async(self, coro):
        """Run async coroutine from sync context"""
        loop = self._ensure_loop()
        task = asyncio.run_coroutine_threadsafe(coro, loop)
        self._tasks.append(task)
        return task.result() if not task.done() else None

# Global HTTPX client manager
http_client = HTTPXClientManager()

# ================================
# 𝐀𝐒𝐘𝐍𝐂 𝐖𝐎𝐑𝐊𝐄𝐑 𝐌𝐀𝐍𝐀𝐆𝐄𝐑
# ================================
class AsyncWorkerManager:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._loop = None
        self._tasks = {}
        self._running = True
        self._live_logs = {}  # user_id: (script_name, task)
        self._task_locks = {}
        self._executor = ThreadPoolExecutor(max_workers=10)
    
    def _ensure_loop(self):
        """Ensure we have an event loop"""
        if self._loop is None or self._loop.is_closed():
            try:
                self._loop = asyncio.get_running_loop()
            except RuntimeError:
                self._loop = asyncio.new_event_loop()
                asyncio.set_event_loop(self._loop)
        return self._loop
    
    def run_async(self, coro, task_name=None):
        """Run async coroutine from sync context"""
        loop = self._ensure_loop()
        task = asyncio.run_coroutine_threadsafe(coro, loop)
        if task_name:
            self._tasks[task_name] = task
        return task
    
    def cancel_task(self, task_name):
        """Cancel a specific task"""
        if task_name in self._tasks:
            task = self._tasks[task_name]
            if not task.done():
                task.cancel()
                del self._tasks[task_name]
                return True
        return False
    
    async def _run_async_worker(self):
        """Main async worker loop"""
        while self._running:
            await asyncio.sleep(1)
            # Cleanup completed tasks
            completed = [name for name, task in self._tasks.items() if task.done()]
            for name in completed:
                del self._tasks[name]
    
    def start_worker(self):
        """Start the async worker"""
        loop = self._ensure_loop()
        task = loop.create_task(self._run_async_worker())
        self._tasks['_worker'] = task
    
    def stop_worker(self):
        """Stop the async worker"""
        self._running = False
        for name, task in list(self._tasks.items()):
            if not task.done():
                task.cancel()
        self._tasks.clear()
        self._executor.shutdown(wait=False)

# Global async worker manager
worker_manager = AsyncWorkerManager()

# ================================
# 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐌𝐎𝐃𝐔𝐋𝐄 𝐌𝐀𝐍𝐀𝐆𝐄𝐑
# ================================
TELEGRAM_MODULES = {
    'telebot': 'pyTelegramBotAPI',
    'telegram': 'python-telegram-bot',
    'aiogram': 'aiogram',
    'pyrogram': 'pyrogram',
    'telethon': 'telethon',
    'httpx': 'httpx',
    'aiofiles': 'aiofiles',
    'anyio': 'anyio',
    'requests': 'requests',
    'flask': 'flask',
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
    'asyncio': '', 'json': '', 'os': '', 'sys': '', 'time': '', 're': '',
    'math': '', 'random': '', 'datetime': '', 'collections': '', 'itertools': '',
    'functools': '', 'pathlib': '', 'subprocess': '', 'threading': '', 'logging': '',
    'io': '', 'hashlib': '', 'base64': '', 'urllib': '', 'http': '', 'socket': '',
    'signal': '', 'string': '', 'typing': '', 'dataclasses': '', 'enum': '',
    'abc': '', 'copy': '', 'pickle': '', 'struct': '', 'gzip': '', 'tarfile': '',
    'shutil': '', 'tempfile': '', 'glob': '', 'fnmatch': '', 'sqlite3': '',
    'csv': '', 'xml': '', 'html': '', 'email': '', 'smtplib': '', 'ssl': '',
    'jwt': 'PyJWT', 'PIL': 'Pillow', 'cv2': 'opencv-python',
    'sklearn': 'scikit-learn', 'skimage': 'scikit-image', 'scipy': 'scipy',
    'matplotlib': 'matplotlib', 'seaborn': 'seaborn', 'plotly': 'plotly',
    'selenium': 'selenium', 'beautifulsoup': 'beautifulsoup4', 'lxml': 'lxml',
    'pydantic': 'pydantic', 'fastapi': 'fastapi', 'uvicorn': 'uvicorn',
    'starlette': 'starlette', 'jinja2': 'jinja2', 'werkzeug': 'werkzeug',
    'click': 'click', 'celery': 'celery', 'kombu': 'kombu', 'boto3': 'boto3',
    'botocore': 'botocore', 'stripe': 'stripe', 'decouple': 'python-decouple',
    'schedule': 'schedule', 'apscheduler': 'APScheduler', 'pytz': 'pytz',
    'pycountry': 'pycountry', 'phonenumbers': 'phonenumbers'
}

def scan_required_modules(file_path):
    """Scan a .py file's imports for missing modules"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        imports = set(re.findall(r'^\s*import\s+([a-zA-Z0-9_\.]+)', content, re.MULTILINE))
        imports |= set(re.findall(r'^\s*from\s+([a-zA-Z0-9_\.]+)\s+import', content, re.MULTILINE))
        
        top_level = sorted(set(i.split('.')[0] for i in imports))
        stdlib = set(getattr(sys, 'stdlib_module_names', []))
        
        missing = []
        for mod in top_level:
            if mod in stdlib or mod.startswith('_'):
                continue
            try:
                __import__(mod)
            except ImportError:
                pip_name = TELEGRAM_MODULES.get(mod.lower(), mod)
                if pip_name:
                    missing.append(pip_name)
        
        return sorted(set(missing))
    except Exception as e:
        error_logger.error(f"Error scanning modules: {e}")
        return []

def install_module(package_name, message=None):
    """Install a Python package"""
    try:
        if message:
            bot.reply_to(message, f"🐍 Installing {package_name}...")
        
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'install', package_name],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            if message:
                bot.reply_to(message, f"✅ Installed {package_name}")
            bot_logger.info(f"✅ Installed package: {package_name}")
            return True
        else:
            error_logger.error(f"Failed to install {package_name}: {result.stderr[:200]}")
            if message:
                bot.reply_to(message, f"❌ Failed to install {package_name}: {result.stderr[:100]}")
            return False
    except Exception as e:
        error_logger.error(f"Error installing {package_name}: {e}")
        if message:
            bot.reply_to(message, f"❌ Error installing {package_name}: {str(e)[:100]}")
        return False

def install_missing_modules(file_path, message=None):
    """Install missing modules for a Python script"""
    missing = scan_required_modules(file_path)
    
    if not missing:
        if message:
            bot.reply_to(message, "✅ All modules are installed")
        return True
    
    if message:
        bot.reply_to(message, f"📦 Installing {len(missing)} missing modules...")
    
    success = True
    for package in missing:
        if not install_module(package, message):
            success = False
    
    return success

# ================================
# 𝐈𝐍𝐈𝐓𝐈𝐀𝐋𝐈𝐙𝐄 𝐁𝐎𝐓
# ================================
bot = telebot.TeleBot(TOKEN, use_class_middlewares=True)

# ================================
# 𝐃𝐀𝐓𝐀 𝐒𝐓𝐑𝐔𝐂𝐓𝐔𝐑𝐄𝐒
# ================================
bot_scripts = {}
_script_locks = {}
_script_locks_guard = threading.RLock()
_state_file_lock = threading.RLock()
_reset_confirmations = {}
user_files = {}
active_users = set()
admin_ids = {OWNER_ID}
user_subscriptions = {}
bot_locked = False
pending_module_installs = {}

# ================================
# 𝐅𝐎𝐍𝐓 𝐂𝐎𝐍𝐕𝐄𝐑𝐒𝐈𝐎𝐍
# ================================
def convert_to_bold_uppercase(text: str) -> str:
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

B = convert_to_bold_uppercase

def unbold(text: str) -> str:
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
# 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍 𝐌𝐀𝐍𝐀𝐆𝐄𝐑
# ================================
_animation_locks = {}
_animation_lock_global = threading.Lock()

def _get_animation_lock(chat_id, message_id):
    key = f"{chat_id}_{message_id}"
    with _animation_lock_global:
        if key not in _animation_locks:
            _animation_locks[key] = threading.Lock()
        return _animation_locks[key]

def run_edit_animation(chat_id, message_id, frames, delay=0.3):
    lock = _get_animation_lock(chat_id, message_id)
    if not lock.acquire(blocking=False):
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
            key = f"{chat_id}_{message_id}"
            with _animation_lock_global:
                if key in _animation_locks:
                    del _animation_locks[key]

    t = threading.Thread(target=_do_animation, daemon=True)
    t.start()
    return t

def _live_animation(chat_id, message_id, frames):
    return run_edit_animation(chat_id, message_id, frames, delay=0.45)

class AnimationManager:
    @staticmethod
    def animate_upload(chat_id, message_id):
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
║    ✅ 𝐔𝐏𝐋𝐎𝐀𝐃 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄              ║
╠══════════════════════════════════╣
║  🎉 𝐅𝐢𝐥𝐞 𝐫𝐞𝐚𝐝𝐲 𝐟𝐨𝐫 𝐡𝐨𝐬𝐭𝐢𝐧𝐠!       ║
╚══════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━
□□□□□□□□🚀□□
[▰▰▰▰▰▰▰▰▰▰] 100%"""
        ]
        _live_animation(chat_id, message_id, frames)

    @staticmethod
    def animate_start(chat_id, message_id):
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
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐋𝐀𝐔𝐍𝐂𝐇𝐈𝐍𝐆                ║
╚══════════════════════════════════╝

> 𝐋𝐚𝐮𝐧𝐜𝐡𝐢𝐧𝐠 𝐚𝐩𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐨𝐧...
[▰▰▰▰▰▰▰▰▰▰] 100%

━━━━━━━━━━━━━━━━━━━━━━
🟢 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐎𝐍𝐋𝐈𝐍𝐄"""
        ]
        _live_animation(chat_id, message_id, frames)

    @staticmethod
    def animate_stop(chat_id, message_id):
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
        _live_animation(chat_id, message_id, frames)

    @staticmethod
    def animate_restart(chat_id, message_id):
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
        _live_animation(chat_id, message_id, frames)

    @staticmethod
    def animate_delete(chat_id, message_id):
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
        _live_animation(chat_id, message_id, frames)

    @staticmethod
    def animate_logs(chat_id, message_id):
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
        _live_animation(chat_id, message_id, frames)

    @staticmethod
    def animate_recovery(chat_id, message_id):
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
        _live_animation(chat_id, message_id, frames)

    @staticmethod
    def animate_full_restart(chat_id, message_id):
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
        _live_animation(chat_id, message_id, frames)

    @staticmethod
    def animate_full_reset(chat_id, message_id):
        frames = [
            f"""╔══════════════════════════════════╗
║  🧹 𝐅𝐔𝐋𝐋 𝐑𝐄𝐒𝐄𝐓                    ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐒𝐓𝐎𝐏𝐏𝐈𝐍𝐆                ║
╚══════════════════════════════════╝

🛑 𝐒𝐭𝐨𝐩𝐩𝐢𝐧𝐠 𝐩𝐫𝐨𝐜𝐞𝐬𝐬...""",
            f"""╔══════════════════════════════════╗
║  🧹 𝐅𝐔𝐋𝐋 𝐑𝐄𝐒𝐄𝐓                    ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐂𝐋𝐄𝐀𝐍𝐈𝐍𝐆                ║
╚══════════════════════════════════╝

🧹 𝐂𝐥𝐞𝐚𝐧𝐢𝐧𝐠 𝐰𝐨𝐫𝐤𝐞𝐫𝐬...""",
            f"""╔══════════════════════════════════╗
║  🧹 𝐅𝐔𝐋𝐋 𝐑𝐄𝐒𝐄𝐓                    ║
╠══════════════════════════════════╣
║  𝐒𝐭𝐚𝐭𝐮𝐬: 𝐂𝐋𝐄𝐀𝐑𝐈𝐍𝐆                ║
╚══════════════════════════════════╝

📜 𝐂𝐥𝐞𝐚𝐫𝐢𝐧𝐠 𝐥𝐨𝐠𝐬...""",
            f"""╔══════════════════════════════════╗
║  ✅ 𝐑𝐄𝐒𝐄𝐓 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄              ║
╚══════════════════════════════════╝

🧹 𝐑𝐞𝐬𝐞𝐭 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲
━━━━━━━━━━━━━━━━━━━━━━"""
        ]
        _live_animation(chat_id, message_id, frames)

    @staticmethod
    def animate_install(chat_id, message_id):
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
║  ✅ 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐀𝐓𝐈𝐎𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄        ║
╚══════════════════════════════════╝

🟢 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲
━━━━━━━━━━━━━━━━━━━━━━
[▰▰▰▰▰▰▰▰▰▰] 100%"""
        ]
        _live_animation(chat_id, message_id, frames)

    @staticmethod
    def show_dashboard(total_files, running_count, ram_pct, cpu_pct, total_users):
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
# 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 𝐎𝐏𝐄𝐑𝐀𝐓𝐈𝐎𝐍𝐒
# ================================
def init_db():
    try:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
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
        bot_logger.info("✅ Database initialized successfully")
    except Exception as e:
        error_logger.exception(f"Database initialization error: {e}")

def load_data():
    try:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT user_id, file_name, file_type FROM user_files')
        for user_id, file_name, file_type in c.fetchall():
            if user_id not in user_files:
                user_files[user_id] = []
            user_files[user_id].append((file_name, file_type))
        c.execute('SELECT user_id FROM active_users')
        active_users.update(user_id for (user_id,) in c.fetchall())
        conn.close()
        bot_logger.info(f"✅ Data loaded: {len(active_users)} users, {sum(len(files) for files in user_files.values())} files")
    except Exception as e:
        error_logger.exception(f"Error loading data: {e}")

def add_active_user(user_id, username=None):
    try:
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
    except Exception as e:
        error_logger.error(f"Error adding active user {user_id}: {e}")

def save_user_file_db(user_id, file_name, file_type):
    try:
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
    except Exception as e:
        error_logger.error(f"Error saving user file {user_id}/{file_name}: {e}")

def remove_user_file_db(user_id, file_name):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        c = conn.cursor()
        c.execute('DELETE FROM user_files WHERE user_id = ? AND file_name = ?', (user_id, file_name))
        conn.commit()
        conn.close()
        if user_id in user_files:
            user_files[user_id] = [(fname, ftype) for fname, ftype in user_files[user_id] if fname != file_name]
        recovery_system.remove_running_script(user_id, file_name)
    except Exception as e:
        error_logger.error(f"Error removing user file {user_id}/{file_name}: {e}")

# ================================
# 𝐇𝐄𝐋𝐏𝐄𝐑 𝐅𝐔𝐍𝐂𝐓𝐈𝐎𝐍𝐒
# ================================
def get_user_folder(user_id):
    user_folder = os.path.join(UPLOAD_BOTS_DIR, str(user_id))
    os.makedirs(user_folder, exist_ok=True)
    return user_folder

def get_user_tier(user_id):
    return "full"

def get_user_file_limit(user_id):
    tier = get_user_tier(user_id)
    return TIER_SYSTEM[tier]["upload_limit"]

def get_user_file_count(user_id):
    return len(user_files.get(user_id, []))

def get_script_log_path(user_id, file_name):
    """Get the log file path for a script"""
    safe_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', file_name)
    return os.path.join(SCRIPTS_LOG_DIR, f"{user_id}_{safe_name}.log")

def get_script_log_lines(user_id, file_name, limit=50, offset=0):
    """Get lines from a script log file with pagination"""
    log_path = get_script_log_path(user_id, file_name)
    if not os.path.exists(log_path):
        return [], 0
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        total = len(lines)
        start = max(0, total - limit - offset)
        end = total - offset
        return lines[start:end], total
    except Exception as e:
        error_logger.error(f"Error reading log {log_path}: {e}")
        return [], 0

def get_log_statistics():
    """Get log statistics"""
    stats = {
        'total_files': 0,
        'total_size': 0,
        'error_count': 0,
        'last_event': None
    }
    
    try:
        # Count log files
        for root, dirs, files in os.walk(LOGS_DIR):
            for file in files:
                if file.endswith('.log'):
                    stats['total_files'] += 1
                    path = os.path.join(root, file)
                    stats['total_size'] += os.path.getsize(path)
                    mtime = os.path.getmtime(path)
                    if stats['last_event'] is None or mtime > stats['last_event']:
                        stats['last_event'] = mtime
        
        # Count errors in error log
        if os.path.exists(ERROR_LOG_PATH):
            try:
                with open(ERROR_LOG_PATH, 'r', encoding='utf-8', errors='ignore') as f:
                    stats['error_count'] = sum(1 for _ in f)
            except:
                pass
        
        if stats['last_event']:
            stats['last_event'] = datetime.fromtimestamp(stats['last_event']).strftime('%H:%M:%S')
        else:
            stats['last_event'] = 'N/A'
            
        stats['total_size_mb'] = stats['total_size'] / (1024 * 1024)
        
    except Exception as e:
        error_logger.error(f"Error getting log statistics: {e}")
    
    return stats

def write_script_log(user_id, file_name, message, level='INFO'):
    """Write a message to a script's log file with timestamp"""
    log_path = get_script_log_path(user_id, file_name)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] [{level}] {message}\n"
    
    try:
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(log_entry)
    except Exception as e:
        error_logger.error(f"Error writing script log {log_path}: {e}")

def sanitize_log_text(text):
    """Sanitize log text by removing sensitive information"""
    # Remove tokens
    text = re.sub(r'token[=:]\S+', 'TOKEN_REDACTED', text, flags=re.I)
    text = re.sub(r'api[_-]key[=:]\S+', 'API_KEY_REDACTED', text, flags=re.I)
    text = re.sub(r'password[=:]\S+', 'PASSWORD_REDACTED', text, flags=re.I)
    text = re.sub(r'secret[=:]\S+', 'SECRET_REDACTED', text, flags=re.I)
    
    # Remove environment variable patterns
    text = re.sub(r'\${?[A-Z_]+}?', 'ENV_VAR_REDACTED', text)
    
    return text

# ================================
# 𝐀𝐔𝐓𝐎-𝐑𝐄𝐂𝐎𝐕𝐄𝐑𝐘 𝐒𝐘𝐒𝐓𝐄𝐌
# ================================
class AutoRecoverySystem:
    def __init__(self):
        self.running_scripts_file = RUNNING_SCRIPTS_DB
        
    def save_running_script(self, user_id: int, file_name: str, file_path: str, process_pid: int):
        try:
            if os.path.exists(self.running_scripts_file):
                with open(self.running_scripts_file, 'r') as f:
                    data = json.load(f)
            else:
                data = {"running_scripts": []}
            
            data["running_scripts"] = [script for script in data["running_scripts"] 
                                     if not (script["user_id"] == user_id and script["file_name"] == file_name)]
            
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
                
            system_logger.info(f"💾 Saved running script: {user_id}/{file_name} (PID: {process_pid})")
            
        except Exception as e:
            error_logger.error(f"Error saving running script: {e}")
    
    def remove_running_script(self, user_id: int, file_name: str):
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
                    system_logger.info(f"🗑️ Removed running script: {user_id}/{file_name}")
                    
        except Exception as e:
            error_logger.error(f"Error removing running script: {e}")
    
    def recover_all_scripts(self):
        try:
            if not os.path.exists(self.running_scripts_file):
                system_logger.info("📭 No running scripts to recover")
                return []
            
            with open(self.running_scripts_file, 'r') as f:
                data = json.load(f)
            
            recovered = []
            for script in data.get("running_scripts", []):
                try:
                    user_id = script["user_id"]
                    file_name = script["file_name"]
                    file_path = script["file_path"]
                    
                    if is_bot_running(user_id, file_name):
                        system_logger.info(f"Skipping duplicate recovery for {user_id}/{file_name}")
                        continue

                    if not os.path.exists(file_path):
                        system_logger.warning(f"⚠️ File not found for recovery: {file_path}")
                        continue
                    
                    user_has_file = False
                    for fname, ftype in user_files.get(user_id, []):
                        if fname == file_name:
                            user_has_file = True
                            break
                    
                    if not user_has_file:
                        system_logger.warning(f"⚠️ User {user_id} no longer has file: {file_name}")
                        continue
                    
                    tier = get_user_tier(user_id)
                    auto_restart_enabled = TIER_SYSTEM[tier]['auto_restart']
                    
                    if not auto_restart_enabled:
                        system_logger.info(f"⏸️ Auto-restart disabled for user {user_id}")
                        continue
                    
                    user_folder = get_user_folder(user_id)
                    file_ext = os.path.splitext(file_name)[1].lower()
                    
                    write_script_log(user_id, file_name, "🛰️ Auto Recovery: Restarting script", "SYSTEM")
                    
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
                    
                    system_logger.info(f"🔄 Recovering script: {user_id}/{file_name}")
                    
                    time.sleep(1)
                    
                except Exception as e:
                    error_logger.error(f"Error recovering script {script}: {e}")
            
            return recovered
            
        except Exception as e:
            error_logger.error(f"Error in recovery system: {e}")
            return []
    
    def _restart_py_script(self, user_id: int, file_path: str, user_folder: str, file_name: str):
        try:
            script_key = f"{user_id}_{file_name}"
            if script_key in bot_scripts:
                system_logger.info(f"✅ Script already running: {file_name}")
                return
            
            write_script_log(user_id, file_name, "🔄 Auto Recovery: Starting recovered script", "SYSTEM")
            
            log_file_path = get_script_log_path(user_id, file_name)
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
            
            self.save_running_script(user_id, file_name, file_path, process.pid)
            write_script_log(user_id, file_name, f"✅ Auto Recovery successful (PID: {process.pid})", "SYSTEM")
            system_logger.info(f"✅ Recovered Python script: {file_name} (PID: {process.pid})")
            
        except Exception as e:
            error_logger.error(f"Error restarting Python script {file_name}: {e}")
    
    def _restart_js_script(self, user_id: int, file_path: str, user_folder: str, file_name: str):
        try:
            script_key = f"{user_id}_{file_name}"
            if script_key in bot_scripts:
                system_logger.info(f"✅ Script already running: {file_name}")
                return
            
            write_script_log(user_id, file_name, "🔄 Auto Recovery: Starting recovered script", "SYSTEM")
            
            log_file_path = get_script_log_path(user_id, file_name)
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
            
            self.save_running_script(user_id, file_name, file_path, process.pid)
            write_script_log(user_id, file_name, f"✅ Auto Recovery successful (PID: {process.pid})", "SYSTEM")
            system_logger.info(f"✅ Recovered JS script: {file_name} (PID: {process.pid})")
            
        except Exception as e:
            error_logger.error(f"Error restarting JS script {file_name}: {e}")
    
    def get_running_count(self):
        try:
            if os.path.exists(self.running_scripts_file):
                with open(self.running_scripts_file, 'r') as f:
                    data = json.load(f)
                return len(data.get("running_scripts", []))
            return 0
        except:
            return 0

recovery_system = AutoRecoverySystem()

# ================================
# 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐌𝐀𝐍𝐀𝐆𝐄𝐌𝐄𝐍𝐓
# ================================
def is_bot_running(user_id, file_name):
    script_key = f"{user_id}_{file_name}"
    script_info = bot_scripts.get(script_key)
    
    if script_info and script_info.get('process'):
        try:
            proc = psutil.Process(script_info['process'].pid)
            return proc.is_running() and proc.status() != psutil.STATUS_ZOMBIE
        except psutil.NoSuchProcess:
            recovery_system.remove_running_script(user_id, file_name)
            if script_key in bot_scripts:
                del bot_scripts[script_key]
            return False
    return False

def kill_process_tree(process_info):
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
                
                if 'user_id' in process_info and 'file_name' in process_info:
                    recovery_system.remove_running_script(
                        process_info['user_id'], 
                        process_info['file_name']
                    )
                    write_script_log(
                        process_info['user_id'], 
                        process_info['file_name'], 
                        f"🛑 Process terminated (PID: {pid})", 
                        "SYSTEM"
                    )
                
            except psutil.NoSuchProcess:
                pass
                
    except Exception as e:
        error_logger.error(f"Error killing process: {e}")

def _script_lock(script_key):
    with _script_locks_guard:
        return _script_locks.setdefault(script_key, threading.RLock())

def _cleanup_script_runtime(user_id, file_name, clear_log=False):
    key = f"{user_id}_{file_name}"
    with _script_lock(key):
        if key in bot_scripts:
            kill_process_tree(bot_scripts[key])
            del bot_scripts[key]
        recovery_system.remove_running_script(user_id, file_name)
        if clear_log:
            log_path = get_script_log_path(user_id, file_name)
            try:
                if os.path.exists(log_path):
                    os.remove(log_path)
                    write_script_log(user_id, file_name, "🧹 Logs cleared", "SYSTEM")
            except Exception as e:
                error_logger.error(f"Error clearing log {log_path}: {e}")
        return True

def _launch_script(file_path, user_id, user_folder, file_name, file_type='py'):
    key = f"{user_id}_{file_name}"
    with _script_lock(key):
        if is_bot_running(user_id, file_name):
            return None
        
        # Create log file
        log_path = get_script_log_path(user_id, file_name)
        log_file = open(log_path, 'a', encoding='utf-8', errors='ignore')
        
        # Write startup log
        write_script_log(user_id, file_name, f"🚀 Starting script ({file_type.upper()})", "SYSTEM")
        write_script_log(user_id, file_name, f"📂 File: {file_name}", "INFO")
        write_script_log(user_id, file_name, f"👤 User: {user_id}", "INFO")
        
        cmd = [sys.executable, file_path] if file_type == 'py' else ['node', file_path]
        
        try:
            startupinfo = None
            if os.name == 'nt':
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE
            
            process = subprocess.Popen(
                cmd,
                cwd=user_folder,
                stdout=log_file,
                stderr=log_file,
                stdin=subprocess.PIPE,
                startupinfo=startupinfo,
                encoding='utf-8',
                errors='ignore'
            )
            
            bot_scripts[key] = {
                'process': process,
                'log_file': log_file,
                'file_name': file_name,
                'user_id': user_id,
                'start_time': datetime.now(),
                'type': file_type,
                'script_key': key
            }
            
            recovery_system.save_running_script(user_id, file_name, file_path, process.pid)
            write_script_log(user_id, file_name, f"✅ Script started (PID: {process.pid})", "SYSTEM")
            
            # Start monitor thread
            threading.Thread(target=_monitor_script, args=(key, process, log_file, user_id, file_name), daemon=True).start()
            
            return process
            
        except Exception as e:
            error_logger.exception(f"Error launching script {file_name}: {e}")
            write_script_log(user_id, file_name, f"❌ Failed to start: {str(e)[:100]}", "ERROR")
            try:
                log_file.close()
            except:
                pass
            return None

def _monitor_script(key, process, log_file, user_id, file_name):
    try:
        # Monitor process
        while True:
            try:
                exit_code = process.wait(timeout=1)
                write_script_log(user_id, file_name, f"🛑 Process exited with code {exit_code}", "SYSTEM")
                break
            except subprocess.TimeoutExpired:
                # Process still running
                continue
            except Exception as e:
                error_logger.error(f"Error monitoring script {file_name}: {e}")
                break
        
        # Cleanup
        if key in bot_scripts:
            del bot_scripts[key]
        recovery_system.remove_running_script(user_id, file_name)
        try:
            log_file.close()
        except:
            pass
            
    except Exception as e:
        error_logger.error(f"Error in monitor for {file_name}: {e}")

# ================================
# 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐇𝐀𝐍𝐃𝐋𝐄𝐑𝐒
# ================================
def create_reply_keyboard_main_menu(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        B("📤 𝐔𝐩𝐥𝐨𝐚𝐝"),
        B("📂 𝐌𝐚𝐧𝐚𝐠𝐞 𝐒𝐜𝐫𝐢𝐩𝐭𝐬"),
        B("⚡ 𝐒𝐩𝐞𝐞𝐝"),
        B("📊 𝐒𝐭𝐚𝐭𝐬"),
        B("👤 𝐏𝐫𝐨𝐟𝐢𝐥𝐞"),
        B("📦 𝐌𝐨𝐝𝐮𝐥𝐞"),
        B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫"),
        B("📜 𝐋𝐨𝐠𝐬"),  # New Logs button
        B("🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐁𝐨𝐭"),
    ]
    if user_id in admin_ids:
        buttons.append(B("🗄️ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞"))
    for i in range(0, len(buttons), 2):
        row = buttons[i:i+2]
        markup.add(*[types.KeyboardButton(text) for text in row])
    return markup

def create_manage_scripts_keyboard(user_id):
    markup = types.InlineKeyboardMarkup()
    files = user_files.get(user_id, [])
    if not files:
        return None
    
    for fname, ftype in files:
        running = is_bot_running(user_id, fname)
        status_text = "🟢 Running" if running else "🔴 Stopped"
        
        markup.add(types.InlineKeyboardButton(f"📂 {fname} | {status_text}", callback_data=f"info_{fname}"))
        
        row = []
        if running:
            row.append(types.InlineKeyboardButton("⏹ Stop", callback_data=f"stop_script_{fname}"))
        else:
            row.append(types.InlineKeyboardButton("▶ Start", callback_data=f"start_script_{fname}"))
        
        row.append(types.InlineKeyboardButton("🗑 Delete", callback_data=f"delete_script_{fname}"))
        row.append(types.InlineKeyboardButton("📜 Logs", callback_data=f"view_logs_{fname}"))
        row.append(types.InlineKeyboardButton("🧹 Clear Logs", callback_data=f"clear_logs_{fname}"))
        row.append(types.InlineKeyboardButton("🧹 Full Reset", callback_data=f"reset_script_{fname}"))
        markup.add(*row)
        markup.add(types.InlineKeyboardButton("━━━━━━━━━━━━━━", callback_data="none"))
        
    markup.add(types.InlineKeyboardButton("🔄 Refresh List", callback_data="manage_scripts"))
    return markup

def create_logs_dashboard_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📜 Bot Logs", callback_data="logs_bot"),
        types.InlineKeyboardButton("🖥️ System Logs", callback_data="logs_system"),
        types.InlineKeyboardButton("⚠️ Error Logs", callback_data="logs_error"),
        types.InlineKeyboardButton("📂 Script Logs", callback_data="logs_scripts")
    )
    markup.add(
        types.InlineKeyboardButton("📊 Stats", callback_data="logs_stats"),
        types.InlineKeyboardButton("🗑️ Clear All Logs", callback_data="logs_clear_all")
    )
    markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="logs_back"))
    return markup

def create_script_logs_keyboard(user_id, page=0):
    markup = types.InlineKeyboardMarkup(row_width=2)
    files = user_files.get(user_id, [])
    
    for fname, ftype in files:
        running = is_bot_running(user_id, fname)
        status = "🟢" if running else "🔴"
        markup.add(types.InlineKeyboardButton(
            f"{status} {fname}", 
            callback_data=f"script_log_{fname}"
        ))
    
    markup.add(types.InlineKeyboardButton("🔙 Back to Logs", callback_data="logs_back"))
    return markup

def create_log_view_keyboard(file_name, user_id, page=0, total_pages=1):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    if page > 0:
        markup.add(types.InlineKeyboardButton("⬅️ Previous", callback_data=f"log_page_{file_name}_{page-1}"))
    if page < total_pages - 1:
        markup.add(types.InlineKeyboardButton("Next ➡️", callback_data=f"log_page_{file_name}_{page+1}"))
    
    markup.add(
        types.InlineKeyboardButton("🔄 Refresh", callback_data=f"refresh_log_{file_name}"),
        types.InlineKeyboardButton("👁️ Live Logs", callback_data=f"live_log_{file_name}")
    )
    markup.add(
        types.InlineKeyboardButton("📥 Full Log", callback_data=f"download_log_{file_name}"),
        types.InlineKeyboardButton("🗑️ Clear", callback_data=f"clear_log_{file_name}")
    )
    markup.add(types.InlineKeyboardButton("🔙 Back to Scripts", callback_data="logs_scripts"))
    return markup

def create_live_log_keyboard(file_name, user_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("⏹ Stop Live Logs", callback_data=f"stop_live_{file_name}"))
    markup.add(types.InlineKeyboardButton("🔙 Back to Log", callback_data=f"view_logs_{file_name}"))
    return markup

def create_clear_logs_confirmation():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("✅ Confirm", callback_data="confirm_clear_logs"),
        types.InlineKeyboardButton("❌ Cancel", callback_data="cancel_clear_logs")
    )
    return markup

# ================================
# 𝐋𝐎𝐆𝐒 𝐒𝐘𝐒𝐓𝐄𝐌 𝐇𝐀𝐍𝐃𝐋𝐄𝐑𝐒
# ================================
def show_logs_dashboard(message, user_id):
    """Show the Logs Dashboard"""
    stats = get_log_statistics()
    running_count = len(bot_scripts)
    
    dashboard = f"""╔══════════════════════════════════╗
║       📜 𝐋𝐎𝐆 𝐂𝐄𝐍𝐓𝐄𝐑            ║
╚══════════════════════════════════╝

🟢 SYSTEM     ONLINE
📂 LOG FILES  {stats['total_files']:02}
⚠️ ERRORS     {stats['error_count']:02}

📊 LOG STATISTICS
━━━━━━━━━━━━━━━━━━━━━━
📂 Files:     {stats['total_files']:02}
💾 Size:      {stats['total_size_mb']:.1f} MB
🟢 Running:   {running_count:02}
🔴 Errors:    {stats['error_count']:02}
🕒 Last Event: {stats['last_event']}

━━━━━━━━━━━━━━━━━━━━━━
📜 Select a log type below:
"""
    
    msg = bot.reply_to(message, dashboard, parse_mode='Markdown',
                       reply_markup=create_logs_dashboard_keyboard())
    
    # Run animation
    try:
        AnimationManager.animate_logs(message.chat.id, msg.message_id)
    except Exception:
        pass

def show_script_logs(message, user_id):
    """Show the Script Logs list"""
    files = user_files.get(user_id, [])
    if not files:
        bot.reply_to(message, B("📭 No scripts uploaded yet."),
                     reply_markup=create_reply_keyboard_main_menu(user_id))
        return
    
    markup = create_script_logs_keyboard(user_id)
    bot.reply_to(message, B("📂 𝐒𝐂𝐑𝐈𝐏𝐓 𝐋𝐎𝐆𝐒\n\nSelect a script to view its logs:"), 
                 reply_markup=markup, parse_mode='Markdown')

def show_script_log(message, user_id, file_name, page=0):
    """Show a specific script's log with pagination"""
    lines, total = get_script_log_lines(user_id, file_name, limit=50, offset=page*50)
    
    if not lines and total == 0:
        bot.reply_to(message, B(f"📭 No logs found for `{file_name}`"), parse_mode='Markdown')
        return
    
    total_pages = max(1, (total + 49) // 50)
    running = is_bot_running(user_id, file_name)
    
    log_text = f"""╔══════════════════════════════════╗
║       📜 𝐒𝐂𝐑𝐈𝐏𝐓 𝐋𝐎𝐆            ║
╚══════════════════════════════════╝

📄 File: {file_name}
🟢 Status: {'RUNNING' if running else 'STOPPED'}
🆔 PID: {bot_scripts.get(f'{user_id}_{file_name}', {}).get('process', {}).pid if running else 'N/A'}

━━━━━━━━━━━━━━━━━━━━━━
📄 Page {page+1}/{total_pages} ({len(lines)} lines)
━━━━━━━━━━━━━━━━━━━━━━

"""
    
    for line in lines[-50:]:  # Show last 50 lines of the page
        log_text += sanitize_log_text(line)
    
    if len(log_text) > 4000:
        log_text = log_text[:4000] + "\n... (truncated)"
    
    markup = create_log_view_keyboard(file_name, user_id, page, total_pages)
    bot.reply_to(message, log_text, parse_mode='Markdown', reply_markup=markup)

# ================================
# 𝐋𝐈𝐕𝐄 𝐋𝐎𝐆𝐒 𝐒𝐘𝐒𝐓𝐄𝐌
# ================================
_live_log_tasks = {}
_live_log_locks = {}

def start_live_logs(user_id, file_name, chat_id, message_id):
    """Start live logs for a script"""
    task_key = f"{user_id}_{file_name}"
    
    # Stop existing live log
    stop_live_logs(user_id, file_name)
    
    def _live_log_worker():
        lock = _live_log_locks.setdefault(task_key, threading.Lock())
        with lock:
            last_lines = []
            iteration = 0
            running = True
            
            while running:
                try:
                    # Check if script still exists
                    if task_key not in bot_scripts and not is_bot_running(user_id, file_name):
                        try:
                            bot.edit_message_text(
                                B(f"⏹️ Script `{file_name}` has stopped.\n\nLive logs ended."),
                                chat_id, message_id, parse_mode='Markdown'
                            )
                        except:
                            pass
                        break
                    
                    # Get latest lines
                    lines, total = get_script_log_lines(user_id, file_name, limit=30)
                    
                    if lines != last_lines:
                        last_lines = lines
                        log_text = f"📜 LIVE LOGS: {file_name}\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
                        for line in lines[-30:]:
                            log_text += sanitize_log_text(line)
                        if len(log_text) > 4000:
                            log_text = log_text[:4000] + "\n... (truncated)"
                        
                        try:
                            bot.edit_message_text(
                                log_text,
                                chat_id, message_id,
                                parse_mode='Markdown',
                                reply_markup=create_live_log_keyboard(file_name, user_id)
                            )
                        except Exception as e:
                            if "message is not modified" not in str(e).lower():
                                error_logger.error(f"Live log edit error: {e}")
                    
                    # Check if task was cancelled
                    if task_key not in _live_log_tasks:
                        break
                    
                    time.sleep(2.5)
                    iteration += 1
                    
                except Exception as e:
                    error_logger.error(f"Live log worker error: {e}")
                    time.sleep(3)
    
    # Start worker in thread
    thread = threading.Thread(target=_live_log_worker, daemon=True)
    thread.start()
    _live_log_tasks[task_key] = thread
    
    return thread

def stop_live_logs(user_id, file_name):
    """Stop live logs for a script"""
    task_key = f"{user_id}_{file_name}"
    if task_key in _live_log_tasks:
        thread = _live_log_tasks[task_key]
        del _live_log_tasks[task_key]
        # Thread will exit on next iteration
        return True
    return False

def cleanup_all_live_logs():
    """Clean up all live log tasks"""
    for key in list(_live_log_tasks.keys()):
        del _live_log_tasks[key]
    _live_log_tasks.clear()

# ================================
# 𝐂𝐀𝐋𝐋𝐁𝐀𝐂𝐊 𝐇𝐀𝐍𝐃𝐋𝐄𝐑𝐒
# ================================
@bot.callback_query_handler(func=lambda call: True)
def callback_router(call):
    user_id = call.from_user.id
    add_active_user(user_id)
    data = call.data
    
    try:
        # ── Logs System ──
        if data == 'logs_back':
            show_logs_dashboard(call.message, user_id)
            
        elif data == 'logs_bot':
            # Show bot logs
            if os.path.exists(BOT_LOG_PATH):
                with open(BOT_LOG_PATH, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                log_text = "📜 BOT LOGS\n━━━━━━━━━━━━━━━━\n\n" + ''.join(lines[-50:])
                if len(log_text) > 4000:
                    log_text = log_text[:4000] + "\n... (truncated)"
                bot.edit_message_text(log_text, call.message.chat.id, call.message.message_id,
                                     reply_markup=create_logs_dashboard_keyboard())
            else:
                bot.answer_callback_query(call.id, "No bot logs found")
                
        elif data == 'logs_system':
            if os.path.exists(SYSTEM_LOG_PATH):
                with open(SYSTEM_LOG_PATH, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                log_text = "🖥️ SYSTEM LOGS\n━━━━━━━━━━━━━━━━\n\n" + ''.join(lines[-50:])
                if len(log_text) > 4000:
                    log_text = log_text[:4000] + "\n... (truncated)"
                bot.edit_message_text(log_text, call.message.chat.id, call.message.message_id,
                                     reply_markup=create_logs_dashboard_keyboard())
            else:
                bot.answer_callback_query(call.id, "No system logs found")
                
        elif data == 'logs_error':
            if os.path.exists(ERROR_LOG_PATH):
                with open(ERROR_LOG_PATH, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                log_text = "⚠️ ERROR LOGS\n━━━━━━━━━━━━━━━━\n\n" + ''.join(lines[-50:])
                if len(log_text) > 4000:
                    log_text = log_text[:4000] + "\n... (truncated)"
                bot.edit_message_text(log_text, call.message.chat.id, call.message.message_id,
                                     reply_markup=create_logs_dashboard_keyboard())
            else:
                bot.answer_callback_query(call.id, "No error logs found")
                
        elif data == 'logs_scripts':
            show_script_logs(call.message, user_id)
            
        elif data == 'logs_stats':
            stats = get_log_statistics()
            running_count = len(bot_scripts)
            stats_text = f"""📊 LOG STATISTICS
━━━━━━━━━━━━━━━━━━━━━━
📂 Files:     {stats['total_files']:02}
💾 Size:      {stats['total_size_mb']:.1f} MB
🟢 Running:   {running_count:02}
🔴 Errors:    {stats['error_count']:02}
🕒 Last Event: {stats['last_event']}
━━━━━━━━━━━━━━━━━━━━━━"""
            bot.edit_message_text(stats_text, call.message.chat.id, call.message.message_id,
                                 reply_markup=create_logs_dashboard_keyboard())
                
        elif data == 'logs_clear_all':
            bot.edit_message_text(
                B("⚠️ 𝐂𝐋𝐄𝐀𝐑 𝐀𝐋𝐋 𝐋𝐎𝐆𝐒?\n\nThis will permanently remove all log history.\n\nThis will NOT delete scripts or configuration."),
                call.message.chat.id, call.message.message_id,
                reply_markup=create_clear_logs_confirmation()
            )
            
        elif data == 'confirm_clear_logs':
            try:
                for root, dirs, files in os.walk(LOGS_DIR):
                    for file in files:
                        if file.endswith('.log'):
                            path = os.path.join(root, file)
                            with open(path, 'w', encoding='utf-8') as f:
                                f.write(f"--- Logs cleared at {datetime.now().isoformat()} ---\n")
                bot.edit_message_text(
                    B("✅ All logs have been cleared."),
                    call.message.chat.id, call.message.message_id,
                    reply_markup=create_logs_dashboard_keyboard()
                )
            except Exception as e:
                error_logger.error(f"Error clearing logs: {e}")
                bot.answer_callback_query(call.id, "Error clearing logs", show_alert=True)
                
        elif data == 'cancel_clear_logs':
            show_logs_dashboard(call.message, user_id)
            
        elif data.startswith('script_log_'):
            file_name = data.replace('script_log_', '')
            if not any(fname == file_name for fname, _ in user_files.get(user_id, [])):
                bot.answer_callback_query(call.id, "Not authorized", show_alert=True)
                return
            show_script_log(call.message, user_id, file_name)
            
        elif data.startswith('log_page_'):
            parts = data.split('_')
            file_name = '_'.join(parts[2:-1]) or parts[2]
            page = int(parts[-1])
            show_script_log(call.message, user_id, file_name, page)
            
        elif data.startswith('refresh_log_'):
            file_name = data.replace('refresh_log_', '')
            show_script_log(call.message, user_id, file_name, 0)
            
        elif data.startswith('download_log_'):
            file_name = data.replace('download_log_', '')
            if not any(fname == file_name for fname, _ in user_files.get(user_id, [])):
                bot.answer_callback_query(call.id, "Not authorized", show_alert=True)
                return
            
            log_path = get_script_log_path(user_id, file_name)
            if os.path.exists(log_path):
                try:
                    # Send as document
                    with open(log_path, 'rb') as f:
                        bot.send_document(call.from_user.id, f, 
                                        caption=B(f"📥 Full log for {file_name}"),
                                        reply_markup=create_reply_keyboard_main_menu(user_id))
                    bot.answer_callback_query(call.id, "📥 Log sent")
                except Exception as e:
                    error_logger.error(f"Error sending log {log_path}: {e}")
                    bot.answer_callback_query(call.id, "Error sending log", show_alert=True)
            else:
                bot.answer_callback_query(call.id, "No log file found", show_alert=True)
                
        elif data.startswith('clear_log_'):
            file_name = data.replace('clear_log_', '')
            if not any(fname == file_name for fname, _ in user_files.get(user_id, [])):
                bot.answer_callback_query(call.id, "Not authorized", show_alert=True)
                return
            
            # Show confirmation
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton("✅ Confirm", callback_data=f"confirm_clear_{file_name}"),
                types.InlineKeyboardButton("❌ Cancel", callback_data=f"view_logs_{file_name}")
            )
            bot.edit_message_text(
                B(f"⚠️ 𝐂𝐋𝐄𝐀𝐑 𝐋𝐎𝐆𝐒?\n\nThis will permanently remove log history for `{file_name}`."),
                call.message.chat.id, call.message.message_id,
                parse_mode='Markdown', reply_markup=markup
            )
            
        elif data.startswith('confirm_clear_'):
            file_name = data.replace('confirm_clear_', '')
            log_path = get_script_log_path(user_id, file_name)
            try:
                if os.path.exists(log_path):
                    with open(log_path, 'w', encoding='utf-8') as f:
                        f.write(f"--- Logs cleared at {datetime.now().isoformat()} ---\n")
                bot.answer_callback_query(call.id, "✅ Logs cleared")
                show_script_log(call.message, user_id, file_name)
            except Exception as e:
                error_logger.error(f"Error clearing script log {log_path}: {e}")
                bot.answer_callback_query(call.id, "Error clearing logs", show_alert=True)
                
        elif data.startswith('live_log_'):
            file_name = data.replace('live_log_', '')
            if not any(fname == file_name for fname, _ in user_files.get(user_id, [])):
                bot.answer_callback_query(call.id, "Not authorized", show_alert=True)
                return
            
            if not is_bot_running(user_id, file_name):
                bot.answer_callback_query(call.id, "⚠️ Script is not running", show_alert=True)
                return
            
            # Start live logs
            msg = bot.edit_message_text(
                B(f"👁️ LIVE LOGS: {file_name}\n\nLoading..."),
                call.message.chat.id, call.message.message_id
            )
            start_live_logs(user_id, file_name, call.message.chat.id, msg.message_id)
            bot.answer_callback_query(call.id, "👁️ Live logs started")
            
        elif data.startswith('stop_live_'):
            file_name = data.replace('stop_live_', '')
            if stop_live_logs(user_id, file_name):
                bot.answer_callback_query(call.id, "⏹️ Live logs stopped")
                show_script_log(call.message, user_id, file_name)
            else:
                bot.answer_callback_query(call.id, "No live logs running")
                
        elif data.startswith('view_logs_'):
            file_name = data.replace('view_logs_', '')
            show_script_log(call.message, user_id, file_name)
            
        # ── Script Management ──
        elif data == 'manage_scripts':
            update_manage_scripts_message(call, user_id)
            
        elif data.startswith('start_script_'):
            file_name = data.replace('start_script_', '')
            if not any(fname == file_name for fname, _ in user_files.get(user_id, [])):
                bot.answer_callback_query(call.id, "Not authorized", show_alert=True)
                return
            
            if is_bot_running(user_id, file_name):
                bot.answer_callback_query(call.id, "⚠️ Already running", show_alert=True)
                return
            
            user_folder = get_user_folder(user_id)
            file_path = os.path.join(user_folder, file_name)
            
            if not os.path.exists(file_path):
                bot.answer_callback_query(call.id, "File not found", show_alert=True)
                return
            
            # Install missing modules for Python scripts
            if file_name.endswith('.py'):
                bot.answer_callback_query(call.id, "📦 Checking modules...")
                install_missing_modules(file_path, call.message)
            
            file_type = 'py' if file_name.endswith('.py') else 'js'
            _launch_script(file_path, user_id, user_folder, file_name, file_type)
            bot.answer_callback_query(call.id, "🚀 Script started")
            time.sleep(0.5)
            update_manage_scripts_message(call, user_id)
            
        elif data.startswith('stop_script_'):
            file_name = data.replace('stop_script_', '')
            if not any(fname == file_name for fname, _ in user_files.get(user_id, [])):
                bot.answer_callback_query(call.id, "Not authorized", show_alert=True)
                return
            
            _cleanup_script_runtime(user_id, file_name)
            bot.answer_callback_query(call.id, "🛑 Script stopped")
            time.sleep(0.5)
            update_manage_scripts_message(call, user_id)
            
        elif data.startswith('delete_script_'):
            file_name = data.replace('delete_script_', '')
            if not any(fname == file_name for fname, _ in user_files.get(user_id, [])):
                bot.answer_callback_query(call.id, "Not authorized", show_alert=True)
                return
            
            _cleanup_script_runtime(user_id, file_name, clear_log=True)
            remove_user_file_db(user_id, file_name)
            bot.answer_callback_query(call.id, "🗑️ Script deleted")
            time.sleep(0.5)
            update_manage_scripts_message(call, user_id)
            
        elif data.startswith('clear_logs_'):
            file_name = data.replace('clear_logs_', '')
            if not any(fname == file_name for fname, _ in user_files.get(user_id, [])):
                bot.answer_callback_query(call.id, "Not authorized", show_alert=True)
                return
            
            log_path = get_script_log_path(user_id, file_name)
            try:
                if os.path.exists(log_path):
                    with open(log_path, 'w', encoding='utf-8') as f:
                        f.write(f"--- Logs cleared at {datetime.now().isoformat()} ---\n")
                bot.answer_callback_query(call.id, "✅ Logs cleared")
            except Exception as e:
                error_logger.error(f"Error clearing logs: {e}")
                bot.answer_callback_query(call.id, "Error clearing logs", show_alert=True)
                
        elif data.startswith('reset_script_'):
            file_name = data.replace('reset_script_', '')
            if not any(fname == file_name for fname, _ in user_files.get(user_id, [])):
                bot.answer_callback_query(call.id, "Not authorized", show_alert=True)
                return
            
            AnimationManager.animate_full_reset(call.message.chat.id, call.message.message_id)
            _cleanup_script_runtime(user_id, file_name, clear_log=True)
            bot.answer_callback_query(call.id, "🧹 Full reset complete")
            update_manage_scripts_message(call, user_id)
            
        elif data == 'info_':
            bot.answer_callback_query(call.id, "📂 Script info")
            
        elif data == 'none':
            bot.answer_callback_query(call.id, "━━━━━━━━━━━━━━")
            
        else:
            bot.answer_callback_query(call.id, "🔍 Unknown action")
            
    except Exception as e:
        error_logger.exception(f"Callback error: {e}")
        try:
            bot.answer_callback_query(call.id, "❌ Error", show_alert=True)
        except:
            pass

def update_manage_scripts_message(call, user_id):
    kb = create_manage_scripts_keyboard(user_id)
    if not kb:
        bot.edit_message_text(B("📂 No scripts uploaded yet."), 
                             call.message.chat.id, call.message.message_id,
                             reply_markup=create_reply_keyboard_main_menu(user_id))
        return
    
    try:
        bot.edit_message_text(B("📂 MANAGE SCRIPTS\n\nSelect a script to control:"),
                             call.message.chat.id, call.message.message_id,
                             reply_markup=kb, parse_mode='Markdown')
    except Exception as e:
        if "message is not modified" not in str(e).lower():
            error_logger.error(f"Error updating manage scripts: {e}")

# ================================
# 𝐌𝐀𝐈𝐍 𝐌𝐄𝐍𝐔 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐇𝐀𝐍𝐃𝐋𝐄𝐑
# ================================
@bot.message_handler(func=lambda message: message.text and (
    message.text == B("📤 𝐔𝐩𝐥𝐨𝐚𝐝") or
    message.text == B("📂 𝐌𝐚𝐧𝐚𝐠𝐞 𝐒𝐜𝐫𝐢𝐩𝐭𝐬") or
    message.text == B("⚡ 𝐒𝐩𝐞𝐞𝐝") or
    message.text == B("📊 𝐒𝐭𝐚𝐭𝐬") or
    message.text == B("👤 𝐏𝐫𝐨𝐟𝐢𝐥𝐞") or
    message.text == B("📦 𝐌𝐨𝐝𝐮𝐥𝐞") or
    message.text == B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫") or
    message.text == B("📜 𝐋𝐨𝐠𝐬") or
    message.text == B("🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐁𝐨𝐭") or
    message.text == B("🗄️ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞")
))
def handle_main_menu_message(message):
    user_id = message.from_user.id
    add_active_user(user_id)
    text = message.text

    if text == B("🗄️ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞"):
        if user_id not in admin_ids:
            bot.reply_to(message, B("🔒 Admin/owner only."))
            return
        bot.reply_to(message, B("🗄️ DATABASE MANAGER"), reply_markup=create_database_keyboard())

    elif text == B("📤 𝐔𝐩𝐥𝐨𝐚𝐝"):
        bot.reply_to(message, B("📤 Send your .py or .js file now!\n\n📋 Supported: .py, .js, .zip"),
                     reply_markup=create_reply_keyboard_main_menu(user_id))

    elif text == B("📂 𝐌𝐚𝐧𝐚𝐠𝐞 𝐒𝐜𝐫𝐢𝐩𝐭𝐬"):
        show_manage_scripts(message, user_id)

    elif text == B("⚡ 𝐒𝐩𝐞𝐞𝐝"):
        run_speedtest(message)

    elif text == B("📊 𝐒𝐭𝐚𝐭𝐬"):
        show_stats(message)

    elif text == B("👤 𝐏𝐫𝐨𝐟𝐢𝐥𝐞"):
        show_profile(message)

    elif text == B("📦 𝐌𝐨𝐝𝐮𝐥𝐞"):
        user_tier = get_user_tier(user_id)
        tier_info = TIER_SYSTEM[user_tier]
        module_text = f"""╔══════════════════════════════════╗
║    📦 MODULE MANAGER             ║
╚══════════════════════════════════╝

*Installed Modules:*
📦 telebot, requests, psutil, flask
📦 qrcode, Pillow, cryptography
📦 httpx, aiofiles, anyio

*Upload a script to auto-install dependencies!*"""
        msg = bot.reply_to(message, module_text, parse_mode='Markdown',
                           reply_markup=create_reply_keyboard_main_menu(user_id))
        try:
            AnimationManager.animate_install(message.chat.id, msg.message_id)
        except Exception:
            pass

    elif text == B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫"):
        msg = bot.reply_to(message, B("🛰 Initiating recovery..."))
        try:
            AnimationManager.animate_recovery(message.chat.id, msg.message_id)
        except Exception:
            pass
        time.sleep(2)
        recovered = recovery_system.recover_all_scripts()
        try:
            if recovered:
                bot.edit_message_text(
                    B(f"✅ Recovery Complete!\n🔄 Recovered: {len(recovered)} script(s)"),
                    message.chat.id, msg.message_id,
                    reply_markup=create_reply_keyboard_main_menu(user_id))
            else:
                bot.edit_message_text(B("📭 No scripts to recover."),
                                     message.chat.id, msg.message_id,
                                     reply_markup=create_reply_keyboard_main_menu(user_id))
        except Exception:
            pass

    elif text == B("📜 𝐋𝐨𝐠𝐬"):
        show_logs_dashboard(message, user_id)

    elif text == B("🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐁𝐨𝐭"):
        if user_id != OWNER_ID:
            bot.reply_to(message, B("🔒 Owner only."))
            return
        msg = bot.reply_to(message, B("🚀 Restarting bot..."))
        try:
            AnimationManager.animate_full_restart(message.chat.id, msg.message_id)
        except Exception:
            pass
        time.sleep(2.5)
        threading.Thread(target=send_restart_notification).start()
        os.execl(sys.executable, sys.executable, *sys.argv)

def show_manage_scripts(message, user_id):
    files = user_files.get(user_id, [])
    if not files:
        bot.reply_to(message, B("📂 No scripts uploaded yet."), 
                     reply_markup=create_reply_keyboard_main_menu(user_id))
        return
    
    kb = create_manage_scripts_keyboard(user_id)
    bot.reply_to(message, B("📂 MANAGE SCRIPTS\n\nSelect a script to control:"), 
                 reply_markup=kb, parse_mode='Markdown')

# ================================
# 𝐃𝐎𝐂𝐔𝐌𝐄𝐍𝐓 (𝐔𝐏𝐋𝐎𝐀𝐃) 𝐇𝐀𝐍𝐃𝐋𝐄𝐑
# ================================
@bot.message_handler(content_types=['document'])
def handle_document(message):
    user_id = message.from_user.id
    add_active_user(user_id)
    
    if bot_locked and user_id != OWNER_ID:
        bot.reply_to(message, "🔒 Bot is locked.")
        return
    
    doc = message.document
    file_name = doc.file_name
    file_ext = os.path.splitext(file_name)[1].lower()
    
    if file_ext not in ['.py', '.js', '.zip']:
        bot.reply_to(message, B("❌ Only .py, .js, and .zip files allowed."))
        return
    
    user_tier = get_user_tier(user_id)
    max_size = TIER_SYSTEM[user_tier]['max_file_size']
    if doc.file_size > max_size:
        max_mb = max_size // (1024 * 1024) if max_size != float('inf') else '∞'
        bot.reply_to(message, B(f"❌ File too large. Max: {max_mb} MB"))
        return
    
    file_count = get_user_file_count(user_id)
    file_limit = get_user_file_limit(user_id)
    if file_count >= file_limit:
        bot.reply_to(message, B(f"❌ File limit reached ({file_limit}). Delete a file first."))
        return
    
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    
    msg = bot.reply_to(message, B("🚀 Initiating upload sequence..."))
    
    try:
        AnimationManager.animate_upload(message.chat.id, msg.message_id)
    except Exception:
        pass
    
    try:
        file_info = bot.get_file(doc.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        with open(file_path, 'wb') as f:
            f.write(downloaded_file)
        
        file_type = 'py' if file_ext == '.py' else 'js'
        save_user_file_db(user_id, file_name, file_type)
        
        # Auto-install modules for Python files
        if file_ext == '.py':
            try:
                install_missing_modules(file_path, message)
            except Exception as e:
                error_logger.error(f"Auto-install error for {file_name}: {e}")
        
        time.sleep(3)
        
        tier_info = TIER_SYSTEM[get_user_tier(user_id)]
        upload_text = f"""╔══════════════════════════════════╗
║    ✅ UPLOAD SUCCESSFUL         ║
╠══════════════════════════════════╣
║    📂 {file_name}
║    💾 {doc.file_size / 1024:.1f} KB
║    {tier_info['icon']} {tier_info['name']} TIER
╚══════════════════════════════════╝

📊 *Status:* Ready to host
🔄 *Auto-Recovery:* {'✅ Enabled' if tier_info['auto_restart'] else '❌ Disabled'}
📦 *Modules:* Auto-installed"""
        
        bot.edit_message_text(upload_text, message.chat.id, msg.message_id, parse_mode='Markdown',
                             reply_markup=create_reply_keyboard_main_menu(user_id))
        
    except Exception as e:
        error_logger.exception(f"Upload error for {file_name}: {e}")
        bot.edit_message_text(B(f"❌ Upload Failed: {str(e)[:100]}"), message.chat.id, msg.message_id,
                             reply_markup=create_reply_keyboard_main_menu(user_id))

# ================================
# 𝐒𝐏𝐄𝐄𝐃 𝐓𝐄𝐒𝐓
# ================================
_SPEED_TEST_DOWNLOAD_URL = 'https://speed.cloudflare.com/__down?bytes=10000000'
_SPEED_TEST_UPLOAD_URL = 'https://speed.cloudflare.com/__up'
_SPEED_TEST_LATENCY_URL = 'https://speed.cloudflare.com/cdn-cgi/trace'
_SPEED_TEST_TIMEOUT = (5, 20)

async def _async_measure_download():
    client = http_client
    response = await client.get(_SPEED_TEST_DOWNLOAD_URL)
    response.raise_for_status()
    return len(response.content)

async def _async_measure_latency():
    client = http_client
    start_time = time.time()
    await client.get(_SPEED_TEST_LATENCY_URL)
    return (time.time() - start_time) * 1000

def _run_speed_test_sync(chat_id, message_id, user_id):
    try:
        # Run async operations
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # Download test
        try:
            start = time.time()
            response = requests.get(_SPEED_TEST_DOWNLOAD_URL, timeout=_SPEED_TEST_TIMEOUT)
            response.raise_for_status()
            download_mbps = (len(response.content) * 8) / (time.time() - start) / 1_000_000
        except Exception as e:
            error_logger.error(f"Download test failed: {e}")
            download_mbps = None
        
        # Upload test
        try:
            payload = os.urandom(4 * 1024 * 1024)
            start = time.time()
            response = requests.post(_SPEED_TEST_UPLOAD_URL, data=payload, timeout=_SPEED_TEST_TIMEOUT)
            response.raise_for_status()
            upload_mbps = (len(payload) * 8) / (time.time() - start) / 1_000_000
        except Exception as e:
            error_logger.error(f"Upload test failed: {e}")
            upload_mbps = None
        
        # Latency test
        try:
            start = time.time()
            response = requests.get(_SPEED_TEST_LATENCY_URL, timeout=_SPEED_TEST_TIMEOUT)
            response.raise_for_status()
            latency_ms = (time.time() - start) * 1000
        except Exception as e:
            error_logger.error(f"Latency test failed: {e}")
            latency_ms = None
        
        if download_mbps is None and upload_mbps is None and latency_ms is None:
            bot.edit_message_text('❌ SPEED TEST FAILED\n━━━━━━━━━━━━━━━━━━━━\nUnable to connect to test server.', chat_id, message_id)
            return
        
        tested = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result = (
            '╭━━━━━━━━━━━━━━━━━━━━╮\n'
            '│   ⚡ SPEED TEST    │\n'
            '╰━━━━━━━━━━━━━━━━━━━━╯\n\n'
            + (f'📥 Download   : {download_mbps:.2f} Mbps\n' if download_mbps else '📥 Download   : N/A\n')
        )
        result += f'📤 Upload     : {upload_mbps:.2f} Mbps\n' if upload_mbps else '📤 Upload     : N/A\n'
        result += f'⏱️ Latency    : {latency_ms:.0f} ms\n' if latency_ms else '⏱️ Latency    : N/A\n'
        result += f'\n🌐 Server     : Cloudflare\n🕐 Tested     : {tested}\n\n━━━━━━━━━━━━━━━━━━━━\n✅ TEST COMPLETE'
        
        bot.edit_message_text(result, chat_id, message_id, reply_markup=create_reply_keyboard_main_menu(user_id))
        
    except Exception as e:
        error_logger.exception(f"Speed test failed: {e}")
        bot.edit_message_text('❌ SPEED TEST FAILED\n━━━━━━━━━━━━━━━━━━━━\nUnable to complete test.\n\nPlease try again.', chat_id, message_id)

@bot.message_handler(commands=['speed'])
def run_speedtest(message):
    user_id = message.from_user.id
    add_active_user(user_id)
    msg = bot.reply_to(message, '⚡ SPEED TEST\n━━━━━━━━━━━━━━━━━━━━\n◐ Connecting to test server...')
    threading.Thread(target=_run_speed_test_sync, args=(message.chat.id, msg.message_id, user_id), daemon=True).start()

# ================================
# 𝐎𝐓𝐇𝐄𝐑 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒
# ================================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    add_active_user(user_id)
    user_tier = get_user_tier(user_id)
    tier_info = TIER_SYSTEM[user_tier]
    
    welcome_text = f"""☁️ 𝘿𝘼𝙍𝙇𝙄𝙉𝙂 𝙃𝙊𝙎𝙏𝙄𝙉𝙂 𝘽𝙊𝙏

🟢 𝗙𝗨𝗟𝗟 𝗔𝗖𝗖𝗘𝗦𝗦
📂 𝗙𝗶𝗹𝗲𝘀 • ∞ Unlimited
💾 𝗦𝗶𝘇𝗲 • ∞ Unlimited

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
    try:
        AnimationManager.animate_dashboard(message.chat.id, msg.message_id)
    except Exception:
        pass

@bot.message_handler(commands=['help'])
def send_help(message):
    user_id = message.from_user.id
    help_text = f"""╔══════════════════════════════════╗
║    📋 HELP GUIDE               ║
╚══════════════════════════════════╝

*Commands:*
/start — Open main menu
/help — This help menu
/stats — Your stats
/profile — Your profile
/speed — Speed test

*How to use:*
1️⃣ Upload a .py or .js file
2️⃣ Modules auto-installed
3️⃣ Click Start to run
4️⃣ View live logs
5️⃣ Restart/Stop/Delete anytime

*Auto-Recovery:* ✅ Enabled"""
    
    bot.reply_to(message, help_text, parse_mode='Markdown',
                 reply_markup=create_reply_keyboard_main_menu(user_id))

@bot.message_handler(commands=['stats'])
def show_stats(message):
    user_id = message.from_user.id
    add_active_user(user_id)
    user_tier = get_user_tier(user_id)
    tier_info = TIER_SYSTEM[user_tier]
    file_count = get_user_file_count(user_id)
    
    stats_text = f"""╔══════════════════════════════════╗
║    📊 YOUR STATS                ║
╚══════════════════════════════════╝

{tier_info['icon']} *Tier: {tier_info['name']}*
📂 *Files:* {file_count}/∞
🚀 *Running:* {sum(1 for key, info in bot_scripts.items() if info['user_id'] == user_id and is_bot_running(user_id, info['file_name']))}

*Account Info:*
🆔 User ID: {user_id}
👤 Username: @{message.from_user.username or 'NOT SET'}
📅 Joined: {datetime.now().strftime('%Y-%m-%d')}"""
    
    msg = bot.reply_to(message, stats_text, parse_mode='Markdown',
                       reply_markup=create_reply_keyboard_main_menu(user_id))
    try:
        AnimationManager.animate_dashboard(message.chat.id, msg.message_id)
    except Exception:
        pass

@bot.message_handler(commands=['profile'])
def show_profile(message):
    user_id = message.from_user.id
    add_active_user(user_id)
    user_tier = get_user_tier(user_id)
    tier_info = TIER_SYSTEM[user_tier]
    
    profile_text = f"""╔══════════════════════════════════╗
║    👤 YOUR PROFILE              ║
╚══════════════════════════════════╝

👤 *Name:* {message.from_user.first_name}
🆔 *User ID:* {user_id}
@ *Username:* @{message.from_user.username or 'NOT SET'}
{tier_info['icon']} *Tier:* {tier_info['name']}"""
    
    bot.reply_to(message, profile_text, parse_mode='Markdown',
                 reply_markup=create_reply_keyboard_main_menu(user_id))

@bot.message_handler(func=lambda message: message.text and (
    message.text.startswith(B("🔴 𝐒𝐭𝐨𝐩 ")) or
    message.text.startswith(B("🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 ")) or
    message.text.startswith(B("🗑️ 𝐃𝐞𝐥𝐞𝐭𝐞 ")) or
    message.text.startswith(B("📜 𝐋𝐨𝐠𝐬 ")) or
    message.text.startswith(B("📜 𝐕𝐢𝐞𝐰 𝐋𝐨𝐠𝐬 ")) or
    message.text.startswith(B("🟢 𝐒𝐭𝐚𝐫𝐭 "))
))
def handle_file_control_message(message):
    handle_file_control_text(message)

def handle_file_control_text(message):
    user_id = message.from_user.id
    text = message.text
    raw_file_name = text.split(' ', 2)[-1] if ' ' in text else ''
    file_name = unbold(raw_file_name)
    
    if "🟢" in text and "𝐒𝐭𝐚𝐫𝐭" in text:
        _start_script(message, user_id, file_name)
    elif "🔴" in text and "𝐒𝐭𝐨𝐩" in text:
        _stop_script(message, user_id, file_name)
    elif "🔄" in text and "𝐑𝐞𝐬𝐭𝐚𝐫𝐭" in text:
        _restart_script(message, user_id, file_name)
    elif "🗑️" in text and "𝐃𝐞𝐥𝐞𝐭𝐞" in text:
        _delete_script(message, user_id, file_name)
    elif "📜" in text and ("𝐋𝐨𝐠𝐬" in text or "𝐕𝐢𝐞𝐰" in text):
        _show_logs(message, user_id, file_name)

def _start_script(message, user_id, file_name):
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    
    if not os.path.exists(file_path):
        bot.reply_to(message, B(f"❌ File not found: `{file_name}`"), parse_mode='Markdown')
        return
    
    if is_bot_running(user_id, file_name):
        bot.reply_to(message, B(f"⚠️ `{file_name}` is already running."), parse_mode='Markdown')
        return
    
    msg = bot.reply_to(message, B(f"🚀 Starting `{file_name}`..."))
    
    try:
        AnimationManager.animate_start(message.chat.id, msg.message_id)
    except Exception:
        pass
    
    # Install missing modules
    if file_name.endswith('.py'):
        install_missing_modules(file_path, message)
    
    file_type = 'py' if file_name.endswith('.py') else 'js'
    process = _launch_script(file_path, user_id, user_folder, file_name, file_type)
    
    if process:
        time.sleep(1)
        try:
            bot.edit_message_text(
                B(f"🟢 `{file_name}` is now running!\n📋 PID: {process.pid}"),
                message.chat.id, msg.message_id, parse_mode='Markdown',
                reply_markup=create_reply_keyboard_main_menu(user_id)
            )
        except Exception:
            pass

def _stop_script(message, user_id, file_name):
    if not is_bot_running(user_id, file_name):
        bot.reply_to(message, B(f"⚠️ `{file_name}` is not running."), parse_mode='Markdown')
        return
    
    msg = bot.reply_to(message, B(f"🛑 Stopping `{file_name}`..."))
    
    try:
        AnimationManager.animate_stop(message.chat.id, msg.message_id)
    except Exception:
        pass
    
    _cleanup_script_runtime(user_id, file_name)
    
    time.sleep(1)
    try:
        bot.edit_message_text(
            B(f"🛑 `{file_name}` stopped successfully."),
            message.chat.id, msg.message_id, parse_mode='Markdown',
            reply_markup=create_reply_keyboard_main_menu(user_id)
        )
    except Exception:
        pass

def _restart_script(message, user_id, file_name):
    _cleanup_script_runtime(user_id, file_name)
    time.sleep(1)
    _start_script(message, user_id, file_name)

def _delete_script(message, user_id, file_name):
    msg = bot.reply_to(message, B(f"🗑️ Deleting `{file_name}`..."))
    
    try:
        AnimationManager.animate_delete(message.chat.id, msg.message_id)
    except Exception:
        pass
    
    _cleanup_script_runtime(user_id, file_name, clear_log=True)
    remove_user_file_db(user_id, file_name)
    
    time.sleep(1)
    try:
        bot.edit_message_text(
            B(f"🗑️ `{file_name}` deleted successfully."),
            message.chat.id, msg.message_id, parse_mode='Markdown',
            reply_markup=create_reply_keyboard_main_menu(user_id)
        )
    except Exception:
        pass

def _show_logs(message, user_id, file_name):
    show_script_log(message, user_id, file_name)

# ================================
# 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 𝐊𝐄𝐘𝐁𝐎𝐀𝐑𝐃
# ================================
def create_database_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('👥 Users', callback_data='db_users'), 
               types.InlineKeyboardButton('📁 Files', callback_data='db_files'))
    markup.add(types.InlineKeyboardButton('🟢 Running Scripts', callback_data='db_running'), 
               types.InlineKeyboardButton('💳 Subscriptions', callback_data='db_subscriptions'))
    markup.add(types.InlineKeyboardButton('📤 Export Database', callback_data='db_export'), 
               types.InlineKeyboardButton('💾 Backup Database', callback_data='db_backup'))
    return markup

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

def _database_summary(call, kind):
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, 'Admin/owner only', show_alert=True)
        return
    queries = {'db_users': ('Users', 'SELECT COUNT(*) FROM active_users'), 
               'db_files': ('Files', 'SELECT COUNT(*) FROM user_files')}
    title, query = queries.get(kind, ('Database', 'SELECT 1'))
    try:
        with sqlite3.connect(DATABASE_PATH, timeout=30) as conn:
            value = conn.execute(query).fetchone()[0]
        bot.edit_message_text(B(f'🗄️ DATABASE MANAGER\n\n{title}: {value}'), 
                             call.message.chat.id, call.message.message_id, 
                             reply_markup=create_database_keyboard())
    except Exception as exc:
        error_logger.exception(f"Database summary failed: {exc}")
        bot.answer_callback_query(call.id, 'Database error', show_alert=True)

def _database_file_action(call, export=False):
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, 'Admin/owner only', show_alert=True)
        return
    path = None
    try:
        path = _safe_database_copy()
        with open(path, 'rb') as fh:
            bot.send_document(call.from_user.id, fh, 
                             caption=B('📤 Database export complete.'))
        bot.answer_callback_query(call.id, 'Database sent')
    except Exception as exc:
        error_logger.exception(f"Database export/backup failed: {exc}")
        bot.answer_callback_query(call.id, 'Database operation failed', show_alert=True)
    finally:
        if path:
            try:
                os.remove(path)
            except OSError:
                pass

# ================================
# 𝐍𝐎𝐓𝐈𝐅𝐈𝐂𝐀𝐓𝐈𝐎𝐍𝐒
# ================================
def send_restart_notification():
    bot_logger.info("📢 Sending restart notifications...")
    notification_text = B("""
🚨 *IMPORTANT ANNOUNCEMENT*

Bot is restarting for maintenance.

🔄 *Your scripts will be automatically restarted if:*
✅ You are Premium/Owner user

⏱️ *Bot will be back online in:*
• 30 seconds

Thank you for your patience! 😊
""")
    sent = 0
    for user_id in list(active_users):
        try:
            bot.send_message(user_id, notification_text, parse_mode='Markdown')
            sent += 1
        except Exception as e:
            error_logger.error(f"Failed to send notification to {user_id}: {e}")
        time.sleep(0.1)
    bot_logger.info(f"📤 Restart notifications: Sent={sent}")

# ================================
# 𝐂𝐋𝐄𝐀𝐍𝐔𝐏
# ================================
def cleanup():
    bot_logger.warning("🔴 Shutting down... Cleaning up")
    
    # Stop live logs
    cleanup_all_live_logs()
    
    # Kill all running scripts
    for script_key, script_info in list(bot_scripts.items()):
        try:
            kill_process_tree(script_info)
        except:
            pass
    
    # Close HTTPX client
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            loop.run_until_complete(http_client.close())
        else:
            asyncio.run(http_client.close())
    except:
        pass
    
    bot_logger.info("✅ Cleanup complete")

atexit.register(cleanup)

# ================================
# 𝐌𝐀𝐈𝐍
# ================================
if __name__ == '__main__':
    bot_logger.info("="*50)
    bot_logger.info("🚀 HOSTING BOT VERSION 5.0")
    bot_logger.info("🎨 PREMIUM ANIMATED PANEL")
    bot_logger.info("📊 Auto-Recovery System Enabled")
    bot_logger.info("📜 Advanced Logging System Enabled")
    bot_logger.info("🌐 Async HTTPX Client Enabled")
    bot_logger.info(f"👑 Owner ID: {OWNER_ID}")
    bot_logger.info(f"👥 Active Users: {len(active_users)}")
    bot_logger.info(f"📁 Total Files: {sum(len(files) for files in user_files.values())}")
    
    # Start Flask keep-alive
    keep_alive()
    
    # Start async worker
    worker_manager.start_worker()
    bot_logger.info("✅ Async worker started")
    
    # Run startup recovery
    threading.Thread(target=startup_recovery).start()
    
    # Start bot polling
    bot_logger.info("🤖 Starting bot polling...")
    
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=30)
        except requests.exceptions.ReadTimeout:
            bot_logger.warning("⚠️ Read Timeout. Restarting in 5s...")
            time.sleep(5)
        except requests.exceptions.ConnectionError as ce:
            error_logger.error(f"⚠️ Connection Error: {ce}. Retrying in 15s...")
            time.sleep(15)
        except Exception as e:
            error_logger.exception(f"💥 Unrecoverable error: {e}")
            bot_logger.info("🔄 Restarting in 30s due to critical error...")
            time.sleep(30)
        finally:
            bot_logger.warning("🔴 Polling stopped. Will restart if in loop...")
            time.sleep(1)