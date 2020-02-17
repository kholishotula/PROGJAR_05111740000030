import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 1234)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    print('connected')

    # Send message
    message = 'requestedFile.txt'
    print(f"sending {message} as the requested file")
    sock.sendall(message.encode())

    # File to save the transferred message
    file = open('savedFile.txt', 'wb')

    # Receive the data
    while True:
        # receive data and write it to file
        data = sock.recv(1024)
        if data:
            file.write(data)
            data = sock.recv(1024)

            file.close()
            print('saved to savedFile.txt')
        else:
            break

finally:
    print('connection closed')
    sock.close()