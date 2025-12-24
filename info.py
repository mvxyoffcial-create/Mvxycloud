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

# ✅ PERMANENT LINK CONFIGURATION - NO EXPIRATION EVER
VERIFY = False                    # 🟢 No verification required
FSUB = False                      # 🟢 No force subscribe
ENABLE_LIMIT = False              # 🟢 Unlimited downloads
BATCH_VERIFY = False              # 🟢 No batch verification
IS_SHORTLINK = False              # 🟢 Direct permanent links only
MAINTENANCE_MODE = False          # 🟢 Always available
PROTECT_CONTENT = False           # 🟢 Allow streaming/buffering
PUBLIC_FILE_STORE = True          # 🟢 Public access enabled
BATCH_PROTECT_CONTENT = False     # 🟢 No content protection
DELETE_AFTER_DOWNLOAD = False     # 🟢 Never delete files
AUTO_DELETE = False               # 🟢 Keep files forever
LINK_EXPIRY = False               # 🟢 Links never expire

# 🔗 Shortlink Configuration (Completely Disabled)
SHORTLINK_URL = ''                # Empty = disabled
SHORTLINK_API = ''                # Empty = disabled
USE_SHORTLINK = False             # Force disabled

# 💾 MongoDB Connection (CRITICAL - Don't change for permanent links)
DB_URL = "mongodb+srv://Mvzydatabase_db:venura8907@cluster0.sphzemi.mongodb.net/?appName=Cluster0"  
DB_NAME = "cluster0"
DB_COLLECTION = "files"           # Permanent storage collection

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

# ⏱️ ULTRA-FAST & PERMANENT SETTINGS
PING_INTERVAL = 180               # Keep alive every 3 minutes
SLEEP_THRESHOLD = 60              # Faster response time
RATE_LIMIT_TIMEOUT = 0            # 🟢 No rate limiting
MAX_FILES = 0                     # 🟢 Unlimited files per request
VERIFY_EXPIRE = 999999999         # 🟢 ~31 years (effectively permanent)
SESSION_TIMEOUT = 0               # 🟢 Sessions never timeout
CACHE_TIME = 86400                # Cache for 24 hours for speed
MAX_RETRIES = 10                  # More retry attempts
RETRY_DELAY = 1                   # Fast retry

# 🚀 SPEED OPTIMIZATION SETTINGS
CHUNK_SIZE = 524288               # 512KB chunks for faster streaming (increased from typical 256KB)
MAX_CONCURRENT_TRANSMISSIONS = 50 # Handle 50 simultaneous downloads
BUFFER_SIZE = 1048576             # 1MB buffer for smoother streaming
STREAM_TIMEOUT = 300              # 5 minute timeout per stream chunk
CONNECTION_POOL_SIZE = 200        # Large connection pool
ENABLE_CACHING = True             # Cache frequently accessed files
COMPRESSION = False               # No compression for speed (pre-compressed files recommended)

# ⚙️ WORKER CONFIGURATION (Maximum Performance)
WORKERS = 500                     # 🟢 Increased to 500 for heavy traffic
MULTI_CLIENT = True               # 🟢 Multiple client support
MAX_WORKERS_PER_FILE = 10         # Allow 10 workers per file download
WORKER_TIMEOUT = 600              # 10 minute worker timeout

# 🔧 App Configuration
name = 'avbotz'  
ON_HEROKU = False
APP_NAME = None

# 🌐 SERVER SETTINGS (Optimized for HTTPS Websites)
PORT = 2626  
NO_PORT = True  
HAS_SSL = True                    # 🟢 Required for HTTPS embedding
BIND_ADDRESS = "0.0.0.0"          # Listen on all interfaces
FQDN = "mvxycloud.koyeb.app"      # Your domain
PORT_SEGMENT = ""  
PROTOCOL = "https"  
URL = f"{PROTOCOL}://{FQDN}/"

# 🔐 SECURITY SETTINGS (While keeping links permanent)
ALLOW_CORS = True                 # Allow website embedding
CORS_ORIGINS = ["*"]              # Allow all origins (or specify your website domain)
MAX_REQUEST_SIZE = 0              # Unlimited request size
RATE_LIMIT = False                # No rate limiting for speed

# 📊 MONITORING & LOGGING (Optional but recommended)
ENABLE_STATS = True               # Track download statistics
LOG_DOWNLOADS = True              # Log all downloads
ANALYTICS_ENABLED = False         # Disable for privacy/speed

# 🎯 FILE STORAGE OPTIMIZATION
PERMANENT_STORAGE = True          # Never auto-delete files
FILE_INDEX_CACHE = True           # Cache file index for instant lookup
PRELOAD_METADATA = True           # Preload file metadata for speed
LAZY_LOADING = False              # Load everything immediately

# 🔄 BACKUP & REDUNDANCY
AUTO_BACKUP = True                # Backup file references
BACKUP_INTERVAL = 86400           # Daily backup
REDUNDANT_STORAGE = True          # Store file IDs redundantly

# 📱 WEBSITE EMBEDDING OPTIMIZATION
EMBED_FRIENDLY = True             # Optimize for iframe embedding
DIRECT_DOWNLOAD = True            # Allow direct downloads
RANGE_REQUESTS = True             # Support partial content (HTTP 206) for video seeking
ACCEPT_RANGES = True              # Enable range header support

# 🎥 VIDEO STREAMING OPTIMIZATION
VIDEO_BUFFER_SIZE = 2097152       # 2MB buffer for smooth video playback
ADAPTIVE_BITRATE = False          # Disable for maximum speed
PREFETCH_CHUNKS = 3               # Prefetch 3 chunks ahead

# ⚡ PERFORMANCE MONITORING
ENABLE_PERFORMANCE_LOGS = True    
LOG_SLOW_REQUESTS = True          
SLOW_REQUEST_THRESHOLD = 5        # Log requests taking >5 seconds

# 🛡️ ERROR HANDLING
GRACEFUL_SHUTDOWN = True          
AUTO_RESTART_ON_ERROR = True      
MAX_ERROR_RETRIES = 100           # Keep trying

# 🌍 CDN & CACHING HEADERS
ENABLE_CDN_HEADERS = True         
CACHE_CONTROL = "public, max-age=31536000"  # Cache for 1 year
ETAG_ENABLED = True               # Enable ETags for caching

# 💡 ADDITIONAL OPTIMIZATIONS
KEEP_ALIVE = True                 # Keep connections alive
TCP_NODELAY = True                # Disable Nagle's algorithm for lower latency
SEND_FILE_MAX_AGE = 31536000      # Cache static files for 1 year
