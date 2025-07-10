# 🚨 Project: Network Packet Sniffer with Alert System

## 🎯 Objective
Develop a real-time packet sniffer in Python that:
- Captures and logs live network traffic
- Detects suspicious activities (e.g., port scanning, flooding)
- Stores logs in SQLite
- Sends alerts based on activity thresholds
- Optionally visualizes traffic via a GUI using Matplotlib

---

## 🛠️ Tools & Technologies Used
- **Python 3.x**
- **Scapy** – for capturing and parsing packets
- **SQLite3** – for structured data logging
- **Matplotlib** – for optional real-time traffic graphs
- **smtplib / logging** – for alerts via email or logs

---

## 🧪 Core Features and Components

### 🔍 1. Packet Capturing
- Uses `scapy.sniff()` to capture packets on the active interface
- Extracts and logs:
  - Source IP, Destination IP
  - Source Port, Destination Port
  - Protocol, Packet Length, TCP Flags

### ⚠️ 2. Anomaly Detection
- Flags suspicious patterns like:
  - **Port Scanning**: Multiple ports hit from a single IP in a short time
  - **Flooding**: High packet rate from a single source
- Custom thresholds trigger alerts

### 🗃️ 3. Database Logging (SQLite)
- All captured packet summaries stored with timestamps
- Enables offline analysis and auditing

### 🚨 4. Alert System
- Sends an **email** or logs a warning when:
  - Abnormal IP activity is detected
  - Thresholds (packet count, scan attempts) are breached

### 📊 5. (Optional) GUI Visualization
- Displays live graph of:
  - Packets per second
  - Top talkers (frequent IPs)
- Built using `matplotlib` and `tkinter` (optional)

---

## 📁 Folder Structure
network_sniffer/
│
├── sniffer.py # Core packet sniffing logic
├── detector.py # Anomaly detection logic
├── database.py # SQLite operations
├── alert.py # Logging/email alert functions
├── visualizer.py # (Optional) GUI with Matplotlib
├── logs/ # Stores alert logs
├── traffic.db # SQLite traffic database
└── README.md # This file


---

## 🚀 How to Run

1. **Install dependencies**
```bash
pip install scapy matplotlib

sudo python3 sniffer.py
```

✅ Outcome
- Captured and logged real-time network traffic
- Detected suspicious behaviors and generated alerts
- Stored logs in a local SQLite database
- (Optionally) visualized traffic for analysis




