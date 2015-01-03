#!/usr/bin/python
# this doesn't work :(

import sys
from scapy.all import *


def sniffBeacon(p):
	unique = []
	if p.haslayer(Dot11Beacon):
		if unique.count(p.addr2) == 0:
			unique.append(p.addr2)
			print p.sprintf("%Dot11.addr2%[%Dot11Elt.info%|%Dot11Beacon.cap%]")
			
interface = sys.argv[1]   
sniff(iface=interface,prn=sniffBeacon)