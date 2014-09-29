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

# WPA and WPA2 both use WPA
data = 'WIFI:S:kamino;T:WPA;P:MagicMan321;;'
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()

img.save("wifi.png","PNG")