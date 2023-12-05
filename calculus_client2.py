#!/usr/bin/env python3
import socket
from calculus_server import HOST, PORT 

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect_ex((HOST, PORT))
    
    # Receive and print the server's response
    welcome = client.recv(2048)
    print(welcome.decode())
    # Send response to the server (Asking to run all_negative function)
    client.sendall("10".encode())
    response = client.recv(2048)
    print(response.decode())
    # Sending arguments for all_negative function
    client.sendall("-37 -1 0 -7".encode())
    response = client.recv(2048)
    print(response.decode())
    
    # Asking to run least common multiple function
    client.sendall("15".encode())
    response = client.recv(2048)
    print(response.decode())
    # Sending arguments for least common multiple function
    client.sendall("64 47".encode())
    response = client.recv(2048)
    print(response.decode())
    
    # close the connection
    client.sendall("quit ".encode())
    client.close()

if __name__ == "__main__":
    # Try to run calculus_client1.py and calculus_client2.py simultaneously to ensure that the server is effectively handling multiple connections
    # If you are using a linux machine, try to run them in the terminal: python3 calculus_client1.py && python3 calculus_client2.py
    start_client()
