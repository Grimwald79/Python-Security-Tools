import socket
from datetime import datetime

def scan_target(target, start_port, end_port):
    """
    Scans a target IP for open ports within a specified range.
    """
    try:
        # Resolve hostname to IPv4
        target_ip = socket.gethostbyname(target)
        print(f"[*] Starting scan on host: {target_ip}")
        print(f"[*] Time started: {datetime.now()}")
        print("-" * 50)

        for port in range(start_port, end_port + 1):
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) # Wait 1 second max
            
            # Returns 0 if connection is successful
            result = s.connect_ex((target_ip, port)) 
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            s.close()
            
    except socket.gaierror:
        print("\n[!] Hostname could not be resolved.")
    except socket.error:
        print("\n[!] Could not connect to server.")
    except KeyboardInterrupt:
        print("\n[!] Exiting Program.")

if __name__ == "__main__":
    # You can change 'scanme.nmap.org' to a local IP like '192.168.1.1' for testing
    target_host = input("Enter target to scan (e.g., scanme.nmap.org): ")
    scan_target(target_host, 20, 100)
    print("-" * 50)
    print("Scan complete.")
