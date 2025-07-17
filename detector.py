import time
from collections import defaultdict

# Keep track of how many times each IP hits a port
ip_port_count = defaultdict(list)

def detect_anomaly(src_ip, dst_port):
    current_time = time.time()
    ip_port_count[src_ip] = [t for t in ip_port_count[src_ip] if current_time - t < 10]
    ip_port_count[src_ip].append(current_time)

    # If more than 20 packets in 10 seconds, treat as a potential port scan
    if len(ip_port_count[src_ip]) > 20:
        return True
    return False
