"""Global constants and configuration values."""

from pathlib import Path

# Application Paths
APP_ROOT = Path(__file__).parent.parent
DATA_DIR = APP_ROOT / "data"
LOGS_DIR = APP_ROOT / "logs"
DB_DIR = DATA_DIR / "database"
TEMP_DIR = DATA_DIR / "temp"

# Ensure directories exist
for directory in [DATA_DIR, LOGS_DIR, DB_DIR, TEMP_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Database
DATABASE_URL = f"sqlite:///{DB_DIR / 'pc_optimizer.db'}"
DATABASE_POOL_SIZE = 10
DATABASE_POOL_TIMEOUT = 30

# Monitoring
MONITOR_UPDATE_INTERVAL = 1.0  # seconds
METRICS_BATCH_INTERVAL = 60  # seconds (batch write to DB)
METRICS_RETENTION_DAYS = 30  # Keep 30 days of metrics

# CPU
CPU_ALERT_THRESHOLD = 90.0  # percentage
CPU_WARNING_THRESHOLD = 70.0  # percentage

# Memory
RAM_ALERT_THRESHOLD = 90.0  # percentage
RAM_WARNING_THRESHOLD = 75.0  # percentage
MEMORY_LEAK_THRESHOLD = 500.0  # MB increase over 1 hour

# Temperature
TEMPERATURE_CRITICAL_THRESHOLD = 95.0  # Celsius
TEMPERATURE_WARNING_THRESHOLD = 80.0  # Celsius
THERMAL_THROTTLING_CHECK_INTERVAL = 5.0  # seconds

# Battery
BATTERY_CRITICAL_THRESHOLD = 15.0  # percentage
BATTERY_WARNING_THRESHOLD = 30.0  # percentage

# Storage
STORAGE_ALERT_THRESHOLD = 85.0  # percentage
STORAGE_WARNING_THRESHOLD = 70.0  # percentage

# Network
NETWORK_STATS_INTERVAL = 2.0  # seconds

# GPU
GPU_ALERT_THRESHOLD = 90.0  # percentage
GPU_WARNING_THRESHOLD = 75.0  # percentage
GPU_MEMORY_ALERT_THRESHOLD = 85.0  # percentage

# UI
UI_REFRESH_INTERVAL = 1000  # milliseconds
UI_ANIMATION_DURATION = 300  # milliseconds
UI_DEFAULT_THEME = "dark"

# Thread Pool
THREAD_POOL_SIZE = 4
THREAD_POOL_TIMEOUT = 300  # seconds

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}"
LOG_ROTATION = "500 MB"
LOG_RETENTION = "30 days"

# Cache
CACHE_MAX_SIZE = 1000  # items
CACHE_TTL = 3600  # seconds (1 hour)

# Gaming Mode
GAMING_MODE_MIN_FREE_RAM = 2048  # MB
GAMING_MODE_CPU_THRESHOLD = 10  # percentage

# System
SYSTEM_INFO_REFRESH_INTERVAL = 3600  # seconds (1 hour)

# Process Management
PROCESS_HISTORY_LIMIT = 10000  # Maximum processes to track
PROCESS_UPDATE_INTERVAL = 2.0  # seconds

# Startup Programs
STARTUP_IMPACT_THRESHOLD = 5.0  # percentage CPU impact

# Recommendations
RECOMMENDATION_CHECK_INTERVAL = 300  # seconds (5 minutes)

# Warnings and Confirmations
CONFIRM_KILL_PROCESS = True
CONFIRM_DELETE_FILE = True
CONFIRM_ENABLE_GAMING_MODE = True

# Safe Processes (don't kill without extra confirmation)
SYSTEM_PROCESSES = {
    "svchost.exe",
    "csrss.exe",
    "services.exe",
    "lsass.exe",
    "winlogon.exe",
    "explorer.exe",
    "dwm.exe",
    "taskhost.exe",
    "wininit.exe",
    "System",
    "Registry",
    "smss.exe",
}
