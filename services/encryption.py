import random
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
plain_text = cipher_suite.decrypt(cipher_text)
print(key)
print(' ')
print(cipher_text)
print(plain_text)
def encrpyt(mode, text):
    print(text)

def decrypt(mode, text, key):
    print(text)
