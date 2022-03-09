from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.number import getPrime
from Crypto.Util.Padding import pad, unpad


byteOrder = "little"
blckLen = 16

def task3():
	msg = input("What is your message my G?: ")
	bitLen = int(input("Bit-length?(256, 1024, 2048): "))
	#vvv Textbook RSA
	hMsg = msg.encode().hex()
	iMsg = int(hMsg, blckLen)
	keyTup = generateKeys(bitLen)
	pubKey = keyTup[0]		
	privKey = keyTup[1]
	ciphertext = encrypt(iMsg, pubKey)
	print(f"CipherText: {ciphertext}")
	plaintext = decrypt(ciphertext,privKey)
	print(f"Encoded-Plaintext: {plaintext}")
	##^^^Textbook RSA
	IV = get_random_bytes(blckLen)
	encryptedMsg1 = keyFixing(pubKey, privKey, msg, IV) 
	recoveredMsg = MalleabilitySignatures(encryptedMsg1, IV)
	print(f"Recovered Message: {recoveredMsg}")

#generates RSA public and private keys based off a provided string-length
# int -> int list * int list
def generateKeys(bitLen):
	p1 = getPrime(bitLen)
	p2 = getPrime(bitLen)
	n = p1 * p2
	#what comes 1 after n?
	e = 65537
	omega = (p1 - 1) * (p2 - 1)
	d = pow(e, -1, omega)
	publicKey = [e, n]
	privateKey = [d, n]
	return (publicKey, privateKey)

#takes a string and private key{e,n} and encrypts the message"
# string * int list -> byte string
def encrypt(msg, pu):
	return pow(msg, pu[0], pu[1])

#inverse of encrypt 
# byte_string ->
def decrypt(encMsg, pr):
	return pow(encMsg, pr[0], pr[1])

def keyFixing(pu, pr, msg, iv):
	cPrime = pu[1]

	#pr[0] = e, pr[1]= n
	secKey = pow(cPrime, pr[0], pr[1])
	secKey = secKey.to_bytes(128, byteOrder)
	hashThingy = SHA256.new()
	hashThingy.update(secKey)
	#convert our ASCII MSG into Hex
	digest = hashThingy.hexdigest()	
	#convert our hex value into an integer
	intDigest = int(digest, blckLen)
	byteKey = intDigest.to_bytes(35, byteOrder)
	key = byteKey[:blckLen]

	enc = AES.new(key, AES.MODE_CBC, iv)
	bMsg = bytes(msg, "utf-8")
	cNought = enc.encrypt(pad(bMsg, blckLen))

	return cNought

#Mallory recreating valid signatures
def MalleabilitySignatures(cNought, iv):
	hashThingy2 = SHA256.new()
	secKey2 = 0 
	secKey2 = secKey2.to_bytes(128, byteOrder)
	hashThingy2.update(secKey2)
	digest = hashThingy2.hexdigest()
	intDigest2 = int(digest, blckLen)
	byteKey2 = intDigest2.to_bytes(35, byteOrder)
	key2 = byteKey2[:blckLen]
	enc2 = AES.new(key2, AES.MODE_CBC, iv)

	pText = enc2.decrypt(cNought)
	pText = unpad(pText, blckLen)
	plaintext = pText.decode("utf-8") 

	return plaintext

