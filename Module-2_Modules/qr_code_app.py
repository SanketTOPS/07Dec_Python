import pyqrcode

url="https://www.tops-int.com/"

qr=pyqrcode.create(url)

qr.png('tops.png')

