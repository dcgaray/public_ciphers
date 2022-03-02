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
    print(usr1.symKey)
    print(usr2.symKey)

    print(usr1.encrypt("lmao"))


if __name__ == "__main__":
    main()
