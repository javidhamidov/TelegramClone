import json


class Authentificator:
    def __init__(self):
        self.filename = "account_password.json"

    def register(self):
        #TODO : change the structure of account_password.json : account : name, password : password
        #TODO : change the code to be able to work with new structure of account_messages.json
        with open(self.filename) as file:
            data = json.load(file)
        flag = True
        while flag:
            name = input("Enter your new account's name : ")
            if name in data[0]:
                print("This name already exists in the data base. Take another name.")
            else:
                flag = False
        password = input("Enter a new password : ")
        data[0][name] = password
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Registered!")

    def login(self):
        with open("account_password.json") as file:
            data = json.load(file)
        flag = True
        while flag:
            name = input("Enter your account's name : ")
            if name in data[0]:
                print("This name exists!")
                flag = False
            elif name not in data[0]:
                answer = input("Do you want to continue trying?(yes/no) : ")
                if answer == "no":
                    name = 0
                    flag = False
                else:
                    continue
        if name == 0:
            logined = False
            return logined
        else:
            flag = True
            while flag:
                password = input("Enter the account's password : ")
                if password == data[0][name]:
                    print("Logined!")
                    logined = True
                    flag = False
                elif password != data[0][name]:
                    answer = input(
                        "Do you want to continue trying?(yes/no) : ")
                    if answer == "no":
                        logined = False
                        user_logined = name
                        flag = False
                    else:
                        continue
            return logined, user_logined


authentificator = Authentificator()
authentificator.register()
# authentificator.login()