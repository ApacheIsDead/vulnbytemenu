import requests as re
import time
import os
import subprocess


def proxyManager():
    print("Proxy Manager")
    ud = "proxylist.txt"
    with open(ud) as file:
        file = file.readlines()
    for line in file:
        x = 0
        print("Checking" + x + line)
        x += 1
        subprocess.call("ping " + line)


target = input("Target Link To Main Page: ")
filelink = input("Wordlist File Link: ")

with open(filelink) as file:
    file = file.readlines()

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130331 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; ar) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)',
    'Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0',
]

for line in file:
    x = 0
    x += 0
    print("Checking" + x + line)
    response = re.get(
        target + line, headers={'User-Agent': user_agents[x % len(user_agents)]})
    if (response.status_code >= 200 and response.status_code <= 299):
        print(target + line + " " + str(response.status_code) +
              " " + time.strftime("%H:%M:%S") + " OKKKKKKK DOMAIN")
        with open("gooddics.txt", "w") as f:
            f.write(target + line + " " + str(response.status_code))
            print("Good domain wrote to file")
    else:
        print(target + line + " " + str(response.status_code) +
              " " + time.strftime("%H:%M:%S"))
