import socket
import os
import json
import requests
import logging

TARGET_IP = "localhost"
TARGET_PORT = 1234

class DriveClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (TARGET_IP, TARGET_PORT)
        self.sock.connect(self.server_address)

    def proses(self, cmdline):
        cstring = cmdline.split(" ")
        try:
            command = cstring[0].strip()
            if (command == "upload"):
                self.sock.send(cmdline.encode())
            elif (command == "download"):
                self.sock.send(cmdline.encode())
            elif (command == "list"):
                self.sock.send(cmdline.encode())
            elif (command == "exit"):
                self.sock.send(cmdline.encode())
            else:
                return "ERRCMD"
            hasil = self.sock.recv(4096)
            print(hasil.decode())
        except:
            return "ERROR"

if __name__=="__main__":
    dc = DriveClient()
    while True:
        cmdline = input()
        if (cmdline=="exit"):
            dc.sock.close()
            print('Exit from program')
            break
        dc.proses(cmdline)
