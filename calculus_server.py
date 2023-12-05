#!/usr/bin/env python3
import socket
from threading import Lock, Condition
from calculus.connection import Connection

HOST = "localhost"  # Standard hostname for loopback interface address (127.0.0.1) 
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

if __name__ == "__main__":
    """The arguments passed to socket() are constants used to specify the address family and socket type. AF_INET is the Internet address family for IPv4. 
        SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network. 
        We have used TCP because it is much more reliable than other protocols for this kind of client-server application"""
    lock = Lock()
    cond = Condition(lock=lock) # This condition object will be used by all connections
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    # limit the number of possible simultaneous connections to 5. No need to use Semaphores
    server.listen(5) # increasing the backlog set the maximum length of the queue for pending connections.
    print(f"Listening on {(HOST, PORT)}")
    while True:
        # Be carefull you will need to stop this code manually
        client_socket, addr = server.accept()
        
        connection = Connection(conn=client_socket, cond=cond, addr=addr)
        # Start the connection thread
        connection.start()
        print(f"Connected clients: {Connection._connected_clients}")
