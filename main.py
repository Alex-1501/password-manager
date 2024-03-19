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
    # Creates Fernet Token
    f = Fernet(key)
    token = f.encrypt(password.encode())
    return token, f

def decryptPassword(token, password):
    return token.decrypt(password)


def addUser():
    username = obtainUser()
    password = obtainPassword()
    encryptedPassword, token = encryptPassword(password)
    return {"username": username, "password": encryptedPassword, "token": token}

def main():
    # for every item in account output result
    user_data = addUser()
    print(user_data)
    print(f"\nUsername: {user_data['username']}")
    print(f"Password: {decryptPassword(user_data['token'], user_data['password'])}")

if __name__ == "__main__":
    main()