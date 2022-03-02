from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.number import getPrime
from Crypto.Util.Padding import pad, unpad

def task3():
	msg = input("What is your message my G?: ")
	bit = int(input("Bit-lenght?(256, 1024, 2048: "))