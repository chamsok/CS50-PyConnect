from prettytable import PrettyTable
import sys
import csv
import os
import validators
import re
import hashlib
import random

user_data_path = "user_database.csv"

#Function to display the main menu
def main_page():
    print("Welcome to CS50 PyConnect!")

    #Define dictionary of options for main menu
    main_dict = {
        1: "Login",
        2: "Register",
        3: "Exit"}

    #Create a table to display main menu options
    table = PrettyTable()
    table.field_names = ["Option", "Description"]

    for option, description in main_dict.items():
        table.add_row([option, description])
        table.align["Description"] = "l"

    print(table)

#Function to get user input from main menu and execute the corresponding action
def user_input():
    #Get user input fromt the chosen option
    n = input("Please selection one of the followings: ")
    #Validate the input
    while n not in ["1","2","3"]:
        n = input("Please selection one of the followings: ")

    #Execute the corresponding function based on user input
    if n == "1":
        login()
    elif n == "2":
        register()
    elif n == "3":
        print("Thank You! See You again soon!")
        sys.exit(0)

#Function to handle login process
def login():
    #Read user data from CSV file
    user_data = read_csv()
    while True:
        #Validate to make sure the email is in correct format
        while True:
            email = input("Email: ").strip()
            if not validators.email(email):
                print("Invalid email. Please enter a valid email address.")
                continue
            break

        password = input("Password: ").strip()
        for record in user_data:
            #Check if email and password match a record in the CVS file
            if record["email"] == email:
                #Hash the input password and compare with the store hash password
                if record["password"] == hashlib.sha256(password.encode("utf-8")).hexdigest():
                    auth_code()
                    print(f'Welcome back, {record["first_name"]}!')
                    return
        #If no matching record is found, print an invalid message
        print("Invalid email or password")

#Function to handle registration process
def register():
    #Get user input for registeration information
    first_name = input("First Name: ").capitalize()
    last_name = input("Last Name: ").capitalize()
    email = validate_email()
    password = validate_password()
    auth_code()

    #Define the path to the CVS file
    file_path = os.path.join(os.path.dirname(__file__), user_data_path)
    #Write the new user's information to the CSV file
    with open(file_path, "a", newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow([first_name, last_name, email, password])

    print("You have successfully signed up!")

#Function to read user data from CVS file
def read_csv():
    #Difine the path to the CSV file
    file_path = os.path.join(os.path.dirname(__file__), user_data_path)

    #Open and read the csv file
    user_data = []
    with open(file_path, "r") as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            user_data.append(row)
        return user_data

#Function to validate email address
def validate_email():
    #Read user data from CSV file
    user_data = read_csv()
    while True:
        email = input("Email: ").strip()
        #Check if email address already exists in CSV file
        for record in user_data:
            if record["email"] in email:
                print("The email is already existed!")
                email = input("Email: ").strip()
        #Validate the email
        if validators.email(email):
            return email
        print("Invalid Email!")

#Function to validate password
def validate_password():
    while True:
        #Disply password requirements
        print("the password must be:")
        print("- between 6-20 characters")
        print("- at least one uppercase letter")
        print("- at least one lowercase letter")
        print("- at least one digit")
        print("- at least one special charactor(@_.$!#%*?&)")
        #Prompt user to enter the password
        password = input("Password: ").strip()
        #Check if the password meets the requirements and compile it
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@_.$!#%*?&])[A-Za-z\d@_.$!#%*?&]{6,20}$"
        reg_compile = re.compile(reg)

        #Check if the password matches the reg
        if re.search(reg_compile, password):
            password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
            return password_hash
        print("Invalid Password")

#Function to generate an authentication code and prompts user for input
def auth_code():
    #Notify the user that the code is sent
    print("An authentication code has been sent to your email. Please check your inbox.")

    #Generate a radom 4-digit code
    code = str(random.randint(1000, 9999))

    #Display the code to the user
    print(f"The authentication code is {code}")

    #Continuously prompt the user to input the authentication code for 5 times
    for _ in range(5):
        try:
            user_code = input("Please input your code: ").strip()
            if user_code == code:
                print("Authentication successful")
                break
            print("Invalid code")
        except ValueError:
            print("Invalid code")
            continue
    #Exit the system when invalid code more than 5 times
    print("You have exceeded the maximum number of attempts. Please try again later.")
    exit()


def main():
    main_page()
    user_input()


if __name__ == "__main__":
    main()

