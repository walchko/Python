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

# expects a list of [app,ip,port,protocol]
# returns a list of [[app,ip,port,protocol] lat, lon]
def locate_ip(iplist):
	locs = []
	#print iplist
	#########################
	# From: https://github.com/appliedsec/pygeoip
	gi4 = pygeoip.GeoIP('./GeoLiteCity.dat', pygeoip.MEMORY_CACHE)

	for iprec in iplist:
		#print iprec
		ip = iprec[1]
		#########################
		# From: https://github.com/appliedsec/pygeoip
		#gi4 = pygeoip.GeoIP('./GeoLiteCity.dat', pygeoip.MEMORY_CACHE)
		
		if numeric_ip(ip) == True:
			try:
				rec = gi4.record_by_addr(ip)
			except:
				print '[-] cannot geolocate address: %s'%(ip)
		elif local_ip(ip) == True:
			#print "local host"
			continue
		else:
			try:
				rec = gi4.record_by_name(ip)
			except:
				print '[-] cannot geolocate address: %s'%(ip)
			
		loc = [iprec, rec['latitude'], rec['longitude']]
		locs.append(loc)
	return locs

if __name__ == "__main__":
    import sys
    list = sys.argv[1].strip('[]')
    list = list.split(',')
    print locate_ip(list)
    
    
    