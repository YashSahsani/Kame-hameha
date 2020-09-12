import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os
def aes_decrypt(filename,method):
    if(method==1):
            a = filename.split('/')
            file1 = ''
            for i in range(len(a)-1):
                file1 += a[i]+'/'
            print(file1)
            name = a[len(a)-1]
        elif(method==2):
            a = filename.split('\\')
            file1 = ''
            for i in range(len(a)-1):
                file1 += a[i]+'\\'
            print(file1)
            name=file1[len(a)-1]
    b64 = json.loads(open(filename,'r').read())
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    keys = open('res/key.txt','r').readlines()
    for line in keys:
        if(file1+name.split('.')[0] == line.split(":")[0]):
            key = line.split(":")[1]
    key = b64decode(key)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    os.remove(filename)
    open(filename[:-4],'w').write(pt.decode())
