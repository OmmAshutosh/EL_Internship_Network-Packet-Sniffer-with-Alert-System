import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect('traffic.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS packets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            src_ip TEXT,
            dst_ip TEXT,
            src_port INTEGER,
            dst_port INTEGER,
            flags TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_packet(src_ip, dst_ip, src_port, dst_port, flags):
    conn = sqlite3.connect('traffic.db')
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO packets (timestamp, src_ip, dst_ip, src_port, dst_port, flags)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, src_ip, dst_ip, src_port, dst_port, flags))
    conn.commit()
    conn.close()
    