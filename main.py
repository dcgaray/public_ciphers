import random,secrets
from user import User

def main():
    '''
    you = "World"
    print(f"Hello {you}")
    g = User(2,3,4, "Alice")
    g.genSecretKey(5)
    g.whoami()
    '''
    task1()

def task1():
    IV = secrets.token_bytes(16)
    p = 37 
    g = 5
    usr1 = User(p,g,IV, "Alice")
    usr2 = User(p,g,IV, "Bob")
    usr1.genSecretKey(usr2.pub)
    usr2.genSecretKey(usr1.pub)

    usr1.genSymmetricKey() 
    usr2.genSymmetricKey() 

    encryptedMsg1 =usr1.encrypt("I am a secret")
    encryptedMsg2 =usr2.encrypt("I am also a secret")

    print(usr1.decrypt(encryptedMsg2)) 
    print(usr2.decrypt(encryptedMsg1)) 


if __name__ == "__main__":
    main()
