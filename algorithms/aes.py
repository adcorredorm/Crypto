import base64
import os
import pyaes
from PIL import Image
from sys import argv

source = os.getcwd() + argv[1]
ext = argv[1].split('.')[-1]
destination = 'result.{}'.format(ext)
mode = int(argv[2])

if mode in (128, 192, 256):
    key = os.urandom(int(mode/8))

    aes = pyaes.AESModeOfOperationCTR(key)

    with open(source, 'rb') as file:
        string = file.read()
        copy = string

    encripted = aes.encrypt(string)
    encripted64 = base64.b64encode(encripted)
    print(encripted64)

    aes = pyaes.AESModeOfOperationCTR(key)
    decripted = aes.decrypt(base64.b64decode(encripted64))

    with open(destination, 'wb') as file:
        file.write(decripted)

    Image.open(destination).show()
else:
    print('El modo de operación debe ser 128, 192 o 256 bits')