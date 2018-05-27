# vulnbytemenu

# This application will scan websites for common vulnerabilities using nmap and the respective scripts!

# Copyright 2018 by Allek Hall
# For Fair Use under GNU
# We Are Not Responsible for how you use this tool

import subprocess
import os
import time

print("VULNBYTE VULNERABILITY ACCESOR\n\n")
# Below the code starts

selection_item = raw_input("[AFPLS] - Anonymous Front Page Login Scan!\n[MAP] - Map your network!\n[SQLS] - Scan a website for vulnerable queries to sql injection!\n[SQL] - Open SQLMap\n[MSF] - open msfconsole\n[MAC] - Change your mac address\n[SET] - Open Social Engeneering toolkit\n[DOS] - Deauth a system by MAC address\n[WP] - Tries to execute a remote code vulnerability in wordpress CM plugin\n[EBS] - Eternal Blue Exploit Scanner")

#if statements
if selection_item == "AFPLS":
	print("[*] Make sure the script http-frontpage-login.nse is installed from nmap")
	target_afpls = raw_input("[?] Target To Scan: ")
	print("[!] Trying to scan")
	time.sleep(2)
	# command: nmap <target> -p 80 --script=http-frontpage-login
	afpls_cmd = "nmap " + target_afpls + " -p 80 --script=http-frontpage-login"
	subprocess.call(afpls_cmd, shell=True)
		
elif selection_item == "MAP":
    #command: nmap -sP -PI -PT <ip>/24
	print("[!] Mapping network")
	mapnIP = raw_input("What is your ip?: ")
	print("[!] Mapping Network")
	mapN_cmd = "sudo nmap -sP -PI -PT " + mapnIP + "/24"
	print("[*] Network mapped!")
	subprocess.call(mapN_cmd, shell=True)
	

			
elif selection_item == "SQLS":
	print("[*] Make sure the script http-sql-injection is installed")
	target_sqls = raw_input("[?] Target To Scan: ")
	print("[!] Trying to scan")
	time.sleep(2)
	# command: nmap -sV --script=http-sql-injection <target>
	sqls_cmd = "nmap -sV --script=http-sql-injection " + target_sqls
	subprocess.call(sqls_cmd, shell=True)
	
elif selection_item == "SQL":
	sqlmap_cmd = "sudo sqlmap"
	print("[!] Starting SQLMAP!")
	subprocess.call(sqlmap_cmd, shell=True)

elif selection_item == "MSF":
	print("[!] Starting msfconsole")
	open_msf = "sudo msfconsole"
	subprocess.call(open_msf, shell=True)
	
elif selection_item == "MAC":
	print("[!] Starting")
	macinterf = raw_input("what interface do we change it on?: ")
	print("[!] THIS WILL PRODUCE A FAKE ERROR, CONTINUING..")
	time.sleep(5)
	maccmd = "sudo macchanger -r " + macinterf
	subprocess.call(maccmd, shell=True).read()
	

elif selection_item == "SET":
	print("[!] Opening set...")
	time.sleep(2)
	cmdSET = "sudo setoolkit"
	subprocess.call(cmdSET, shell=True)

elif selection_item == "DOS":
    #cmd: aireplay-ng --deauth 0 -a (networks bssid) -c (Their mac address)
	print("[!] Setting up")
	bssidos = raw_input("Network bssid: ")
	vicmacdos = raw_input("Mac Address Of Victim: ")
	cmd = "aireplay-ng --deauth 0 -a " + bssidos + vicmacdos

elif selection_item == "WP":
	print("[!] Welcome to remote code vulnerability scanner/exploiter make sure http-vuln-cve2014-8877.nse is installed from nmap")
	target = raw_input("TARGET: ")
	cmdWP = "nmap --script http-vuln-cve2014-8877 " + target
	subprocess.call(cmdWP, shell=True)
	
elif selection_item == "EBS":
	print("[!] Starting... make sure smb-double-pulsar-backdoor.nse is installed from nmap")
	ebsip = raw_input("Target ip: ")
	ebscmd = "nmap -p 445 " + ebsip + " --script=smb-double-pulsar-backdoor"
	subprocess.call(ebscmd, shell=True)
	#cmd: nmap -p 445 <target> --script=smb-double-pulsar-backdoor
	

	
