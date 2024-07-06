import socket
import pickle

# Client configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        # Get user input for the array
        input_array = input("Enter comma-separated numbers (or 'q' to quit): ")
        if input_array.lower() == 'q':
            break

        # Convert input to a list of integers
        try:
            array_to_send = [int(x.strip()) for x in input_array.split(',')]
        except ValueError:
            print("Invalid input. Please enter comma-separated numbers.")
            continue

        # Serialize the array
        data = pickle.dumps(array_to_send)

        # Send the serialized array to the server
        s.sendto(data, (HOST, PORT))
        print(f"Sent array to server: {array_to_send}")

        # Receive the processed array from the server
        response, _ = s.recvfrom(1024)

        # Deserialize the received data
        received_array = pickle.loads(response)
        print(f"Received processed array from server: {received_array}")

print("Client closed.")