#! /usr/bin/python

import base64, time;

#time.strptime(localtime,time.localtime(time.time()),)
#print localtime

vc_fname = "Kevin"
vc_lname = "Walchko"
vc_avatar = "./Farnsworth2.png"
vc_public_key = "./public_key.comodo.com.pem"
vc_home_email = "kevin.walchko@gmail.com"
vc_url = "http:/github.com/walchko"
vc_im = "aim:johndoe@aol.com"

vc_home_phone = "" # "(111) 222-3333"
vc_home_addr = "" # "111 here st;Aldie;VA;12345;United States of America"

vc_title = ""
vc_org = ""
vc_work_phone = ""
vc_work_email = ""
vc_work_addr = ""


with open(vc_avatar, "rb") as f:
    image_data = f.read()
    image_data_64 = image_data.encode("base64")
    

with open(vc_public_key, "r") as f:
    key_data = f.read()
#    print key_data.encode("base64")
    
f=open("./test.vcard","w")

f.write("BEGIN:VCARD \n")
f.write("VERSION:3.0 \n")

# BASIC INFO ----------------------------------------------
f.write("N:"+vc_lname+";"+vc_fname+";;;\n")
f.write("FN:"+vc_fname+" "+vc_lname+"\n")
#f.write("PHOTO;PNG;ENCODING=BASE64:"+image_data_64+"\n")
f.write("PHOTO;VALUE=URL;TYPE=PNG:http://upload.wikimedia.org/wikipedia/en/0/0f/FuturamaProfessorFarnsworth.png \n")
f.write("EMAIL;type=INTERNET;type=HOME:"+vc_home_email+"\n")
f.write("IMPP:"+vc_im+"\n")
f.write("URL:"+vc_url+"\n")

# WORK ----------------------------------------------------
f.write("TITLE:"+vc_title+"\n")
f.write("ORG:"+vc_org+"\n")
f.write("TEL;type=WORK;type=VOICE:"+vc_home_phone+"\n")
f.write("EMAIL;type=INTERNET;type=WORK:"+vc_work_email+"\n")
#f.write("KEY;PGP;ENCODING=BASE64:"+key_data+"\n")
#f.write("KEY;TYPE=application/pgp-keys;ENCODING=BASE64:"+key_data+"\n")
f.write("ADR;WORK:;;"+vc_work_addr+"\n")

# HOME -----------------------------------------------------
f.write("TEL;type=WORK;type=VOICE:"+vc_home_phone+"\n")
f.write("ADR;HOME:;;"+vc_home_addr+"\n")

# MISC -----------------------------------------------------
f.write("PRODID:-//Kevin's Python Script//EN \n")
f.write("KIND:individual \n")
f.write("LANG:en-US \n")
#f.write("REV"+vc_rev+"\n")
f.write("END:VCARD \n")

f.close()