#! /usr/bin/python

import qrcode

with open("test.vcard", "r") as f:
    data = f.read()

f.close()

qr = qrcode.QRCode(
	version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
    
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()

img.save("image.png","PNG")