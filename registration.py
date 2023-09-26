import json
from utils import Validator


def register():
    first_name = Validator.validate_name("First Name")
    last_name = Validator.validate_name("Last Name")
    email = Validator.validate_email("Email")
    password = Validator.validate_password("Password")
    confirm_password = Validator.validate_confirm_password(password, "Confirm Password")
    mobile = Validator.validate_mobile("Mobile Phone")
    new_user = {
        "first_name": first_name,
        "last Name": last_name,
        "email": email,
        "password": password,
        "mobile_phone": mobile,
    }
    if new_user:
        add_user(new_user)
        print(" Registration Successful ".center(48, "*"))
    else:
        print(" Registration Failed ".center(48, "*"))


def add_user(new_user):
    try:
        listusers = get_users()
        with open("users.json", "w") as json_file:
            listusers.append(new_user)
            json.dump(listusers, json_file)
    except Exception as e:
        print(e)


def get_users():
    try:
        with open("./users.json", "r") as json_file:
            users = json.load(json_file)
            return users
    except Exception as e:
        return []
