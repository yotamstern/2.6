import socket


def send_request(request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))
    client_socket.send(request.encode())
    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")
    client_socket.close()


if __name__ == "__main__":
    while True:
        user_input = input("Enter a request (TIME, NAME, RAND, EXIT): ").strip().upper()

        if user_input == "EXIT":
            send_request(user_input)
            break

        if len(user_input) == 4:
            send_request(user_input)
        else:
            print("Invalid request. Please enter a 4-character request.")
