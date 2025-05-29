import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = sys.argv[1]
port = sys.argv[2]

def scan_port(ip, port):
    try:
        sock.connect((ip, int(port)))
        print(f"Port {port} is open on {ip}")
        return True
    except socket.error:
        print(f"Port {port} is closed on {ip}")
        return False
    finally:
        sock.close()

scan_port(ip, port)