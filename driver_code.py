from os import listdir
from os.path import isfile, join
from os import getcwd
from aes_decryption import aes_decrypt
from aes_encryption import aes_encrypt
import RSA_encryption as Rencrypt
import RSA_decryption as Rdecrypt


driver = int(input("Enter 1 for encryption and 2 for decryption:"))
if(driver == 1):
   onlyfiles = [f for f in listdir(getcwd()) if(isfile(join(getcwd(), f))  and f.split('.')[1]=="txt" )]
   for file in onlyfiles:
      aes_encrypt(file)
   Rencrypt.d_main()
elif(driver == 2):
   Rdecrypt.d_main()
   onlyfiles = [f for f in listdir(getcwd()) if(isfile(join(getcwd(), f))  and f.split('.')[1]=="txt" )]
   for file in onlyfiles:
       aes_decrypt(file)
   