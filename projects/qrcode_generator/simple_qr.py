import pyqrcode
import qrtools
from PIL import Image
from pyzbar.pyzbar import decode

def encoding(message, path):
    qr = pyqrcode.create(message)
    qr.png(path, scale=6)
    return path

def decoding(path):
    data = decode(Image.open(path))
    return data[0].data


# testpath = encoding("Hello World!", "test1.png")
# print(decoding(testpath))