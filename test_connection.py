import socket

def scan_host(ip, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except Exception as e:
        print(e)

def main():
    target_ip = "35.180.128.146"  # Replace with the IP you are testing
    target_ports = [22, 80, 443]  # Common ports to test

    for port in target_ports:
        scan_host(target_ip, port, 1.5)

if __name__ == "__main__":
    main()
