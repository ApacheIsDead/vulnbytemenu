# vulnbytemenu

# This application will scan websites for common vulnerabilities using nmap and the respective scripts!

# Copyright 2018 by Allek Hall
# For Fair Use under GNU
# We Are Not Responsible for how you use this tool

import subprocess
import os
import smtplib
import time

print("VULNBYTE TOOLKIT\n\n")
# Below the code starts


selection_item = raw_input("[1] - Anonymous Front Page Login Scan!\n[2] - Map your network!\n[3] - Scan a website for vulnerable queries to sql injection!\n[4] - Open SQLMap\n[5] - open msfconsole\n[6] - Change your mac address\n[7] - Open Social Engeneering toolkit\n[8] - Deauth a system by MAC address\n[9] - Tries to execute a remote code vulnerability in wordpress CM plugin\n[10] - Eternal Blue Exploit Scanner\n[11] - Get Dependencies Info\n[12] - Install xerosploit\n[13] - Git Script Installer\n[14] - Ping A Target To Check If Online\n[15] - Traceroute a target to get hostname\n[16] - DNS Scanner\n[17] - SMTP Email Spoofer\n")

#if statements
if selection_item == "1":
    print("[*] Make sure the script http-frontpage-login.nse is installed from nmap")
    target_afpls = raw_input("[?] Target To Scan: ")
    print("[!] Trying to scan")
    time.sleep(2)
    # command: nmap <target> -p 80 --script=http-frontpage-login
    afpls_cmd = "nmap " + target_afpls + " -p 80 --script=http-frontpage-login"
    subprocess.call(afpls_cmd, shell=True)
    
        
elif selection_item == "2":
    print("[!]Starting...")
    #command: nmap -sP -PI -PT <ip>/24
    mapnIP = raw_input("What is your ip?: ")
    print("[!] Mapping Network")
    mapN_cmd = "sudo nmap -sP -PI -PT " + mapnIP + "/24"
    print("[*] Network mapped!")
    subprocess.call(mapN_cmd, shell=True)
    

            
elif selection_item == "3":
    print("[*] Make sure the script http-sql-injection is installed")
    target_sqls = raw_input("[?] Target To Scan: ")
    print("[!] Trying to scan")
    time.sleep(2)
    # command: nmap -sV --script=http-sql-injection <target>
    sqls_cmd = "nmap -sV --script=http-sql-injection " + target_sqls
    subprocess.call(sqls_cmd, shell=True)
    
elif selection_item == "4":
    sqlmap_cmd = "sudo sqlmap"
    print("[!] Starting SQLMAP!")
    subprocess.call(sqlmap_cmd, shell=True)

elif selection_item == "5":
    print("[!] Starting msfconsole")
    open_msf = "sudo msfconsole"
    subprocess.call(open_msf, shell=True)
    
elif selection_item == "6":
    print("[!] Starting")
    macinterf = raw_input("what interface do we change it on?: ")
    print("[!] THIS WILL PRODUCE A FAKE ERROR, CONTINUING..")
    time.sleep(5)
    maccmd = "sudo macchanger -r " + macinterf
    subprocess.call(maccmd, shell=True).read()
    

elif selection_item == "7":
    print("[!] Opening set...")
    time.sleep(2)
    cmdSET = "sudo setoolkit"
    subprocess.call(cmdSET, shell=True)

elif selection_item == "8":
    #cmd: aireplay-ng --deauth 0 -a (networks bssid) -c (Their mac address)
    print("[!] Setting up")
    bssidos = raw_input("Network bssid: ")
    vicmacdos = raw_input("Mac Address Of Victim: ")
    cmd = "aireplay-ng --deauth 0 -a " + bssidos + vicmacdos

elif selection_item == "9":
    print("[!] Welcome to remote code vulnerability scanner/exploiter make sure http-vuln-cve2014-8877.nse is installed from nmap")
    target = raw_input("TARGET: ")
    cmdWP = "nmap --script http-vuln-cve2014-8877 " + target
    subprocess.call(cmdWP, shell=True)
    
elif selection_item == "10":
    print("[!] Starting... make sure smb-double-pulsar-backdoor.nse is installed from nmap")
    ebsip = raw_input("Target ip: ")
    ebscmd = "nmap -p 445 " + ebsip + " --script=smb-double-pulsar-backdoor"
    subprocess.call(ebscmd, shell=True)
    #cmd: nmap -p 445 <target> --script=smb-double-pulsar-backdoor

elif selection_item == "11":
    print("GO TO NMAP.ORG AND DOWNLOAD THESE SCRIPTS\n")
    time.sleep(2)
    print("smb-double-pulsar-backdoor.nse\n")
    print("http-vuln-cve2014-8877.nse\n")
    print("http-sql-injection.nse\n")
    print("http-frontpage-login.nse\n")
    time.sleep(1)
    print("install those scripts from nmap.org scripts section, on the tab vuln")
    
elif selection_item == "12":
    print("[*] Installing")
    cmdGitXero = "git clone https://github.com/LionSec/xerosploit.git"
    gitdirscripts = raw_input("What dir would you like to install this to?: ")
    xerodir = "sudo cd " + gitdirscripts
    subprocess.call(xerodir, shell=True)
    subprocess.call(cmdGitXero, shell=True)
    
elif selection_item == "13":
    print("[*] Setting up...")
    time.sleep(5)
    gitscript = raw_input("Whats the git link to the project?: ")
    gitinstalldir = raw_input("What dir shall vulnbyte install this to?: ")
    gitmaster = "sudo git clone " + gitscript
    gitdirmaster = "sudo cd "+ gitinstalldir    
    print("[*] Tinkering...")
    time.sleep(1)
    subprocess.call(gitdirmaster, shell=True)
    print("[!] Pasting")
    time.sleep(1)
    subprocess.call(gitmaster, shell=True)
    
elif selection_item == "14":
	print("[!] Enter A Target")
	target_ping = raw_input("Enter a target ip: ")
	pingcmd = "ping " + target_ping
	os.system(pingcmd)
    
elif selection_item == "15":
	print("Setting up...")
	time.sleep(1)
	target_tracert = raw_input("[*] Target IP: ")
	tracert_cmd = "traceroute " + target_tracert
	subprocess.call(tracert_cmd, shell=True)
	
elif selection_item == "16":
	print("[*] Starting...")
	time.sleep(1)
	dnscan = raw_input("TARGET: ")
	dnscancmd = "nslookup " + dnscan
	subprocess.call(dnscancmd, shell=True)
	
elif selection_item == "17":
	server = smtplib.SMTP('mail.smtp2go.com', 2525)

	#Next, log in to the server
	username = input("What is your smtp2go username?: ")
	password = input("What is your smtp2go password?: ")
	server.login(username, password)

	#Send the mail
	msg = input("Input Message Here: ") # The /n separates the message from the header
	spoof = input("What is your spoofed email?: ")
	sender = input("What is the target email?: ")

	server.sendmail(spoof, sender, msg)
                #rec     #target

	print("Email Sent.")
else:
    print("not a valid option")
  
