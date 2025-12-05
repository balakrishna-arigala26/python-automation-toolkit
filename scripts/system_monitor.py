import psutil
import time
from datetime import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                        "logs/system_health.log")

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 90


def log(message: str):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {message}\n")


def check_health():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    log(f"STATUS | CPU: {cpu}% | Memory: {mem}% | Disk: {disk}%")

    if cpu > CPU_THRESHOLD:
        log(f"ALERT | High CPU Usage: {cpu}%")
    if mem > MEM_THRESHOLD:
        log(f"ALERT | High Memory Usage: {mem}%")
    if disk > DISK_THRESHOLD:
        log(f"ALERT | High Disk Usage: {disk}%")


def run(interval: int = 10):
    """Run system monitor continuously at given interval (seconds)."""
    print(f"🔍 System monitor started (interval = {interval}s). Press CTRL + C to stop.")
    try:
        while True:
            check_health()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user.")
