# Day 7: Weekly Challenge - Create a mini form that collects user details, checks for empty inputs, and prints a summary

name = ""
while name == "":
    name = input("Enter Name: ")

    if name == "":
        print("Please Enter Your Name")

age = ""
while not age.isdigit():
    age = input("Enter Age: ")   
    if not age.isdigit():
        print("Please Enter Your Age")
age = int(age)

email = ""
while email == "":
    email = input("Enter Email: ")
    
    if email == "":
        print("Please Enter Your Email")

dob = ""
while dob == "":
    dob = input("Enter Date of Birth: ")
    if dob == "":
        print("Please Enter Date of Birth: ")
        

user_details = {
    "Name" : name,
    "Age" : age,
    "Email" : email,
    "Date of Birth" : dob
}


print("Here's a summary:")

for keys, values in user_details.items():
    print(f"{keys}:{values}")