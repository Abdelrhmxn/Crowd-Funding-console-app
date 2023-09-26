import os
from registration import register
from login import login


def mainMenu():
    while True:
        os.system("clear")
        print(" Crowd Funding ".center(48, "*"))
        print(" Main Menu ".center(48, "*"))
        choice = input("Choose:\n 1)Login\n 2)Registeration\n 3)Exit\n")
        if choice.isnumeric():
            choice = int(choice)
        if choice == 1:
            login()
        elif choice == 2:
            register()
        elif choice == 3:
            exit()


mainMenu()
