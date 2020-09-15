import base64
import os
import win32api
from aesd_windows import aes_decrypt
def decrypt_win():
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        if(str(drive) == "C:\\"):
                continue
        for root,dirs,files in os.walk(drive):
            for f in files:
                try:
                    ext = f.split(".")[2]
                except:
                    continue
                if(ext == "y4h"):
                    try:
                        path = str(os.path.join(root, f))
                        aes_decrypt(path)
                    except:
                        continue
