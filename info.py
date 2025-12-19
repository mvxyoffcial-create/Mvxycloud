import re
from typing import Set, Optional, List, Dict
from Script import script 

# 🚀 Bot Session and Token Information
SESSION = 'Webavbot'  

API_ID = 36282056  
API_HASH = '3a948acece533f362b4c90b2b3c14b60'  
BOT_TOKEN = '8171094813:AAHf6NHlgi6pRku_zS-XqdoQmJWrpco21-k'  

# 👑 Channels & Logs
BIN_CHANNEL = -1003285174560  
LOG_CHANNEL = -1003285174560  
PREMIUM_LOGS = -1003285174560  
VERIFIED_LOG = -1003285174560  
SUPPORT_GROUP = -1003285174560

# Admin and Auth Channel IDs
ADMINS = [8312532076]  
AUTH_CHANNEL = [-1003285174560]  

# Usernames
OWNER_USERNAME = 'Zeroboy216'  
BOT_USERNAME = 'Filmzihdjdhoster_bot'  

# 🔗 Channel & Support Links
CHANNEL = 'https://t.me/AV_BOTz_UPDATE'  
SUPPORT = 'https://t.me/AV_SUPPORT_GROUP'  
HOW_TO_VERIFY = 'https://t.me/'  
HOW_TO_OPEN = 'https://t.me/'  

# ✅ Feature Toggles (Optimized for Website Hosting)
VERIFY = False           # 🟢 Set to False so links NEVER require verification
FSUB = False             # 🟢 Set to False so your website users aren't blocked by Telegram
ENABLE_LIMIT = False     # 🟢 Set to False for unlimited downloads/views
BATCH_VERIFY = False     
IS_SHORTLINK = False     # 🟢 Set to False for direct, permanent links
MAINTENANCE_MODE = False
PROTECT_CONTENT = False  # 🟢 Set to False to allow video players to buffer/stream
PUBLIC_FILE_STORE = True 
BATCH_PROTECT_CONTENT = False

# 🔗 Shortlink Configuration (Disabled)
SHORTLINK_URL = 'techvjlink.site'  
SHORTLINK_API = 'd73e70a35dc3877fa14afbf51fa8ec312c94780c'  

# 💾 MongoDB Connection (Must remain the same for link permanence)
DB_URL = "mongodb+srv://Mvzydatabase_db:venura8907@cluster0.sphzemi.mongodb.net/?appName=Cluster0"  
DB_NAME = "cluster0"  

# 📸 All Media
QR_CODE = 'https://graph.org/file/6afb4093d5ec5c4176979.jpg'  
VERIFY_IMG = "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg"  
AUTH_PICS = 'https://envs.sh/AwV.jpg'  
PICS = 'https://envs.sh/_pM.jpg'  
FILE_PIC = 'https://i.ibb.co/bj4My0bW/photo-2025-07-21-02-15-21-7529360175656861700.jpg'  

# 📝 File Captions
FILE_CAPTION = script.CAPTION  
BATCH_FILE_CAPTION = script.CAPTION  
CHANNEL_FILE_CAPTION = script.CAPTION  

# ⏱️ Time & Rate Limit Settings (Max Permanence)
PING_INTERVAL = 300       # Keep server alive every 5 minutes
SLEEP_THRESHOLD = 120     # Prevent connection drops
RATE_LIMIT_TIMEOUT = 0    # No waiting time
MAX_FILES = 0             # Unlimited
VERIFY_EXPIRE = 999999    # 🟢 Set to 100+ years (Permanent)

# ⚙️ Worker Configuration (High Traffic Ready)
WORKERS = 200             # Increased to handle many website viewers at once
MULTI_CLIENT = True       

# 🔧 App Configuration
name = 'avbotz'  
ON_HEROKU = False
APP_NAME = None

# 🌐 Server Settings (Fixed for Secure Hosting)
PORT = 2626  
NO_PORT = True  
HAS_SSL = True            # 🟢 Required for embedding in HTTPS websites
BIND_ADDRESS = "0.0.0.0"  
FQDN = "mvxycloud.koyeb.app"  
PORT_SEGMENT = ""  
PROTOCOL = "https"  
URL = f"{PROTOCOL}://{FQDN}/"
