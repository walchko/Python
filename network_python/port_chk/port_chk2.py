#!/usr/bin/env python

import socket
import sys

import logging
#logging.getLogger("scapy").setLevel(1)

from scapy.all import *

class Scanner:
	def network(self,net="192.168.1.0/24"):
		ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=net),timeout=2)
		d = {}
		for s,r in ans: 
			d[ r.sprintf("%Ether.src%") ] = r.sprintf("%ARP.psrc%")
		return d
			
	def scan(self,ip,ports=(1,1024)):
		try:
			res,unans = sr( IP(dst=ip)/TCP(flags="S", dport=ports),timeout=2 )
			res.nsummary( lfilter=lambda (s,r): (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)) )

		except KeyboardInterrupt:
			print "You pressed Ctrl+C"
			sys.exit()


	
def main():
	scanner = Scanner()
	net = scanner.network('192.168.1.0/24')
	for hd,ip in net.iteritems():
		print ip
		scanner.scan(ip)


if __name__ == '__main__':
    main()

