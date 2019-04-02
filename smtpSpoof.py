import smtplib
def main():
    print("""
          _______________________________________________
                           MAIL SPOOFER
          _______________________________________________
          """)
    uChoice = input("Would you like to continue?:\nmain$ ")
    if uChoice == "y" or "yes" or "Yes" or "Y":
            login()
def login():
    host = input("[!] Mail Server: ")
    port = input("[!] Mail Server Port: ")
    server = smtplib.SMTP(host, port)
    username = input("[+] Authentication Username:\nclient$ ")
    password = input("[+] Authentication Password:\nclient$ ")
    server.login(username, password)
    send()
def send():
    msg = input("Input Message Here: ") # The /n separates the message from the header
    spoof = input("What is your spoofed email?: ")
    sender = input("What is the target email?: ")
    server.sendmail(spoof, sender, msg)
    print("[*] Sent.")
