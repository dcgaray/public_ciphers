import random,secrets
from user import User
from keyFixing import task3

def main():
    '''
    you = "World"
    print(f"Hello {you}")
    '''
    p = int("B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371", 16) 
    g = int("A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5", 16)
    
    task1(37,5)
    task2(p,g)
    '''
    task2(p,p)
    task2(p,p-1)
    task2(p,1)
    '''
    task3()


def task1(p,g):
    IV = secrets.token_bytes(16)
    usr1 = User(p,g,IV, "Alice")
    usr2 = User(p,g,IV, "Bob")
    usr1.genSecretKey(usr2.pub)
    usr2.genSecretKey(usr1.pub)

    usr1.genSymmetricKey() 
    usr2.genSymmetricKey()

    encryptedMsg1 =usr1.encrypt("I am a secret")
    encryptedMsg2 =usr2.encrypt("I am also a secret")
    #^^^ First half of Task1 ^^^#

    #vvv Second half of Task1 vvv#
    p = int("B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371", 16) 
    g = int("A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5", 16) 

    usr3 = User(p,g,IV, "Laura")
    usr4 = User(p,g,IV, "Frankie")

    usr1.genSecretKey(usr2.pub)
    usr2.genSecretKey(usr1.pub)

    usr1.genSymmetricKey() 
    usr2.genSymmetricKey() 

    msg1 = "Hahaha, don't tell John the secret"
    msg2 = "hahah, I told Laura's secret"

    encMsg1 = usr1.encrypt(msg1)
    encMsg2 = usr2.encrypt(msg2)
    print(f"I am {usr3.whoami()} this is my message{encMsg1}")
    print(f"I am {usr4.whoami()} this is my message{encMsg2}")

    decMsg1 = usr1.decrypt(encMsg2)
    decMsg2 = usr2.decrypt(encMsg1)

    print(f"{usr3.whoami()} found: {decMsg1}")
    print(f"{usr4.whoami()} found: {decMsg2}")

def task2(p, g):
    IV = secrets.token_bytes(16)
    usr1 = User(p,g,IV, "Alice")
    usr2 = User(p,g,IV, "Bob") 
    #modification of the public keys by Mallory
    usr1.pub = p
    usr2.pub = p

    usr1.genSecretKey(usr2.pub)    
    usr2.genSecretKey(usr1.pub)    

    usr1.genSymmetricKey()
    usr2.genSymmetricKey()

    msg1 = "hahah, I am secret"
    msg2 = "ahahah, I am also a secret"

    encMsg1 = usr1.encrypt(msg1)
    encMsg2 = usr2.encrypt(msg2)

    decMsg1 = usr1.decrypt(encMsg2)
    decMsg2 = usr2.decrypt(encMsg1)

    print(f"{usr1.whoami()} found: {decMsg1}")
    print(f"{usr2.whoami()} found: {decMsg2}")


if __name__ == "__main__":
    main()
