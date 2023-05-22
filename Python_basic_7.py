username = "username123"

password = "password123"

user_input_username = input("Enter your username: ")

user_input_password = input("Enter your password: ")

if user_input_username != username and user_input_password != password:

  print("Username and password are incorrect.")

elif user_input_username != username:

  print("Username is incorrect.")

elif user_input_password != password:

  print("Password is incorrect.")

else:

  print("Login Successful")
