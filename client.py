import socket

def main():
    host = '127.0.0.1'  # 服务器 IP 地址
    port = 12345  # 服务器端口号

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter message: ")
        client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    main()
