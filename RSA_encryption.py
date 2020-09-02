import base64
import logging
from random import SystemRandom
import os
from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
# set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def encryption_(public_key,plain_text):
    try:
        # ENCRYPTION
        cipher_text_bytes = public_key.encrypt(
            plaintext=plain_text.encode('utf-8'),
            padding=padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )
        # CONVERSION of raw bytes to BASE64 representation
        cipher_text = base64.urlsafe_b64encode(cipher_text_bytes)
        with open("res/key.txt.y4h",'wb') as cipher:
            cipher.write(cipher_text)
    except UnsupportedAlgorithm:
        logger.exception("Asymmetric encryption failed")

def generate_public_key_(private_key):
    public_key = private_key.public_key()
    pem_public = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    with open("res/public_key.pem", 'wb') as key_file:
            key_file.write(pem_public)
    return public_key
def generate_private_key_(password_bytes):
    # GENERATE NEW KEYPAIR
    private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=default_backend()
        )
    pem_private = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(password_bytes)
        )
    try:
        os.mkdir('res/')
    except:
        pass
    with open("res/private_key.pem", 'wb') as key_file:
            key_file.write(pem_private)
    return private_key

def password_():
    passwd = input("Enter password (or leave it empty to generate random password):")
    if(len(passwd)!=0):
        logger.info(passwd)
        password_bytes = passwd.encode('utf-8')
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        password = "".join(SystemRandom().choice(alphabet) for _ in range(20))
        logger.info(password)
        password_bytes = password.encode('utf-8')
    return password_bytes

def d_main():
    filename='res/key.txt'
    password = password_()
    private_key = generate_private_key_(password)
    public_key = generate_public_key_(private_key)
    secert_data = open(filename,'r').read()
    encryption_(public_key,secert_data)
    os.remove(filename)


