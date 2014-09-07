#!/usr/bin/python

import sys
import argparse
from subprocess import check_output
import pprint as pp

# Lists IP connections from apps (Dropbox, Safari, etc)
def port_check():
    ans = check_output("lsof -i | grep ESTABLISHED", shell=True)
    return ans

# returns a list of wifi base stations (RSSI, protocol, etc) that it sees ... obviously wifi needs to be turned on
def sniff():
    ans = check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s ", shell=True)
    line = ans.split('\n')
    wifi=[]
    for i in line:
    	wifi.append(i.split())
    return wifi
    
# takes the output of port_check() and parses it to get the useful items
# returns [app,ip,port,protocol]
def parse_rec(rec, debug=False):
    iplist = list()
    xx=rec.split('\n') # break into lines
    
    for s in xx: 
        #print 'WTF \n'
        if len(s) == 0: continue
        #print 'line: ' +s+ '\n'
        xxx=s.split()                     # break each line into fields
        app=xxx[0]
        port=xxx[8].split("->")[0].split(':')[1] # grab the IP addr 
        ip=xxx[8].split("->")[1].split(':')[0] # grab the IP addr 
        protocol=xxx[8].split("->")[1].split(':')[1] # grab the IP addr  
        
        rec = [app,ip,port,protocol]
        iplist.append(rec)
        
        if debug: 
            pp.pprint(rec)
    
    return iplist 

# returns IP connections from various apps and returns a list composed of [app,ip,port,protocol] for each
def getIPConnections(p=False):
	ret = port_check()
	return parse_rec(ret,p) 

def main():
	parser = argparse.ArgumentParser('Lists local IP connections to a Mac computer')
	parser.add_argument('-v', '--verbose', help='print output', action='store_true')
	parser.add_argument('-w', '--wifi', help='list wifi access points', action='store_true')
	args = vars(parser.parse_args())
	
	p = args['verbose']
	w = args['wifi']
	
	if w:
		ans = sniff()
		if p:
			pp.pprint(ans)
		return ans
	else:
		return getIPConnections(p) 
	

if __name__ == "__main__":
	main()