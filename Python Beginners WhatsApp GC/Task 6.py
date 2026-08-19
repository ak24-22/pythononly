# Day 6: Control Flow (if-elif-else)

# -	Example: Check if a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# -	Exercise: Validate user age for voting eligibility

vote_age = int(input("Enter your age: "))

if vote_age >= 18:
    print("You are allowed to vote")
else:
    print("You are not allowed to vote") 

# -	Challenge: Build a simple login system

fname = input("Enter your first name: ").upper()
lname = input("Enter your last name: ").upper()
yrborn = input("Enter the year year were born in: ")
correct_pw = "password"
correct_uname = fname[0]+lname[:3]+yrborn[-2:]

print("\nLog In with your Username and Pasword\n")

username =input("Username: ")
password = input("Password: ")

if username == correct_uname and password == correct_pw:
    print("Logging In...")
else:
    print("Please check you password or username again")


# extra: better login system

# username
print("Create a new username and password")

fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
yb = input("Enter Year Born: ")

user_name = f"{fname[:3]}{lname[:3]}{yb[-2:]}"

#password

favcolour = input("Enter Favourite Colour: ")
current_year = input("Enter current year: ")
pspecchar = input("Enter a special character or punctuation: ")

pass_word = f"{favcolour}{current_year}{pspecchar}"

print("Login to your account")

username = input("Username: ")
password = input("Password: ")

if user_name == username and pass_word == password:
    print("Logging in...")
elif user_name != username or pass_word != password:
    print("Username or Password is incorrect, please try again")
else:
    print("Invalid Response")

