import re
from typing import Set, Optional, List, Dict
from Script import script  # Custom script file with caption & other settings

# 🚀 Bot Session and Token Information
SESSION = 'Webavbot'  # Pyrogram client session name

API_ID = 36282056  # Telegram API ID
API_HASH = '3a948acece533f362b4c90b2b3c14b60'  # Telegram API Hash
BOT_TOKEN = '8171094813:AAHf6NHlgi6pRku_zS-XqdoQmJWrpco21-k'  # Telegram Bot Token

# 👑 Channels & Logs
BIN_CHANNEL = -1003285174560  # File storage channel
LOG_CHANNEL = -1003285174560  # General log channel
PREMIUM_LOGS = -1003285174560  # Premium user actions log
VERIFIED_LOG = -1003285174560  # Verified user actions log
SUPPORT_GROUP = -1003285174560

# Admin and Auth Channel IDs
ADMINS = [8312532076]  # List of admin user IDs
AUTH_CHANNEL = [-1003285174560]  # Allowed channels for authorization

# Usernames (without @)
OWNER_USERNAME = 'Zeroboy216'  # Owner's username
BOT_USERNAME = 'Filmzihdjdhoster_bot'  # Bot's username

# 🔗 Channel & Support Links
CHANNEL = 'https://t.me/AV_BOTz_UPDATE'  # Updates channel
SUPPORT = 'https://t.me/AV_SUPPORT_GROUP'  # Support group
HOW_TO_VERIFY = 'https://t.me/'  # Verification guide link
HOW_TO_OPEN = 'https://t.me/'  # File access guide link

# ✅ Feature Toggles
VERIFY = False  # Enable user verification
FSUB = True  # Force Subscribe feature
ENABLE_LIMIT = True  # Enable file limits
BATCH_VERIFY = False  # Verify files in batch
IS_SHORTLINK = False  # Enable channel shortlink creation
MAINTENANCE_MODE = False  # Put bot in maintenance mode
PROTECT_CONTENT = False  # Enable content protection
PUBLIC_FILE_STORE = True  # Public or private file visibility
BATCH_PROTECT_CONTENT = False  # Batch file protection

# 🔗 Shortlink Configuration
SHORTLINK_URL = 'techvjlink.site'  # Shortener site
SHORTLINK_API = 'd73e70a35dc3877fa14afbf51fa8ec312c94780c'  # API key for shortlink

# 💾 MongoDB Connection Information
DB_URL = "mongodb+srv://Hdmoviehutcloud:zero8907@cluster0.sgcp0am.mongodb.net/?appName=Cluster0"  # MongoDB connection URI
DB_NAME = "cluster0"  # MongoDB database name

# 📸 All Media (Images)
QR_CODE = 'https://graph.org/file/6afb4093d5ec5c4176979.jpg'  # QR Code image
VERIFY_IMG = "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg"  # Verify success image
AUTH_PICS = 'https://envs.sh/AwV.jpg'  # Auth step image
PICS = 'https://envs.sh/_pM.jpg'  # Default info image
FILE_PIC = 'https://i.ibb.co/bj4My0bW/photo-2025-07-21-02-15-21-7529360175656861700.jpg'  # File image

# 📝 File Captions
FILE_CAPTION = script.CAPTION  # Caption for single file
BATCH_FILE_CAPTION = script.CAPTION  # Caption for batch files
CHANNEL_FILE_CAPTION = script.CAPTION  # Caption for channel posts

# ⏱️ Time & Rate Limit Settings
PING_INTERVAL = 1200  # Ping interval in seconds (20 minutes)
SLEEP_THRESHOLD = 60  # Threshold for sleep delay
RATE_LIMIT_TIMEOUT = 600  # Rate limit time (10 mins)
MAX_FILES = 5  # Max files allowed per user
VERIFY_EXPIRE = 60  # Time (in hours) after which verification expires

# ⚙️ Worker Configuration
WORKERS = 50  # Number of async workers
MULTI_CLIENT = True  # Enable multi-client handling (if needed)

# 🔧 App/Heroku Configuration
name = 'avbotz'  # Project name
ON_HEROKU = False
APP_NAME = None

# 🌐 Server Settings (✅ Fixed HTTPS)
PORT = 2626  # Port for web server
NO_PORT = True  # Disable port in URL
HAS_SSL = True  # ✅ Enable SSL (Fixes secure download issue)
BIND_ADDRESS = "127.0.0.1"  # Server bind address
FQDN = "hdmoviehutcloud.koyeb.app"  # Full domain name
PORT_SEGMENT = ""  # No port in URL
PROTOCOL = "https"  # ✅ Use HTTPS instead of HTTP
URL = f"{PROTOCOL}://{FQDN}/"  # Final generated base URL with trailing slash
