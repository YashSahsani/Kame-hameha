import os
import base64
from aes_decryption_for_linux import aes_decrypt
def decrypt_lin():
    file_format = {'.Y4H':0}
    for actual_path, directories, files_found in os.walk('/'):
        for arg in files_found:
            ext = os.path.splitext(os.path.join(actual_path, arg))[1].upper()
            if(file_format.get(ext) == 0 and 'key.txt.y4h' not in os.path.join(actual_path, arg)):
                path = os.path.join(actual_path, arg)
                aes_decrypt(path)
    os.remove('res/key.txt')
