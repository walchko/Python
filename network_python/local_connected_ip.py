#!/usr/bin/python

import sys
from subprocess import check_output


def port_check():
    ans = check_output("lsof -i | grep ESTABLISHED", shell=True)
    return ans

def sniff():
    ans = check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s ", shell=True)
    return ans
    
def parse_rec(rec, debug=False):
    ip = list()
    xx=rec.split('\n') # break into lines
    
    #print rec
    
    for s in xx: 
        #print 'WTF \n'
        if len(s) == 0: continue
        #print 'line: ' +s+ '\n'
        xxx=s.split()                     # break each line into fields
        t=xxx[8].split("->")[1].split(':')[0] # grab the IP addr  
        ip.append(t)
        
        if debug: 
            print xxx[0], '\t', t
    
    return ip  

def main():
	ret = port_check()
	return parse_rec(ret,False) 
	

if __name__ == "__main__":
	main()