import socket
import threading
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def receive_messages(sock, username):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            message = data.decode()
            if message.startswith("USERNAME:"):
                continue  # Ignore username messages
            print(f"\r{' ' * 50}\r{message}")
            print(f"{username}: ", end="", flush=True)
        except:
            pass

def send_messages(sock, target_address, username):
    while True:
        message = input(f"{username}: ")
        full_message = f"{username}: {message}"
        sock.sendto(full_message.encode(), target_address)

def main():
    your_port = int(input("Enter your port number: "))
    target_ip = input("Enter target IP address: ")
    target_port = int(input("Enter target port number: "))
    username = input("Enter your username: ")

    host = '0.0.0.0'  # Listen on all available interfaces

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, your_port))

    print(f"Chat application started. Listening on port {your_port}")
    print(f"Sending messages to {target_ip}:{target_port}")
    print(f"Your username: {username}")
    print("Type your messages and press Enter to send. Press Ctrl+C to exit.")
    print("-" * 50)

    # Send username to the other user
    sock.sendto(f"USERNAME:{username}".encode(), (target_ip, target_port))

    receive_thread = threading.Thread(target=receive_messages, args=(sock, username))
    send_thread = threading.Thread(target=send_messages, args=(sock, (target_ip, target_port), username))

    receive_thread.daemon = True
    send_thread.daemon = True

    receive_thread.start()
    send_thread.start()

    try:
        send_thread.join()
    except KeyboardInterrupt:
        print("\nExiting chat application...")
        sys.exit(0)

if __name__ == "__main__":
    main()