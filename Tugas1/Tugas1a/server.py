import socket
import sys

s = socket.socket()
# server 1
server_address = ('127.0.0.1', 31000)
# server 2
# server_address = ('127.0.0.1', 31001)
# server 3
# server_address = ('127.0.0.1', 31002)
s.bind(server_address)
s.listen(1)
print(f"server with ip {server_address} is ON")

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = s.accept()
    print(f"get a connection from {client_address}")

    # File to save the transferred message
    file = open('Tugas1a/getFile.txt', 'wb')

    # Receive the data in small chunks and retransmit it
    while True:
        # receive data and write it to file
        data = connection.recv(1024)
        if data:
            file.write(data)
            data = connection.recv(1024)

            file.close()
            print('saved to getFile.txt')
        else:
            break

    # Clean up the connection
    connection.close()
    print('client has been disconnected')