import bcrypt
from cryptography.fernet import Fernet

account = {

}

def obtainUser():
    userName = input("Enter Username: ")
    return userName

def obtainMasterPassword():
    password = input("Enter Password: ")
    return password

def addUser():
    user = obtainUser()
    account[user] = obtainMasterPassword()
    return account
addUser()

for u, p in account.items():
    print(f"Username: {u}\nPassword: {p}")