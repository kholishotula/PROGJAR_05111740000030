import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
# Getting the ip address of computer
name = socket.gethostname()
ip = socket.gethostbyname(name)
# PORT 31000
server_address = (ip, 31000)
# PORT 31001
# server_address = (ip, 31001)
# PORT 31002
# server_address = (ip, 31002)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(32)
        print(f"received {data}")
        if data:
            print("sending back data")
            connection.sendall(data)
        else:
           break
    # Clean up the connection
    connection.close()