from user import User

def main():
    you = "World"
    print(f"Hello {you}")
    g = User(2,3,4, "Alice")
    g.whoami()


if __name__ == "__main__":
    main()
