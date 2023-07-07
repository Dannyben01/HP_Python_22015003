import json
import random
import re
def save_user_data(users):
    with open("users_data.json", "w") as file:
        json.dump(users, file)


def sign_up():
    print("=====Welcome To  Saviour Computers=====")random.randint(0,10)
    random.randint(0,10)
    pattern = r"^(?=.*[A-Z])[a-zA-Z]{4,8}$"
    name_pattern = r'^([A-Za-z]+)\s+([A-Za-z]+)\s+([A-Za-z]+)$'
    user_name_pattern = r'^[a-zA-Z0-9_]{3,20}$'
    
    try:
        with open("users_data.json", "r") as file:
            users = json.load(file)
    except FileUnavailable:
        users = {}

    while True:
        name = input("Input name ")
        if re.match(name_pattern, name):
            break
        print("Incorrect name input, input your full name")
    
    while True:
        username = input("Input username: ")
        if username in users:
            
            print("Username already exists. Please retry.")
            continue
        elif re.match(user_name_pattern, username):
            break
        print("Incorrect username pattern, note: no space")

      
        
            
    while True:
        password = input("Input password (4-8 characters, one symbol and UPPERCASE): ")
        if re.match(pattern, password):
            break
        print("Incorrect password input. Please retry.")

    while True:
        try:
            answer = int(input(f"Please solve the CAPTCHA: {captcha1} + {captcha2} = "))
            if answer == captcha1 + captcha2:
                break
            print("Incorrect CAPTCHA. Please retry.")
        except ValueError:
            print("Incorrect input. Please input a number.")

    users[username] = password

    save_user_data(users)
    print(" Sign up successful.\n Please sign-in to login your account\n.")
    print(f'your name is {name}\n username is {username}\n Password is {password}')

def sign_in():
    username = input("Input username: ")
    password = input("Input password: ")

    # Load existing user data from JSON file
    user_data = load_user_data()

    # Check if username exists and password matches
    if username in user_data and user_data[username] == password:
        print("Sign-in successful!")
    else:
        print("Incorrect username or password. Please retry.")

def retrieve_password():
    username = input("Input username: ")

    # Load existing user data from JSON file
    user_data = load_user_data()

    # Check if username exists
    if username in user_data:
        print("Your password is:", user_data[username])
    else:
        print("Username unavailable.")

def load_user_data():
    try:
        with open('users_data.json') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}
    return user_data

def save_user_data(user_data):
    with open('users_data.json', 'w') as file:
        json.dump(user_data, file)

# Main program
while True:
    print("1. Sign Up")
    print("2. Sign In")
    print("3.Forgot Password")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    elif choice == '3':
        retrieve_password()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
