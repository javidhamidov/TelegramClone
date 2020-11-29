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
            if to in range(0, n+1):
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
            frm = int(input("Choose whom do you want to send a message to : "))
            if frm in range(0, n+1):
                flag = False
            else:
                print("This user does not exist: ")
        recievers = []
        for reciever in data:
            recievers.append(reciever)
        print(recievers[frm-1])


messenger = Message("javid")
#messenger.sender()
messenger.all_messages()