import socket
import sys

s = socket.socket()
server_address = ('127.0.0.1', 1234)
s.bind(server_address)
s.listen(1)
print(f"server with ip {server_address} is ON")

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = s.accept()
    print(f"get a connection from {client_address}")

    # Receive the message
    requested = connection.recv(1024)
    print(f"The requested file is {requested.decode()}")

    # Read the file and send it
    file = open(requested.decode(), 'rb')
    while True:
        data = file.read(1024)
        if data:
            print(f"sending {data} from {requested.decode()}")
            connection.send(data)
        else:
            break

    # Clean up the connection
    connection.close()
    print('client has been disconnected')