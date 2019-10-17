import base64
import os
import pyDes
from PIL import Image
from sys import argv

source = os.getcwd() + argv[1]
ext = argv[1].split('.')[-1]
crypted = os.getcwd() + argv[1] + '.crypted'
destination = os.getcwd() + '/result.{}'.format(ext)

with open(source, 'rb') as file:
    string = base64.b64encode(file.read())

des = pyDes.des(argv[2], pyDes.CBC, '\0\0\0\0\0\0\0\0', pad=None, padmode=pyDes.PAD_PKCS5)

string = des.encrypt(string)
with open(crypted, 'wb')as file:
    file.write(string)
    print(string)

string = des.decrypt(string)
with open(destination, 'wb') as file:
    file.write(base64.b64decode(string))

Image.open(destination).show()