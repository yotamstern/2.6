import socket
import datetime
import random


def handle_request(request):
    if request == "TIME":
        response_data = str(datetime.datetime.now())
    elif request == "NAME":
        response_data = "MyServer"
    elif request == "RAND":
        response_data = str(random.randint(1, 10))
    elif request == "EXIT":
        response_data = "Goodbye"
    else:
        response_data = "Invalid request"

    return f"{request}\n{response_data}"


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(1)
    print("Server is ready to receive requests.")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        while True:
            request = client_socket.recv(1024).decode()
            assert len(request) == 4
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
