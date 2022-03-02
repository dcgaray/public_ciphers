import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256



class User():
    def __init__(self, p, g, initialVector, username):
        self.priv = random.randint(0, p-1)
        self.pub = pow(g, self.priv, p) 
        self.name = username
        self.IV = initialVector #IV variable
        self.secKey = None #var for da secret key
        self.symKey = None #var for symmetric key
        self.encryKey = None

    #generates a secret key used for symmetric encryption from another
        # user's public key
    def genSecretKey(self, pubKey):
        # A = g^a % p
        # g = pubInput, a = self.priv, p = self.pub
        self.secKey = pow(pubKey, self.priv, self.pub) 

    #performs SHA256 hashing and gets a 2byte symmetric key for AES-CBC
    def genSymmetricKey(self):
        bOrder = "little" #byteOrder mode necessary for Python's "to_bytes func"
        hashThingy = SHA256.new()
        hashThingy.update(self.secKey.to_bytes(128, bOrder))
        digest = hashThingy.hexdigest()
        intDigest = int(digest, 16) #get our hex digest into a hex integer
        byteKey = intDigest.to_bytes(35, bOrder)
        self.symKey = byteKey[:16]

    def whoami(self):
        print(f"I am {self.name}: {self.secKey}")
