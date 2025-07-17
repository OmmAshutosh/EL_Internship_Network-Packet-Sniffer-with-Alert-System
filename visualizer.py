import sqlite3
import matplotlib.pyplot as plt
from collections import Counter

def fetch_data():
    conn = sqlite3.connect("traffic.db")
    cursor = conn.cursor()
    cursor.execute("SELECT dst_port FROM packets")
    ports = [row[0] for row in cursor.fetchall()]
    conn.close()
    return ports

ports = fetch_data()
count = Counter(ports)

plt.figure(figsize=(10, 5))
plt.bar(count.keys(), count.values())
plt.xlabel("Destination Ports")
plt.ylabel("Packet Count")
plt.title("Traffic Summary by Destination Port")
plt.grid(True)
plt.show()
