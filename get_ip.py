import threading
import re
import subprocess
import platform
import time
Flag = False
ip = []

def task(n, cmd):
    global ip
    global Flag
    temp = cmd + str(n)
    if(platform.system() == 'Windows'):
        res = subprocess.Popen(("ping -n 1 " + temp), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    elif(platform.system() == 'Linux'):
        res = subprocess.Popen(("ping -c 1 " + temp), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    res = res.stdout.read().decode()
    if 'Destination host unreachable.' in res or 'Request timed out.' in res or 'Destination Host Unreachable' in res:
        pass
    else:
        ip.append(temp)
    if(n == 245):
        Flag = True

def get_ip_():
    global ip,Flag
    if(platform.system() == 'Windows'):
        cmd = "ipconfig"
        cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        temp = re.findall('IPv4 Address.+: (.+)',cmd.stdout.read().decode())
        temp = temp[len(temp)-3].rstrip()
        temp = temp.split('.')
        b1 = int(temp[0])
        b2 = int(temp[1])
        b3 = int(temp[2])
    elif(platform.system() == 'Linux'):
        cmd = 'ifconfig'
        cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        temp =  re.findall('inet \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',cmd.stdout.read().decode())
        temp = temp[0].split(" ")
        temp = temp[1].rstrip()
        temp = temp.split('.')
        b1 = int(temp[0])
        b2 = int(temp[1])
        b3 = int(temp[2])
    cmd = str(b1) + "."+ str(b2) + "." + str(b3) + "."
    print(cmd)
    for i in range(1,255):
        t = threading.Thread(name = i, target = task, args = (i, cmd))
        t.daemon = False
        t.start()
    while(True):
        if(Flag):
            return ip
        else:
            pass

