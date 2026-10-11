import socket
import sys

# ---------------------------------------------------------
# Basit Port Tarayıcı (Simple Port Scanner)
# Geliştirici: cyber-ybs-99
# İletişim / Sosyal Medya: @siber_yolcu_01
# ---------------------------------------------------------

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} AÇIK!")
        sock.close()
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Kullanım: python scanner.py <IP> <Port>")
    else:
        scan_port(sys.argv[1], int(sys.argv[2]))
