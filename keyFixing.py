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

	if iMsg == plaintext:
		print("ayo")





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
