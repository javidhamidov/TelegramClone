import time
import account_loginer_registerer
import messages

who_logined = ""
while True:
    option = input("Choose what you want to do :\n1. Register\n2. Log in\n3. Send a message\n4. Get messages\n5. Log out\n6. Exit\n>>>")
    if option == "1":
        registrator = account_loginer_registerer.Authentificator()
        registrator.register()
    elif option == "2":
        loginer = account_loginer_registerer.Authentificator()
        who_logined = loginer.loginer()
    elif option == "3":
        if who_logined == "":
            print("You have not logged in !")
        else:
            messenger = messages.Message(who_logined)
            messenger.send()
    elif option == "4":
        if who_logined == "":
            print("You have not logged in!")
        else:
            messenger = messages.Message(who_logined)
            messenger.get()
    elif option == "5":
        who_logined = ""
        print("Logged out !")
    elif option == "6":
        break
    else:
        print("There is no such an option. Please enter the appropriate option.")