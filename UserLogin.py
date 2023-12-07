import random

while True:
    user_name = input("Enter your username: ")
    if user_name.isdigit():
        print("Need to include alphabets.")
        continue
    else:
        break

user_accept = input("Do you want to generate password? ")
pw = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

if user_accept.lower() == "yes":
    password = "".join(random.sample(pw, 5))
else:
    quit()

print(f"Username: {user_name} : Password: {password}")

attempt = 3
user_attempt = 0

while user_attempt < attempt:
    user_attempt += 1
    user_login = input("Enter your username to login: ")
    user_pw = input("Enter your password to login: ")

    if user_login == user_name and user_pw == password:
        print("Successfully Login!")
        break
    else:
        print("Invalid Login!")
        continue
