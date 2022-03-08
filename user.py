import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256



class User():
    # In the case of our assignment p=primeNumber q=PrimitiveRoot of p
    def __init__(self, p, q, initialVector, username):
        self.name = username
        self.randElem = random.randint(0, p-1)
        self.pub = pow(q, self.randElem, p) 
        self.p = p
        self.q = q 
        self.IV = initialVector #IV variable
        self.secKey = None #var for da secret key
        self.symKey = None #var for symmetric key
        self.byteOrder = "little" #byteOrder mode necessary for Python's "to_bytes func"
        self.blckLen = 16

    #generates a secret key used for symmetric encryption from another
        # user's public key
    def genSecretKey(self, pubKey):
        # A = g^a % p
        # g = pubInput, a = self.randElem, p = self.p 
        self.secKey = pow(pubKey, self.randElem, self.p) 

    #normally this could be done right after the generation of the secret key
        #but in light of the assignment specifications, this is done in multiple steps
    #performs SHA256 hashing and gets a 2byte symmetric key for AES-CBC
    def genSymmetricKey(self):
        self.blckLen = 16
        hashObj = SHA256.new()
        hashObj.update(self.secKey.to_bytes(128, self.byteOrder))
        digest = hashObj.hexdigest()
        intDigest = int(digest, self.blckLen) #get our hex digest into a hex integer
        byteDigest = intDigest.to_bytes(35, self.byteOrder)
        self.symKey = byteDigest[:self.blckLen]

    #takes a messsage and encrypts it using AES-CBC
    def encrypt(self, msg):
        self.blckLen = 16 
        enc = AES.new(self.symKey, AES.MODE_CBC, self.IV)
        plaintext = bytes(msg, "utf-8")
        ptLen = len(plaintext)
        blkRemainder = ptLen % self.blckLen

        #pad the information using #PCKS 7 standards
        if blkRemainder != 0:
            padLen = self.blckLen - blkRemainder 
            #check to see how much we need to pad our block by
            for idx in range(padLen):
                plaintext += idx.to_bytes(1, self.byteOrder)
        #if our message is the size of the block, pad it with an extra block anyways
        else:
            for i in range(self.blckLen):
                plaintext += b"16"

        return enc.encrypt(plaintext)

    #takes an AES-CBC encrypted messages and returns the plaintext
    def decrypt(self, ciphertext):
        enc = AES.new(self.symKey, AES.MODE_CBC, self.IV)
        byteText = enc.decrypt(ciphertext) # this is in bytes
        bLen = len(byteText)

        #go through and find out where our padding occurs within our encrypted message
        nonPadCount = 0
        #starting at the end and workingo our down to zero
        for i in range(bLen-1, bLen, -1):
            # loop through our bytes until we find out where our padding occurs
            if byteText[bLen - 1] ==  byteText[i]:
                j += 1
            #PCKS 7 dictates the padding be the number of bytes remaining for pad
            else: 
                break

        #remove our padding
        if nonPadCount == byteText[bLen - 1]:
            bText = byteText[:bLen - nonPadCount]
        return byteText.decode("utf-8")

    #returns the username provided when the user was first created
    def whoami(self):
        return self.name

