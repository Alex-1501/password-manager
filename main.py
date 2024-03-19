from cryptography.fernet import Fernet

def obtainUser():
    userName = input("\nEnter Username: ")
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
    return token, f

# Decrypts Password
def decryptPassword(f, password):
    return f.decrypt(password)

def addUser():
    username = obtainUser()
    password = obtainPassword()
    token, f = encryptPassword(password)
    return {"username": username, "token": token, "key": f}


def loginUser(user_data):
    inputUser = input("\nPlease Enter Your Username To A Valid Account: ")
    inputPassword = input("Please Enter Your Passphrase To A Valid Account: ")

    if inputUser != user_data['username'] or inputPassword != decryptPassword(user_data['key'], user_data['token']).decode():
        print("\n-----------------")
        print("-Login Incorrect-")
        print("-----------------")

        return False
    else:
        print("\n------------------")
        print("-Login Successful-")
        print("------------------")
        return True

def main():
    while(True):
        flag = False
        userInput = input("\nPress '1' to add an account\nPress '2' to login\nEnter Here: ")
        if userInput == '1':
            user_data = addUser()
            print(user_data)
        else:
            flag = loginUser(user_data)
            if flag:
                break

if __name__ == "__main__":
    main()