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

