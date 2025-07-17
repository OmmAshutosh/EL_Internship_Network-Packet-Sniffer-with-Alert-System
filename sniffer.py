from datetime import datetime

from scapy.all import IP, TCP, sniff

from alert import log_alert
from database import init_db, log_packet
from detector import detect_anomaly

init_db()
