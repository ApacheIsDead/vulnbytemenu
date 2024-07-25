import sockets
import html
import subprocess


def main():
    subprocess.call("python3 -m http.server").read()
    subprocess.call("cd /var/www/")
    subprocess.call("mkdir home")
    subprocess.call("cd home")


main()
