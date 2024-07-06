import socket

try:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    server_address = (socket.gethostname(), 1234)
    print(f"Attempting to connect to {server_address}")
    s.connect(server_address)
    print("Connected successfully")

    full_msg = b''  # Use bytes instead of string
    while True:
        msg = s.recv(1024)
        if len(msg) == 0:
            break
        full_msg += msg  # Append bytes directly

    print("Received message:")
    print(full_msg.decode("utf-8"))  # Decode the full message at the end

except ConnectionRefusedError:
    print("Connection was refused. Make sure the server is running.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    s.close()
    print("Connection closed")