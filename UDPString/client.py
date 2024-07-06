import socket

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455
    addr = (host, port)
    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"Connected to server at {host}:{port}")
    
    while True:
        data = input("Enter a word (or '!EXIT' to quit): ")
        
        encoded_data = data.encode("utf-8")
        client.sendto(encoded_data, addr)
        
        if data == "!EXIT":
            print("Disconnected from the server")
            break
        
        response, _ = client.recvfrom(1024)
        decoded_response = response.decode("utf-8")
        print(f"Server: {decoded_response}")
    
    client.close()