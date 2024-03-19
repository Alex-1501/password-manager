from cryptography.fernet import Fernet

def obtainUser():
    userName = input("Enter Username: ")
    return userName

def obtainPassword():
    password = input("Enter Password: ")
    return password

# Encrypts Password
def encryptPassword(password):
    # Generates A Key
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(password.encode())
    print(f"token: {token}")
    return token, f

# Decrypts Password
def decryptPassword(f, password):
    return f.decrypt(password) 


def addUser():
    username = obtainUser()
    password = obtainPassword()
    token, f = encryptPassword(password)
    return {"username": username, "token": token, "key": f}

def main():
    # for every item in account output result
    user_data = addUser()
    print(user_data)
    print(f"\nUsername: {user_data['username']}")
    print(f"Password: {decryptPassword(user_data['key'], user_data['token'])}")

if __name__ == "__main__":
    main()