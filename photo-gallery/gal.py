

import os

def gallery(index):
	x=len(index)
	for fname in index:
	    while x>0:
	        x=x-1
	        index[x] = index[x].lower()
	        index[x] = '<a href="./' + index[x].replace("jpg", "html") + '">' + '<img src="./Thumbs/' + index[x] + '" height="240" width="320"/>' + '</a>'
	
	listString='\n'.join(index)
		
	file = open("gallery.html", 'w')
	
	file.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"' + '\n')
	file.write('    "http://www.w3.org/TR/html4/loose.dtd">' + '\n')
	file.write('<html>' + '\n')
	file.write('<head>' + '\n')
	file.write('<style>' + '\n')
	file.write('body {font-size:small;padding:10px;background-color:black;margin-left:15%;margin-right:15%;font-family:"Lucida Grande",Verdana,Arial,Sans-Serif;color: white;}' + '\n')
	file.write('img {border-style:solid;border-width:5px;border-color:white;}' + '\n')
	file.write('h1 {text-align:center;}' + '\n')
	file.write('a:link {color: grey; text-decoration: none;}' + '\n')
	file.write('a:visited {color: grey; text-decoration: none;}' + '\n')
	file.write('a:active {color: grey; text-decoration: none;}' + '\n')
	file.write('a:hover {color: grey;text-decoration: underline;}' + '\n')
	file.write('</style>' + '\n')
	file.write('</head>' + '\n')
	file.write('<body>' + '\n')
	file.write(listString + '\n')
	file.write('</body>' + '\n')
	file.write('</html>')
	file.close()

def getDir():
	list = os.listdir('./Images')
	list.remove('.DS_Store')
	list = [element.lower() for element in list]
	return list

	
index=getDir()
print index

gallery(index)

#exit(0)


next = getDir()
next = [element.replace("jpg", "html") for element in next]
image=getDir()
page=getDir()
page  = [element.replace("jpg", "html") for element in page]

print "---"

next.append(page[0])
print page

x=len(next)
y=len(page)
z=len(image)

for fname in page:
        y=y-1
        x=x-1
        z=z-1
        file = open(page[y], 'w')
        file.write('<html>' + '\n')
        file.write('<head>' + '\n')
        file.write('<script type="text/javascript">function delayer(){window.location = "./' + next[x].replace("jpg", "html") +'"}</script>' + '\n')
        file.write('<style>' + '\n')
        file.write('body {font-size:small;text-align:center;background-color:black;font-family:"Lucida Grande",Verdana,Arial,Sans-Serif;color: white;}' + '\n')
        file.write('a:link {color: white; text-decoration: none;}' + '\n')
        file.write('a:visited {color: white; text-decoration: none;}' + '\n')
        file.write('a:active {color: white; text-decoration: none;}' + '\n')
        file.write('a:hover {color: white;text-decoration: underline;}' + '\n')
        file.write('</style>' + '\n')
        file.write('</head>' + '\n')
        #file.write('<body onLoad="setTimeout(\'delayer()\', 3000)">' + '\n')
        file.write('<p><a href="./gallery.html">' + "gallery" + '</a></p>' + '\n')
        file.write('<a href="./' + next[x] + '">' + '<img height="90%" src="./Images/' + image[z] + '" />' + '</a>')
        file.write('</body>' + '\n')
        file.write('</html>')
        file.close()