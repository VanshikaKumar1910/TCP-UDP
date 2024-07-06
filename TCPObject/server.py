import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(),1234))

s.listen(5)
print("server is listening")

client_socket,address=s.accept()

print(f"connection from {address} has been established")

message="welcome to the server"
client_socket.send(message.encode('utf-8'))

client_socket.close()