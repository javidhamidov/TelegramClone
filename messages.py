import time
import json

class Message:
    def __init__(self, logined):
        self.logined = logined
        self.filename = "account_messages.json"
        self.filename2 = "account_password.json"
    def send(self):
        with open(self.filename) as file:
            data = json.load(file)
        with open(self.filename2) as file:
            data2 = json.load(file)
        all_users = []
        for dictionary in data2:
            all_users.append(dictionary["account"])
        all_users.remove(self.logined)
        while True:
            n = 1
            nums = []
            for user in all_users:
                print("{}. {}".format(n, user))
                nums.append(n)
                n += 1
            #Ask whom user want to send the message to
            try:
                reciever = int(input("Choose user to send a message : "))
            except ValueError:
                print("Number !")
                continue
            if reciever in nums:
                break
            else:
                print("This user does not exist !")
                continue
        print(all_users[reciever-1])
        message = input("Enter your message :\n")
        msg_info = {"message" : message, "sender" : self.logined, "reciever" : all_users[reciever-1], "time" : int(time.time())}
        data.append(msg_info)
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
    def get(self):
        with open(self.filename) as file:
            data = json.load(file)
        with open(self.filename2) as file:
            data2 = json.load(file)
        all_users = []
        for dictionary in data2:
            all_users.append(dictionary["account"])
        all_users.remove(self.logined)
        while True:
            n = 1
            nums = []
            for user in all_users:
                print("{}. {}".format(n, user))
                nums.append(n)
                n += 1
            #Ask whom user want to get all the message from
            try:
                reciever = int(input("Choose user to get all the message from : "))
            except ValueError:
                print("Number !")
                continue
            if reciever in nums:
                break
            else:
                print("This user does not exist !")
                continue
        for message in data:
            if (all_users[reciever-1] == message["reciever"] and self.logined == message["sender"]) or (all_users[reciever-1] == message["sender"] and self.logined == message["reciever"]):
                if self.logined == message["sender"]:
                    print("You : {}".format(message["message"]))
                elif self.logined == message["reciever"]:
                    print("Person : {}".format(message["message"]))