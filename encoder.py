# -*- coding: utf-8 -*-

from cryptography.fernet import Fernet
import json

def encode(auth_file,name):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(bytes(auth_file,encoding = 'utf-8'))
    with open(r'auth\{}.txt'.format(name),'w') as outfile:
        json.dump(str(ciphered_text),outfile)
    with open(r'auth\key_{}.txt'.format(name),'w') as outfile:
        json.dump(str(key),outfile)


# =============================================================================
# with open("gmail_auth.json",'r') as readfilr:
#     auth = json.load(readfilr)
# 
# a = encode(auth['password'],'password')
# =============================================================================
