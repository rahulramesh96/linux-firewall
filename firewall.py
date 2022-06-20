import os
from scapy.all import *
import sys


print('Welcome to Linux Firewall')

interface = conf.iface 
print()
print("The working network interface is " + interface)
ip = get_if_addr(interface)
print('The IP address: '+ip)

def help():
    print("What attack do you want to stop?")
    print("Enter 1 to set rules for LAND Attack")

def landAttack():
    os.system("sudo iptables -F ; iptables -t nat -F ; iptables -t mangle -F ; iptables -X")
    os.system('sudo iptables -A INPUT -s '+  ip + '/24'  + ' j DROP')
    print('SAFE FROM LAND ATTACK.')

if (len(sys.argv)) == 1:
    choice = int(input("Enter the choice to stop packet attacks "))
    if choice == 1:
        landAttack()




