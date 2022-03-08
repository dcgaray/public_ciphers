import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256



class User():
    def __init__(self, p, g, initialVector, username):
        self.name = username
        self.randElem = random.randint(0, p-1)
        self.pub = pow(g, self.randElem, p) 
        self.p = p
        self.g = g
        self.IV = initialVector #IV variable
        self.secKey = None #var for da secret key
        self.symKey = None #var for symmetric key
        self.encryKey = None
        self.bOrder = "little" #byteOrder mode necessary for Python's "to_bytes func"

    #generates a secret key used for symmetric encryption from another
        # user's public key
    def genSecretKey(self, pubKey):
        # A = g^a % p
        # g = pubInput, a = self.randElem, p = self.p 
        self.secKey = pow(pubKey, self.randElem, self.p) 

    #performs SHA256 hashing and gets a 2byte symmetric key for AES-CBC
    def genSymmetricKey(self):
        hashThingy = SHA256.new()
        hashThingy.update(self.secKey.to_bytes(128, self.bOrder))
        digest = hashThingy.hexdigest()
        intDigest = int(digest, 16) #get our hex digest into a hex integer
        byteKey = intDigest.to_bytes(35, self.bOrder)
        self.symKey = byteKey[:16]

    #takes a messsage and encrypts it using AES-CBC
    def encrypt(self, msg):
        blckLen = 16 
        enc = AES.new(self.symKey, AES.MODE_CBC, self.IV)
        plaintext = bytes(msg, "utf-8")
        ptLen = len(plaintext)

        #check to see if we have to #PCKS 7 pad it
        if (ptLen % blckLen) != 0:
            padLen = blckLen - (ptLen % blckLen)
            for idx in range(padLen):
                plaintext += idx.to_bytes(1, self.bOrder)
        #no padding necessary 
        else:
            for i in range(blckLen):
                plaintext += b"16"

        return enc.encrypt(plaintext)

    #takes an AES-CBC encrypted messages and returns the plaintext
    def decrypt(self, ciphertext):
        enc = AES.new(self.symKey, AES.MODE_CBC, self.IV)
        bText = enc.decrypt(ciphertext) # this is in bytes
        bLen = len(bText)

        nonPadCount = 0
        for i in range(bLen-1, bLen, -1):
            # loop through our bytes until we find out where our padding occurs
            if bText[bLen - 1] ==  bText[i]:
                j += 1
            #PCKS 7 dictates the padding be the number of bytes remaining for pad
            else: 
                break

        #remove our padding
        if nonPadCount == bText[bLen - 1]:
            bText = bText[:bLen - nonPadCount]
        return bText.decode("utf-8")

    #returns the username provided when the user was first created
    def whoami(self):
        return self.name

