import json
import os
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
def aes_encrypt(filename):
    try:
        a = filename.split('\\')
        file1 = ''
       	for i in range(len(a)-1):
            file1 += a[i]+'\\\\'
        name=a[len(a)-1]
        data = open(filename,'rb').read()
        key = get_random_bytes(32)
        try:
            os.mkdir('res/')
            f = open("")
        except:
            pass
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        result = json.dumps({'iv':iv, 'ciphertext':ct})
        os.remove(filename)
        print(result)
        with open(filename+".y4h",'w') as wr:
            wr.write(result)
        open('res/temp_key.txt','a').writelines(file1+name.split('.')[0]+":"+b64encode(key).decode()+ '\n')
    except:
        return
