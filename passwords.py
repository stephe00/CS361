#StephenOium
#CS361
#ORSTATE
#Passwords
import requests
import fileinput
import string

def login(username, password):
    found = False
    with open("userpass.txt", "r+") as file:
        for line in file:
            user, pw = line.split(":")
            if username == user:
                print("User already exists")
                found = True
    file.close()
    if found == True:
        changepw = input("Change user password?[s/n]")
        if changepw == "s":
            output = ""
            for line in fileinput.input(["userpass.txt"], inplace=True):
                if line.strip().startswith(username):
                    line = username+":"+newpw
                output = output + line
            f = open("userpass.txt", "w")
            f.write(output)
            f.close()

    if not found:
        with open("userpass.txt", "a+") as file:
            account = '%s:%s\n'%(username,newpw)
            file.write(account)
            print ('Conta Guardada')

username = input("Insert username")
newpw = input("Insert password")

s = requests.session()
url_login = "<loginUrl>"

payload = {
    "username": "<user>",
    "password": "<pass>"
}

req1 = s.post(url_login, data=payload)

# Now to make sure you do not get the "Access denied", use the same session variable for the request.

req2 = s.get(url_earthdata)


login(username, newpw)
