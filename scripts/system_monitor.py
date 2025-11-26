import psutil
from datetime import datetime

CPU_THRESHOLD = 80                    # %
MEMORY_THRESHOLD = 80                 # %
DISK_THRESHOLD = 85                   # %

LOG_FILE = "/home/balu/projects/python-automation-toolkit/logs/system_health.log"

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} | {message}\n")

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    log(f"STATUS | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

    if cpu > CPU_THRESHOLD:
        log(f"ALERT | High CPU Usage: {cpu}%")
    if memory > MEMORY_THRESHOLD:
        log(f"ALERT | High Memory Usage: {memory}%")
    if disk > DISK_THRESHOLD:
        log(f"ALERT | Disk Space Usage High: {disk}%")

if __name__ == "__main__":
    check_system_health()
    print("System health check completed. See logs/system_health.log")
