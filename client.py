import socket

def create_socket_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket

def send_message(client_socket, message):
    client_socket.sendall(message.encode())

def receive_message(client_socket):
    response = client_socket.recv(1024)
    return response.decode()

if __name__ == "__main__":
    host = 'localhost'
    port = 65432

    client_socket = create_socket_client(host, port)
    try:
        send_message(client_socket, "Hello, Server!")
        response = receive_message(client_socket)
        print(f"Received from server: {response}")
    finally:
        client_socket.close()