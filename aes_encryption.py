import json
import os
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
def aes_encrypt(filename):
    data = open(filename,'rb').read()
    key = get_random_bytes(32)
    try:
        os.mkdir('res/')
        f = open("")
    except:
        pass
    open('res/key.txt','a').writelines(filename.split('.')[0]+":"+b64encode(key).decode()+ '\n')
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext':ct})
    os.remove(filename)
    print(result)
    with open(filename+".y4h",'w') as wr:
        wr.write(result)
