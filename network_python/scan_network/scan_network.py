#!/usr/bin/env python

import nmap
#import optparse
from multiprocessing import Process
import multiprocessing
import socket
#from awake import wol
	

def printHost(h,ip):
	print h['hostname'] + " is " + h['status']['state']
	print "-["+ip+"]------------------------"
	ports = h['tcp'] #printPorts(h['tcp'])
	pp = sorted(ports.iterkeys())
	for p in pp:
		print " - "+str(p)+"/"+ports[p]['name']+" is "+ports[p]['state']
	print "\n"

def nmapScan(host):
	p = multiprocessing.current_process()
#	print " Starting Scan ", p.name, p.pid
	nm = nmap.PortScanner()
	nm.scan(host)
	hosts = nm.all_hosts()
	
	try:
		printHost(nm[host],p.name)
	except KeyError:
		return

# Only need the first 3 parts of the IP address
def getIP():
	ip = socket.gethostbyname(socket.gethostname())
	i=ip.split('.')
	ip = i[0]+'.'+i[1]+'.'+i[2]+'.'
	return ip
	
def main():

	ip = getIP()
	
	jobs=[]
	for i in range(255):
		host = ip + str(i+1)
		#wol.send_magic_packet(host)
		p = Process(name=host,target=nmapScan, args=(host,)) 
		jobs.append(p)
		p.start()


if __name__ == '__main__':
    main()

