#!/usr/bin/env python
#
# Can't seem to kill this program with ctrl-c ... it just keeps going!!!
#

import nmap
#import optparse
from multiprocessing import Process
import multiprocessing
from multiprocessing import Pool
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


def getIP():
	ip = socket.gethostbyname(socket.gethostname())
	i=ip.split('.')
	ip = i[0]+'.'+i[1]+'.'+i[2]+'.'
	return ip
		
def main():
	ip = getIP()
	
	hosts=[]
	for i in range(25):
		hosts.append(ip+str(i))
	
	# simpler multi threaded process
	pool = Pool(10)
	pool.map(nmapScan,hosts)
	pool.close()
	pool.join()
	


if __name__ == '__main__':
    main()

