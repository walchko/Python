#!/usr/bin/python

import netaddr as net
import argparse

# expect a list p = [[app,ip,port,protocol],lat,lon]
def addPoint(loc,p,vn):
	l = 'var %s = new google.maps.LatLng(%d, %d);' % (vn,p[1],p[2])
	loc.append(l)
	return loc

def searchServices(ip):
	domains = ['yahoo','git','google','facebook','dropbox','apple','pinterest','reddit','tumblr','steam','bitbucket','deviantart','windows','vimeo','vine','linux','twitter','youtube']
	icon = 'circle-thin'
	for d in domains:
		if ip.find(d) >=0:
			icon = d
			break
	
	#print icon
	return icon

# in site = [app,ip,port,protocol]
# returns the the icon either Font Awesome or just IP:port
def getIcon(site):
	app = site[0]
	ip = str(site[1])
	port = str(site[2])
	#print '[+] Finding:',app,ip,site[2],site[3]
	icon = '%s<br>%s'%(ip,port)
	
	svc = searchServices(ip)
	
	if app == 'Mail':
		#print '  Mail'
		# need to do a stack envelop and 
		icon = '<span class="fa-stack "><i class="fa fa-envelope-o fa-stack-2x fa-fw"></i><i class="fa fa-%s fa-stack-1x fa-fw"></i></span><br>%s'%(svc,port)
	
	elif svc != 'circle-thin':
		#print '  found service:',scv
		icon = '<i class="fa fa-%s pull-left"><br>%s'%(svc,port)
		
	# Mail app can be yahoo or outlook or etc
	# com.apple is Apple's CDN i think, but it is an app and shows amazon ip
	elif (app == 'com.apple') & ((ip.find('amazonaws.com')>=0) | (ip.find('akamaitechnologies.com')>=0) ):
		#print '  found: apple CDN'
		icon = '<i class="fa fa-%s pull-left"><br>%s'%('cloud',port)
	
	elif ip.find('me.com')>=0:
		#print '  found: apple'
		icon = '<i class="fa fa-%s pull-left"><br>%s'%('apple',port)
	
	else:
		#print '[-]  Not found:',ip,app,'<br>'
		icon
	
	return icon

# in points = [[app,ip,port,protocol],lat,lon]
# creates the javascript variables for google maps of all the points
def addVariables(points):
	b=[]
	name_array =[]
	loc_array=[]
	cnt = 0
	for i in points:
		#print 'point',i
		var_name = 'pt' + str(cnt)
		b=addPoint(b,i,var_name)
		loc_array.append(var_name)
		#name_array.append(str(i[0][0])+str(i[0][1])+str(i[0][2])+str(i[0][3]))
		
		fmt = getIcon(i[0])
		if fmt == ' ': continue
		name_array.append('<center>%s</center>'%fmt)
		cnt += 1
		
	#b.append('var locationArray = ' + str(loc_array) + ';')
	loc_str = 'var locationArray = ['
	for i in loc_array:
		loc_str = loc_str + i +','
	loc_str = loc_str + '];'
	b.append(loc_str)
	
	b.append('var locationNameArray = ' + str(name_array) + ';')
	
	return b

def create(points):
	a="""
	<!DOCTYPE html>
	<html>
	  <head>
	    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
		<title>Simple Map</title>
		<meta name="viewport" content="initial-scale=1.0, user-scalable=no">
		<meta charset="utf-8">
		<style>
		  html, body, #map-canvas {
			height: 100%;
			margin: 0px;
			padding: 0px
		  }
		</style>
		<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>
		<script>
	"""
	
	b = addVariables(points)
	
	c="""
    
	var map;
	
	function initialize() {
		var lat = 40, lon = -110;
	
		// Doesn't work for some reason
		//if (navigator.geolocation) {
		//	navigator.geolocation.getCurrentPosition(
		//		function(position){
		//			lat = position.coords.latitude;
		//			lon = position.coords.longitude;
		//		});
 		//};
		
		var mapOptions = {
			zoom: 2,
			center: new google.maps.LatLng(lat, lon),
			scrollwheel: false
		};


		map = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);

		var coord;
	  	for (coord in locationArray) {
			new google.maps.InfoWindow({
			  position: locationArray[coord],
			  map: map,
			  content: locationNameArray[coord]
		});
		
		//for(coord in locationArray){
		//	new google.maps.Marker({
		//		position: locationArray[coord],
		//		map: map,
		//		title: locationNameArray[coord]
		//});
	}

	}

	google.maps.event.addDomListener(window, 'load', initialize);

		</script>
	  </head>
	  <body>
		<div id="map-canvas"></div>
	  </body>
	</html>
	"""
	
	#print a
	
	page = []
	page.append(a)
	
	
	for i in b:
		page.append(i)
	
	
	page.append(c)
	
	return page


# Expect a list containing lines of html which will create a Google Map	
def printMap(map):
	for i in map:
		print i


def main():
	parser = argparse.ArgumentParser('Creates a Google Maps webpage with locations plotted on it')
	#parser.add_argument('-f', '--file', help='yaml file containing the locations to plot', required=True)
	#parser.add_argument('-p', '--path', help='location to grab images', default='.')
	#parser.add_argument('-v', '--video_name', help='video file name', default='out')
	#parser.add_argument('-n', '--numpy', type=str, help='numpy camera calibration matrix')
	#parser.add_argument('-s', '--size', type=int, nargs=2, help='size of image capture, e.g., 640 480')
	
	args = vars(parser.parse_args())
	
	points = []
	points.append(['127.0.0.10',41.850033, -87.6500523])
	points.append(['qc-in-f108.1e100.net',41.850033, 87.6500523])
	points.append(['127.0.0.1',-41.850033, 87.6500523])
	points.append(['anchorage',61.2180556, -149.9002778])
	points.append(['mexico',19.4270499, -99.1275711])
	
# 	cnt = 0
# 	for i in points:
# #		i[0] = i[0].replace('.','').replace('-','')
#  		if net.valid_ipv4(i[0]):
#  			i[0] = 'unknown' + str(cnt)
#  			cnt += 1
# 	
# 	for i in points:
# 		i[0] = i[0].replace('.','').replace('-','')
		
	map = create(points)
	printMap(map)
	

if __name__ == "__main__":
	main()