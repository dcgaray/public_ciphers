from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.number import getPrime
from Crypto.Util.Padding import pad, unpad

def task3():
	msg = input("What is your message my G?: ")
	bit = int(input("Bit-length?(256, 1024, 2048): "))
	hMsg = msg.encode().hex()
	iMsg = int(hMsg, 16)
	# keytup = (pu, pr)
	keyTup = generateKeys(bit)
	ciphertext = encrypt(iMsg, keyTup[0])
	print(ciphertext)
	plaintext = decrypt(ciphertext,keyTup[1])
	print(plaintext)

	IV = get_random_bytes(16)
	recoveredMsg =keyFixing(keyTup[0], keyTup[1], msg, IV)
	print(recoveredMsg)

def generateKeys(bit):
	p1 = getPrime(bit)
	p2 = getPrime(bit)
	n = p1 * p2
	#what comes 1 after n?
	e = 65537
	o = (p1 - 1) * (p2 - 1)
	d = pow(e, -1, o)
	pu = [e, n]
	pr = [d, n]
	return (pu, pr)

def encrypt(msg, pu):
	return pow(msg, pu[0], mod=pu[1])

def decrypt(encMsg, pr):
	return pow(encMsg, pr[0], mod=pr[1])

def keyFixing(pu, pr, msg, iv):

	cPrime = pu[1]

	secKey = pow(cPrime, pr[0], mod=pr[1])
	secKey = secKey.to_bytes(128, "little")
	hashThingy = SHA256.new()
	hashThingy.update(secKey)
	digest = hashThingy.hexdigest()	
	intDigest = int(digest, 16)
	byteKey = intDigest.to_bytes(35, "little")
	key = byteKey[:16]

	enc = AES.new(key, AES.MODE_CBC, iv)
	bMsg = bytes(msg, "utf-8")
	cNought = enc.encrypt(pad(bMsg, 16))

	hashThingy2 = SHA256.new()
	secKey2 = 0
	secKey2 = secKey2.to_bytes(128, "little")
	hashThingy2.update(secKey2)
	digest = hashThingy2.hexdigest()
	intDigest2 = int(digest, 16)
	byteKey2 = intDigest2.to_bytes(35, "little")
	key2 = byteKey2[:16]
	enc2 = AES.new(key2, AES.MODE_CBC, iv)

	pText = enc2.decrypt(cNought)
	pText = unpad(pText, 16)
	plaintext = pText.decode("utf-8") 

	return plaintext









