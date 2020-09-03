import threading
import re
import subprocess
Flag = False
def get_ip_():
    global Flag,ip
    while(True):
        if(Flag):
            return ip
        else:
            pass

def task(n, cmd):
    global ip
    global Flag
    temp = cmd + str(n)
    res = subprocess.Popen(("ping -n 1 " + temp), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    res = res.stdout.read().decode()
    if 'Destination host unreachable.' in res or 'Request timed out.' in res:
        pass
    else:
        ip.append(temp)
    if(n == 245):
        Flag = True
cmd = "ipconfig"
cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
temp = re.findall('IPv4 Address.+: (.+)',cmd.stdout.read().decode())
temp = temp[len(temp)-3].rstrip()
temp = temp.split('.')
b1 = int(temp[0])
b2 = int(temp[1])
b3 = int(temp[2])
cmd = str(b1) + "."+ str(b2) + "." + str(b3) + "."
ip = []
for i in range(1,255):
    t = threading.Thread(name = i, target = task, args = (i, cmd))
    t.daemon = False
    t.start()
print(get_ip_())