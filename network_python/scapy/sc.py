#!/usr/bin/python
#
# Simple tool which sniffs packets and tries to identify what they are and what hosts 
# are they coming from and to.

from scapy.all import *
import socket

# transforms the IP address into a host name
def formatSrc(pkt):
	src = pkt[IP].src
	try:
		src = socket.gethostbyaddr(src)[0]
	except:
		if src.find('169.254.') >= 0:
			src = 'local link (auto config)'
		else:
			src = pkt[IP].src
	return src

# identifies broadcasts and multicasts and transforms the IP address into a host name
def formatDst(pkt):
	dest = pkt[IP].dst
	
	if dest.find('224.0.0') >= 0:
		dest = "Multicast"
	elif dest.find('255.255.255.255') >= 0:
		dest = "Broadcast"
	elif dest.find('239.255.255.250') >= 0:
		dest = "Simple Service Discovery Protocol"
	else: 
		# try to get host name
		p = IP(src=pkt[IP].dst)
		dest = formatSrc(p)
	
	return dest

# this is the main loop
def pktPrint(pkt):
	if pkt.haslayer(Dot11Beacon):
		print '[+] detected 802.11 Beacon Frame'
	elif pkt.haslayer(Dot11ProbeReq):
		print '[+] detected 802.11 Probe Request Frame'
	elif pkt.haslayer(TCP) & pkt.haslayer(IP):
		dst = formatDst(pkt)
		src = formatSrc(pkt)
		sport = pkt.sprintf("%TCP.sport%")
		dport = pkt.sprintf("%TCP.dport%")
		proto = pkt.sprintf("%IP.proto%")
		fmt = '[+] TCP[%s]: %s:%s -> %s:%s' % (proto,src,sport,dst,dport)
		print fmt
		#ls(pkt)
	elif pkt.haslayer(IP):
		src = formatSrc(pkt)
		dst = formatDst(pkt)
		proto = pkt.sprintf("%IP.proto%")
		fmt = '[+] IP[%s]: %s -> %s' % (proto,src,dst)
		print fmt
	elif pkt.haslayer(DNS):
		print '[+] DNS packet'
	elif pkt.haslayer(IPv6):
		print '[-] IPv6: ',pkt.summary()
	elif pkt.haslayer(ARP):
		print '[-] ARP: ',pkt.summary()
	else:
		print '[ ] Unknown: ',pkt.summary()

sniff(prn=pktPrint)