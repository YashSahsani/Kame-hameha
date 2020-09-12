from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import UnsupportedAlgorithm
import base64
import os
pem_key ="""-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAt8hFQLue+ybkcWTqPDQs
vWpXL1CUs4NmWbTlyMGLvA4axyDWekwKUq4VoFpnA9dR6RAN9CLuO1TmFRD0glNN
Gy3phX+1D+0Rq5Yw3unz8mQrUrVgkuNJarqntKKjqpLgUxryg44AV/kOvpc1ro6p
Sn6dqFtz2LBcRn81WstXNWDuBa/dvjZ4z45MwsdHIHiZ+TfQ8h4Nb+RNfdz+9sNJ
MmHPCbW8WPcnzmRm/a/4SyxJNuHFAiCvKR8nW6YLKmN8FiUNTuKdJZ/ehYVHSIOC
dvOe+0rngWDwzT0CjQbrB0XdTMDZd9umt11/aiKJmshs2vqCApC0rVeCmwA0vzIg
WJ7ID/Wk4wbfAwK8LLMlxnlI+S5KA9GGt6O8fqH28qazgrV2msoVhAbUsb+WIkhz
0PI/ZYzq75/mStOdFbK5N9eOaOu26k1fK8UAR9jAca2yaZamhkFpKJXWolRMPurK
O22XzsU9pOI27TuZgjYkbhqTvDMyIFLaukn02UYSk9Nf8vEImnMRLRIwHXzpfcoY
nG8zwV+X666HB8mF5gt1K1n1CRGmtFAE4keJKYTNkP/gIqcLAhgx6mAkXwPO02fr
M+rJjcSX2/cLKyIdW2fiE9m0Vq0ZscJzCDX0Kx9i4Gf89/FWLDPLMi3Oe5ahWi53
dY4zocxbUY1JpvOPVOnAP9ECAwEAAQ==
-----END PUBLIC KEY-----""".encode()
def public():
	global pem_key
	public_key = serialization.load_pem_public_key(
	        pem_key,
	        backend=default_backend()
	    )
	return public_key
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
        with open("res/temp_key.txt.y4h",'wb') as cipher:
            cipher.write(cipher_text+"Y$H4".encode())
    except UnsupportedAlgorithm:
        logger.exception("Asymmetric encryption failed")

def d_main():
	secert_data = open('res/temp_key.txt','r').read()
	encryption_(public(),secert_data)
	os.remove('res/temp_key.txt')
