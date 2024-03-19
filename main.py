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

# Registers A User
def addUser():
    username = obtainUser()
    password = obtainPassword()
    token, f = encryptPassword(password)
    return {"username": username, "token": token, "key": f}

def loginUser(user_data):
    inputUser = input("\nUsername: ")
    inputPassword = input("Password: ")

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

def addPassword(stored_Passwords):
    password = obtainPassword()
    token, f = encryptPassword(password)
    stored_Passwords['tokens'].append(token)
    stored_Passwords['keys'].append(f)

def main():
    user_data = {}
    while True:
        flag = False
        userInput = input("\n[+] Press '1' To Register\n[+] Press '2' To Login\nEnter Here: ")
        if userInput == '1':
            user_data = addUser()
        else:
            flag = loginUser(user_data)
            if flag:
                print(f"Welcome {user_data['username']}")
                stored_Passwords = {'tokens': [], 'keys': []}  # New dictionary for storing passwords
                break
    
    while True:
        userInput = input("\n[+] Press '1' To List All Stored Passwords\n[+] Press '2' To Add A Password\nEnter Here: ")
        if userInput == '1':
            if stored_Passwords.get('tokens'):
                for token, key in zip(stored_Passwords['tokens'], stored_Passwords['keys']):
                    decrypted_password = decryptPassword(key, token).decode()
                    print(decrypted_password)
            else:
                print("No Passwords Found")
        elif userInput == '2':
            addPassword(stored_Passwords)
            print("Password Added!")
        else:
            break

if __name__ == "__main__":
    main()