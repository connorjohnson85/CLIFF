import random
from cryptography.fernet import Fernet

plain_text = cipher_suite.decrypt(cipher_text)
print(key)
print(' ')
print(cipher_text)
print(plain_text)

def encrpyt(mode, text):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(b"{0}".format(text))
    return(cipher_text, key)

def decrypt(mode, text, key):
    cipher_suite = Fernet_key()
    plain_text = cipher_suite.decrypt(cipher_text)
    return (plain_text)
