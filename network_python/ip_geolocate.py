#!/usr/bin/python
#
# Simple script to geolocate an IP address or website.
#
# ip_locate [website]
#
# where:
#   website: is an IP address (8.8.8.8) or a website (google.com)

import pygeoip


def numeric_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for item in parts:
        #if not 0 <= int(item) <= 255:
        #    return False
        if item.isdigit() == False:
            return False
    return True

def local_ip(ip):
	this_machine = ['localhost','127.0.0.1','.home','.local']
	for w in this_machine:
		if ip.find(w) >=0:
			return True
	else:
		return False

def locate_ip(iplist):
	locs = []
	for ip in iplist:
	
		#########################
		# From: https://github.com/appliedsec/pygeoip
		gi4 = pygeoip.GeoIP('./GeoLiteCity.dat', pygeoip.MEMORY_CACHE)
		
		if numeric_ip(ip) == True:
			rec = gi4.record_by_addr(ip)
		elif local_ip(ip) == True:
			#print "local host"
			continue
		else:
			rec = gi4.record_by_name(ip)
			
		loc = [ip, rec['latitude'], rec['longitude']]
		locs.append(loc)
	return locs

if __name__ == "__main__":
    import sys
    list = sys.argv[1].strip('[]')
    list = list.split(',')
    print locate_ip(list)
    
    
    