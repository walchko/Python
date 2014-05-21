#!/usr/bin/python

basename='denso'
axisip='192.168.1.152'  # '192.168.1.95'
axisuser='dlink'  #'admin'
axispass='dlink'  #'axis'
flvcreator='TTU ME Department'

import urllib2, time, os, re, getopt, sys

def usage():
    print """ip_cam.py grabs images from an IP camera \nUsage: axisgrab.py [--grab | --encode]"""

def main():

    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'g:e:',[ 'grab', 'encode' ])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    
    if optlist == [] and args == []:
        usage()
        sys.exit(2)
    	

    for opt, junk in optlist:
        if (opt=='--grab'):    
            auth_handler = urllib2.HTTPBasicAuthHandler()
            auth_handler.add_password('/',axisip,axisuser,axispass)
            opener = urllib2.build_opener(auth_handler)
            #urllib2.install_opener(opener)
            #axis_jpg=urllib2.urlopen('http://%s/axis-cgi/jpg/image.cgi' % ( axisip ) )
            #axis_jpg=urllib2.urlopen('http://%s/mjpeg.cgi?user=%s&password=%s&snapshot=on' % ( axisip,axisuser,axispass ) )
            axis_jpg=urllib2.urlopen('http://%s/image/jpeg.cgi' % ( axisip ) )
    
            filename='%s_%s_%s.jpg' % ( basename, time.strftime('%Y%m%d'), time.strftime('%H%M%S') )
            local_jpg=open(filename,'w')
            local_jpg.write(axis_jpg.read())
            local_jpg.close()
            os.chmod(filename,0644)

#         if (opt=='--encode'):
#             os.system('mencoder -really-quiet -ovc lavc -lavcopts vcodec=flv -mf fps=25:type=jpg \\'mf://%s_%s*.jpg\\' -of lavf -lavfopts i_certify_that_my_video_stream_does_not_use_b_frames -o %s_%s.flv >&/dev/null' % ( basename, time.strftime('%Y%m%d'), basename, time.strftime('%Y%m%d') ))
#     
#             playlistname="playlist-%s.xml" % ( basename )
#             playlist=open(playlistname,'w');
#             playlist.write("""
#             <?xml version="1.0" encoding="utf-8"?>
#             <playlist version="1" xmlns="http://xspf.org/ns/0/">
#             <trackList>
#             """)
# 
#     
#             files=os.listdir(".")
#             files.sort()
#             repattern="%s.+flv" % ( basename )
#             recompiled=re.compile(repattern)
#             for file in files:
#                 if recompiled.search(file):
#                     playlist.write("    <track>\n")
#                     playlist.write("      <title>%s</title>\n" % (file))
#                     playlist.write("      <creator>%s</creator>\n" % (flvcreator))
#                     playlist.write("      <location>%s</location>\n" % (file))
#                     playlist.write("      <info>force_download.php?file=%s</info>\n" % (file))
#                     playlist.write("    </track>\n")
# 
#             playlist.write("""
#             </trackList>
#             </playlist>
#             """)

if __name__ == "__main__":
    main()