# CS50 PyConnect

PyConnect is a command-line tool that allows users to register, login, and authenticate themselves using an authentication code. It is developed as a final project for the [Harvard CS50xP](https://www.edx.org/course/cs50s-introduction-to-programming-with-python?index=product&queryID=1fe4a6e8b7406306f3ebcf0870335c3f&position=1) course on edX.

# Features:

- Login: Users can login with their email and password. If the login information matches the records in the database, the user will be authenticated and welcomed to the system.
- Registration: Users can register with their first name, last name, email, and password. The system validates the email address and password and sends an authentication code to the user's email address.
- Authentication: Users must authenticate themselves with a 4-digit code sent to their email address. They have 5 attempts to enter the code correctly before they are locked out of the system.
- User data management: User data is stored in a CSV file, and the system reads and writes to this file to manage user data.

# Usage:

To run PyConnect, execute the CS50P_PyConnect.py file from the command line. The program will present a main menu with the following options:

- Login: Enter your email address and password to log in.
- Register: Enter your first name, last name, email address, and password to create a new account.
- Exit: Exit the program.
If you select Login, you will be prompted to enter your email address and password. If the information matches the records in the database, you will be authenticated and welcomed to the system. If not, you will be prompted to try again.

If you select Register, you will be prompted to enter your first name, last name, email address, and password. If the email address and password are valid, an authentication code will be sent to your email address, and you will be prompted to enter the code to authenticate yourself.

If you enter an invalid email address or password, you will be prompted to try again.

You can exit the program at any time by selecting the Exit option from the main menu.

# Dependencies:
PyConnect uses the following Python libraries:

- prettytable: A Python library used to display data in a table format
- validators: A Python library used to validate data such as email addresses
- re: A Python library used for regular expressions
- random: A Python library used to generate random numbers

Make sure these libraries are installed before running the program.

# Contributing:
Contributions to this project are welcome. If you find a bug or have an idea for a new feature, please create a new issue.

# License:
This project is licensed under the [MIT License](https://opensource.org/license/mit/).
