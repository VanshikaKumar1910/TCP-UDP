import socket

def main():
    # Server configuration (same as in the server script)
    host = '127.0.0.1'  # The server's hostname or IP address
    port = 12345        # The port used by the server

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        while True:
            # Get user input
            user_input = input("Enter an integer (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break

            try:
                # Convert input to integer
                int_to_send = int(user_input)

                # Convert integer to bytes
                data = int_to_send.to_bytes(4, byteorder='big')

                # Send data to server
                client_socket.sendto(data, (host, port))
                print(f"Sent integer to server: {int_to_send}")

                # Receive response from server
                response, _ = client_socket.recvfrom(1024)
                
                # Convert received bytes to integer
                result = int.from_bytes(response, byteorder='big')
                print(f"Received result from server: {result}")

            except ValueError:
                print("Invalid input. Please enter an integer.")

    print("Client closed.")

if __name__ == "__main__":
    main()