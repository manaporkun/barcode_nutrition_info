from pyzbar import pyzbar
from PIL import Image
info = pyzbar.decode(Image.open('index.png'))
print(info)