import socket

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455
    
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    
    print(f"Server is listening on {host}:{port}")
    
    while True:
        data, addr = server.recvfrom(1024)
        decoded_data = data.decode("utf-8")
        print(f"Received from {addr}: {decoded_data}")
        
        if decoded_data == "!EXIT":
            print("Client requested to exit. Closing connection.")
            break
        
        response = decoded_data.upper()
        server.sendto(response.encode("utf-8"), addr)
    
    server.close()
    print("Server shut down")