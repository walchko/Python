#! /usr/bin/python

#
# Kevin J. Walchko
# 28 Sept 2014
#
# http://daniel-baumann.ch/other/qr-codes/wifi/
#

import qrcode

qr = qrcode.QRCode(
	version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

name = 'Kevin J. Walchko'
url = 'http\://walchko.github.io'
paper_url = 'https\://github.com/walchko/soccer2'
email = 'kevin.walchko@outlook.com'

# WPA and WPA2 both use WPA
data = 'MECARD:N:{0};URL:{1};URL:{2};EMAIL:{3};;'.format(name,url,paper_url,email)
print data
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()

img.save("mecard.png","PNG")