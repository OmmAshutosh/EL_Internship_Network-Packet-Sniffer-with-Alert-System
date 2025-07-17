import os
from datetime import datetime

log_path = "logs/alerts.log"
os.makedirs("logs", exist_ok=True)

def log_alert(message):
    with open(log_path, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")
    print(message)
    