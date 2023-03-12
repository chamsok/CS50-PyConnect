from prettytable import PrettyTable
import sys
import random
import validators
import csv


def main_scren():
    print("Welcome to ....")

    main_dict = {
        1: "Sign in",
        2: "Sign up",
        3: "Exit"}

    table = PrettyTable()
    table.field_names = ["Option", "Description"]

    for option, description in main_dict.items():
        table.add_row([option, description])
        table.align["Description"] = "l"

    print(table)

def user_input():
    try:
        n = input("Please selection one of the followings: ")
        while n not in ["1","2","3"]:
            n = input("Please selection one of the followings: ")
    except ValueError or KeyError:
        n = input("Please selection one of the followings: ")

    if n == "1":
        sign_in()
    elif n == "2":
        sign_up()
    elif n == "3":
        print("Thank You! See You again soon!")
        sys.exit(0)

def read_csv():
    filepath = os.path.join(os)
    user_data = []
    with open("user_datbase.csv", "r") as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            user_data.append(row)
    return user_data

def sign_in():
    user_data = read_csv()
    while True:
        email = input("email: ")
        password = input("password: ")
        for record in user_data:
            if record["email"] == email and record["password"] == password:
                print("Welcome back!")
        print("Invalid email or password")

def main():
    main_scren()
    user_input()


if __name__ == "__main__":
    main()

