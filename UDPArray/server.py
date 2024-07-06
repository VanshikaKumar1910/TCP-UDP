import socket
import pickle

# Server configuration
HOST = '127.0.0.1'  # localhost
PORT = 65432        # Port to listen on

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        # Receive data from the client
        data, addr = s.recvfrom(1024)
        
        # Deserialize the received data
        received_array = pickle.loads(data)
        print(f"Received array from {addr}: {received_array}")

        # Process the array (in this example, we'll just reverse it)
        processed_array = received_array[::-1]

        # Serialize the processed array
        response = pickle.dumps(processed_array)

        # Send the processed array back to the client
        s.sendto(response, addr)
        print(f"Sent processed array to {addr}: {processed_array}")