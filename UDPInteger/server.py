import socket

def main():
    # Server configuration
    host = '127.0.0.1'  # localhost
    port = 12345        # Choose a port number

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        # Bind the socket to a specific address and port
        server_socket.bind((host, port))
        print(f"UDP server is listening on {host}:{port}")

        while True:
            # Wait for a connection
            print("Waiting for data...")
            data, client_address = server_socket.recvfrom(1024)
            
            # Convert received bytes to integer
            received_int = int.from_bytes(data, byteorder='big')
            print(f"Received integer from {client_address}: {received_int}")

            # Process the integer (multiply by 2)
            result = received_int

            # Convert the result back to bytes
            response = result.to_bytes(4, byteorder='big')

            # Send the result back to the client
            server_socket.sendto(response, client_address)
            print(f"Sent result back to client: {result}")

if __name__ == "__main__":
    main()