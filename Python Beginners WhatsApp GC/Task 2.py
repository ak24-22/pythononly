# -	Day 2: Variables & Data Types

# -	Example: Assign values to variables

num1 = 5
num2 = 5
print(num1 + num2) 

# -	Exercise: Store and display user details

name = "Barry Allen"
age = 26
email = "theflash@jl.com"
phone = "07547309186"
dob = "11/11/98" 
address = "London"

user_details = {
    "Name": name,
    "Age": age, 
    "Email": email, 
    "Phone No": phone, 
    "DOB": dob, 
    "Address": address
}

for key, value in user_details.items():
    print(f"{key}: {value}")

print("\n")

# -	Challenge: Create a profile generator
def profile_generator():

    print("\nPlease fill in the details below.\n")
    
    ufname = input("Enter your first name: ")
    ulname = input("Enter your last name: ")
    uage = int(input("Enter your age: "))
    uphone = input("Enter your phone number: ")
    udob = input("Enter your date of birth: ")
    upemail = input("Enter your primary email: ")
    usemail = input("Enter your secondary email: ")
    uhaddress = input("Enter your home address: ")
    
    print("\n")
    
    profile = {
    "First Name": ufname, 
    "Surname": ulname, 
    "Age": uage, 
    "Phone Number": uphone,
    "Date of Birth": udob,
    "Primary Email": upemail,
    "Secondary Email": usemail,
    "Home Address": uhaddress
    }
    print("\n--- User Profile ---")
    for keys, values in profile.items():
        print(f"{keys}: {values}")



limit = 0

while limit < 5:
    create_profile = input("Do you want to create a profile? (Enter y/n): ").lower()

    if create_profile == "y":
        profile_generator()
        limit+=1
    elif create_profile == "n":
        print("Bye!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

if limit == 5:
        print("Cannot create anymore profiles")
