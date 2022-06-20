import os
from scapy.all import *

print('Welcome to Linux Firewall')

interface = conf.iface 
print(interface)

def help():
    print("What attack do you want to stop?")
    print("Enter 1 to set rules for LAND Attack)


def landAttack():
    os.system("iptables -F ; iptables -t nat -F ; iptables -t mangle -F ; iptables -X")
