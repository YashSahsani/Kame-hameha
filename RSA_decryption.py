import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os
def decrypt_met(private_key,cipher_text):
        # DECRYPTION
        decrypted_cipher_text_bytes = private_key.decrypt(
            ciphertext=base64.urlsafe_b64decode(cipher_text),
            padding=padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )
        return decrypted_cipher_text_bytes
def read_private_key(password_bytes):
        with open("res/private_key.pem", "rb") as key_file:
            private_key_after = serialization.load_pem_private_key(
                data=key_file.read(),
                password=password_bytes,
                backend=default_backend()
            )
        return private_key_after
def read_cipher():
    return open('res/key.txt.y4h').read()
def d_main():
    password=str(input("Enter password:"))
    password_bytes = password.encode('utf-8')
    private_key = read_private_key(password_bytes)
    cipher = read_cipher()
    os.remove('res/key.txt.y4h')
    with open('res/key.txt','w') as keys:
        keys.write(decrypt_met(private_key,cipher).decode())
