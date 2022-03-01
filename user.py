import random
from Crypto.cipher import AES
from Crypto.Hash import SHA256

class User():
    def __init__(self, p, g, initialVector, username):
        self.p = p
        self.g = g
        self.name = username
        self.IV = initialVector

    def whoami(self):
        print(self.name)
