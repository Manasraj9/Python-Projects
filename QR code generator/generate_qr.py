import qrcode as qr

img = qr.make("https://github.com/Manasraj9")
img.save("myqr.png")
