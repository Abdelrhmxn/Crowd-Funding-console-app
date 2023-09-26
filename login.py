import os
import json
from usermain import secondaryMenu


def login():
    email = input("Enter Email: \n")
    password = input("Enter Password: \n")
    users = get_users()
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Successful Login\n")
            secondaryMenu(user["email"], user["first_name"])
            break
    else:
        print("Failed To Login\n")


def get_users():
    try:
        with open("./users.json", "r") as json_file:
            users = json.load(json_file)
            return users
    except Exception as e:
        return []
