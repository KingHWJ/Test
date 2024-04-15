import socket
import threading

def handle_client(client_socket, address):
    while True:
        # 接收客户端消息
        message = client_socket.recv(1024).decode()
        if not message:
            print(f"Connection with {address} closed.")
            break
        print(f"Received message from {address}: {message}")

def main():
    host = '0.0.0.0'  # 允许任何 IP 地址连接
    port = 12345  # 端口号

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # 最大连接数

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    main()
