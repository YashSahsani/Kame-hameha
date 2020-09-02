import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os
def aes_decrypt(filename):
    b64 = json.loads(open(filename,'r').read())
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    keys = open('res/key.txt','r').readlines()
    for line in keys:
        if(filename.split('.')[0] == line.split(":")[0]):
            key = line.split(":")[1]
    key = b64decode(key)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    os.remove(filename)
    open(filename[:-4],'w').write(pt.decode())
