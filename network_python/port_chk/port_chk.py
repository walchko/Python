#!/usr/bin/env python

import socket
import sys

class Scanner:
	def bgrabber(self,sock):
		try:
			sock.send("I'm running a port scan on your server for penetration testing\r\n")
			banner=sock.recv(1024)
			return banner
		except:
			return None
	
	def openPort(self,ip,port):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((ip, port))
# 			print 'opened',ip,':',port
			return sock
		except:
			sock.close()
			return None
			
	def scan(self,ip):
# 		socket.setdefaulttimeout(0.5)
		try:
			for port in range(1,1024):	
				sock = self.openPort(ip,port)
				if sock:
					service = self.bgrabber(sock)
					if service:
						print "[+] Open: {}: {}".format(port,service.strip())
					else:
						try:
							svc = socket.getservbyport(port)
							print "[+] Open: {}: {}".format(port,svc.strip())
						except:
							print "[+] Open: {}: unknown".format(port)
					sock.close()
#			else:
# 				print "[-] Closed: {}".format(port)

# 		except:
# 			print 'unknown error ... fuck'
# 			pass
#
		except KeyboardInterrupt:
			print "You pressed Ctrl+C"
			sys.exit()
# 
# 		except socket.gaierror:
# 			print 'Hostname could not be resolved. Exiting'
# 			sys.exit()
# 
# 		except socket.error:
# 			print "Couldn't connect to server"
# 			sys.exit()

	
def main():
	scanner = Scanner()
	scanner.scan('192.168.1.13')


if __name__ == '__main__':
    main()

