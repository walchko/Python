#!/usr/bin/python

import ip_locate, test2
from subprocess import check_output

def main():
	ips = test2.main()
	#print ips
	ret = ip_locate.locate_ip(ips)
	print ret
	

if __name__ == "__main__":
	main()