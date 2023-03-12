# CS50 PyConnect

This is my final python project for [Harvard Course](https://www.edx.org/course/cs50s-introduction-to-programming-with-python?index=product&queryID=1fe4a6e8b7406306f3ebcf0870335c3f&position=1) on edx.

PyConnect is a command-line tool that allows users to register, login, and authenticate themselves using an authentication code.

# Features:

- Login: users can login with their email and password, and if the login information matches the records in the database, the user will be authenticated and welcomed to the system.
- Registration: users can register with their first name, last name, email, and password. The system will validate the email address and password, and send an authentication code to the user's email address.
- Authentication: users must authenticate themselves with a 4-digit code sent to their email address. They have 5 attempts to enter the code correctly before they are locked out of the system.
- User data management: user data is stored in a CSV file, and the system reads and writes to this file to manage user data.

# Usage:

1. When you run the PyConnect.py file, you will be presented with a main menu.

2. From the main menu, you can select the following options:
  - Login: enter your email address and password to login.
  - Register: enter your first name, last name, email address, and password to create a new account.
  - Exit: exit the program.

3. If you select Login, you will be prompted to enter your email address and password. If the information matches the records in the database, you will be authenticated and welcomed to the system. If not, you will be prompted to try again.

4. If you select Register, you will be prompted to enter your first name, last name, email address, and password. If the email address and password are valid, an authentication code will be sent to your email address, and you will be prompted to enter the code to authenticate yourself.

5. If you enter an invalid email address or password, you will be prompted to try again.

6. You can exit the program at any time by selecting the Exit option from the main menu.

# Dependencies:
- prettytable: A Python library used to display data in a table format
- validators: A Python library used to validate data such as email addresses
- re: A Python library used for regular expressions
- random: A Python library used to generate random numbers

# Contributing:
Contributions to this project are welcome. If you find a bug or have an idea for a new feature, please create a new issue or submit a pull request.

# License:
This project is licensed under the [MIT License](https://opensource.org/license/mit/).
