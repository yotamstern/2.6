import socket
import datetime
import random

IP = '0.0.0.0'
PORT = 20003
QUEUE_SIZE = 1
MAX_PACKET = 2


def handle_request(request):
    if request == "TIME":
        return str(datetime.datetime.now())
    elif request == "NAME":
        return "YSServer"
    elif request == "RAND":
        return str(random.randint(1, 10))
    elif request == "EXIT":
        return "Goodbye"
    else:
        return "Invalid request"


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(QUEUE_SIZE)
    print("Server is ready to receive requests.")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        while True:
            request = client_socket.recv(MAX_PACKET)
            if not request:
                break

            response = handle_request(request)
            client_socket.send(response.encode())

            if request == "EXIT":
                break

        print(f"Connection with {client_address} closed.")
        client_socket.close()


if __name__ == "__main__":
    start_server()
