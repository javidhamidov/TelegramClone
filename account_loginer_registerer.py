import json

class Authentificator:
    def __init__(self):
        self.filename = "account_password.json"
    def register(self):
        #Open file with account names and passwords
        with open(self.filename) as file:
            data = json.load(file)
        #Create a list of users who have alredy registered
        current_users = []
        for dictionary in data:
            current_users.append(dictionary["account"])
        print(current_users)
        #Initialize loop that asks user about his new account's password
        while True:
            account_name = input("Enter your new account's name : ")
            if account_name == "":
                print("You have not entered anything !")
                continue
            elif " " in account_name:
                print("Your account's name cannot consist of spaces !")
                continue
            elif account_name in current_users:
                print("This user name is not available !")
                continue
            account_password = input("Enter your new account's password : ")
            if account_password == "":
                print("You have not entered anything !")
                print("You have to begin from account's name again .")
                continue
            elif " " in account_password:
                print("Your account's paassword cannot consist of spaces !")
                print("You have to begin from account's name again .")
                continue
            break
        #Create new dictionary that will include the name and password that user just entered
        new_user = {"account" : account_name, "password" : account_password}
        #Appending the new_user dictionary to the data list
        data.append(new_user)
        #Writing the data to the json file
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
        print("Registered !")
    def loginer(self):
        #Open file with account names and passwords
        with open(self.filename) as file:
            data = json.load(file)
        current_users = []
        for dictionary in data:
            current_users.append(dictionary["account"])
        print(current_users)
        while True:
            account_name = input("Enter your account's name : ")
            if account_name not in current_users:
                print("This user name does not exist !")
                continue
            account_password = input("Enter your account's password : ")
            check_user = {"account" : account_name, "password" : account_password}
            if check_user not in data:
                print("Wrong password !")
                print("You have to begin from account's name again .")
                continue
            break
        print("Logged in !")
        logined = account_name
        return logined