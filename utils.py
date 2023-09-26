import re
from datetime import datetime
from datetime import date


class Validator:
    @staticmethod
    def validate_name(msg):
        while True:
            name = input(f"{msg}:\n")
            name = name.replace(" ", "")
            if name.isalpha():
                return name
            else:
                print(f"Invalid {msg}")

    @staticmethod
    def validate_number(msg):
        while True:
            number = input(f"{msg}:\n")
            if number.replace(".", "", 1).isdigit():
                return float(number)
            else:
                print("Invalid Number")

    @staticmethod
    def validate_email(msg):
        while True:
            email = input(f"{msg}:\n")
            if re.fullmatch(r"^[\w\.]+@([\w]+\.)+[\w]{2,4}$", email):
                return email
            else:
                print("Invalid Email")

    @staticmethod
    def validate_password(msg):
        while True:
            password = input(f"{msg}:\n")
            if password != "":
                return password
            else:
                print("Invalid Input")

    @staticmethod
    def validate_confirm_password(passwd, msg):
        while True:
            confirm_pass = input(f"{msg}:\n")
            if passwd == confirm_pass:
                return True
            else:
                print("Not Confirmed .... \n")

    @staticmethod
    def validate_mobile(msg):
        while True:
            mobile = input(f"{msg}:\n")
            if re.fullmatch(r"^01[0-2,5]\d{8}$", mobile):
                return mobile
            else:
                print("Invalid Number")

    @staticmethod
    def validate_time(msg, delta=datetime.strptime(datetime.today().strftime("%d/%m/%Y"), "%d/%m/%Y")):
        while True:
            date_str = input(f"{msg}:\n")
            try:
                time = datetime.strptime(date_str, "%d/%m/%Y")
                if time >= delta:
                    return time
            except Exception as e:
                print(e)
