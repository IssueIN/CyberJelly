import socket

def send_data(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.sendall(message.encode())
        data = s.recv(1024)
    print(f"Received: {data.decode()}")

def main():
    target_ip = "35.180.128.146"
    target_port = 22 
    message = "l33t"

    send_data(target_ip, target_port, message)

if __name__ == "__main__":
    main()
