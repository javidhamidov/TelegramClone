import time
import json
class Message:
    def __init__(self, who_logined):
        self.filename = "account_messages.json"
        self.who_logined = who_logined
    def sender(self):
        with open(self.filename) as file:
            data = json.load(file)
        n = 0
        for name in data:
            n += 1
            print("{}. {}".format(n, name))
        print("N -" + str(n))
        flag = True
        while flag:    
            to = int(input("Choose whom do you want to send a message to : "))
            if to == 1:
                print("You cannot message yourself.")
            elif to in range(1, n+1):
                flag = False
            else:
                print("This user does not exist: ")
        recievers = []
        for reciever in data:
            recievers.append(reciever)
        print(recievers[to-1])
        message = input("Enter the message :\n")
        current = int(time.time())
        if data[self.who_logined]:
            if data[self.who_logined][recievers[to-1]]:
                data[self.who_logined][recievers[to-1]]["you"].append({"message" : message, "time" : current})
                data[recievers[to-1]][self.who_logined]["person"].append({"message" : message, "time" : current})
            else:
                data[self.who_logined][recievers[to-1]]["you"] = []
                data[self.who_logined][recievers[to-1]]["person"] = []
                data[self.who_logined][recievers[to-1]]["you"].append({"message" : message, "time" : current})
                data[recievers[to-1]][self.who_logined]["you"] = []
                data[recievers[to-1]][self.who_logined]["person"] = []
                data[recievers[to-1]][self.who_logined]["person"].append({"message" : message, "time" : current})
        else:
            data[self.who_logined] = {}
            data[self.who_logined][recievers[to-1]] = {}
            data[self.who_logined][recievers[to-1]]["you"] = []
            data[self.who_logined][recievers[to-1]]["person"] = []
            data[self.who_logined][recievers[to-1]]["you"].append({"message" : message, "time" : current})
            data[recievers[to-1]][self.who_logined] = {}
            data[recievers[to-1]][self.who_logined]["you"] = []
            data[recievers[to-1]][self.who_logined]["person"] = []
            data[recievers[to-1]][self.who_logined]["person"].append({"message" : message, "time" : current})
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)
    def all_messages(self):
        with open(self.filename) as file:
            data = json.load(file)
        n = 0
        for name in data:
            n += 1
            print("{}. {}".format(n, name))
        print("N -" + str(n))
        flag = True
        while flag:    
            to = int(input("Choose whom do you want to get a message from : "))
            if to == 1:
                print("You cannot get messages from chat with your account.")
            elif to in range(1, n+1):
                flag = False
            else:
                print("This user does not exist: ")
        recievers = []
        for reciever in data:
            recievers.append(reciever)
        print(recievers[to-1])
        all_messages = data[self.who_logined][recievers[to-1]]["you"].copy()
        all_messages += data[self.who_logined][recievers[to-1]]["person"].copy()
        times = []
        for i in range(0, len(all_messages)):
            times.append(all_messages[i]["time"])
            times.sort()
        for t in times:
            for i in range(0, len(all_messages)):
                if t == all_messages[i]["time"]:
                    msg = all_messages[i]
                    if msg in data[self.who_logined][recievers[to-1]]["you"]:
                        print("You : {}".format(msg["message"]))
                    elif msg in data[self.who_logined][recievers[to-1]]["person"]:
                        print("Person : {}".format(msg["message"]))
                            
messenger = Message("javid")
messenger.sender()
messenger.all_messages()