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
    print(f"I am {usr1.name}, with Priv: {usr1.priv}")
    print(f"I am {usr1.name}, with Pub: {usr1.pub}")
    usr2 = User(p,g,IV, "Bob")
    print(f"I am {usr2.name}, with Priv: {usr2.priv}")
    print(f"I am {usr2.name}, with Pub: {usr2.pub}")
    usr1.genSecretKey(usr2.pub)
    usr2.genSecretKey(usr1.pub)

    usr1.genSymmetricKey() 
    usr2.genSymmetricKey() 
    print(usr1.symKey)
    print(usr2.symKey)

    if usr1.symKey == usr2.symKey:
        print('they got the same key')
    if usr1.symKey == 0 and usr2.symKey == 0:
        print("they're both zero")

if __name__ == "__main__":
    main()
