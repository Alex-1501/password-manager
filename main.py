import bcrypt
from cryptography.fernet import Fernet

def obtainUser():
    userName = input("Enter Username: ")
    return userName

def obtainPassword():
    password = input("Enter Password: ")
    return password

def encryptPassword(password):
    key = Fernet.generate_key()
    f = Fernet(key)
    t = f.encrypt(password.encode())
    return t, f

def decryptPassword(key, password):
    return key.decrypt(password)


def addUser():
    username = obtainUser()
    password = obtainPassword()
    encryptedPassword, key = encryptPassword(password)
    return {"username": username, "password": encryptedPassword, "key": key}

def main():
    # for every item in account output result
    user_data = addUser()
    print(user_data)
    print(f"\nUsername: {user_data['username']}")
    print(f"Password: {decryptPassword(user_data['key'], user_data['password'])}")

if __name__ == "__main__":
    main()