# Day 5: String Manipulation

# -	Example: Formatting and slicing strings

name = "Bruce Waynw"
lang = "Python"

print("My surname is " + name + " and I am learning, " + lang)
print(f"My surname is {name} and I am learning, {lang}")

print(name[7])
print(name[::-1])


# -	Exercise: Reverse a string using slicing

batman = "I am Batman"

print(batman)
print(batman[::-1])

# -	Challenge: Build a username generator

def username_generator():
        
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    yrborn = input("Enter the year were born in: ")

    print(fname[:3])
    print(lname[-3:])
    print(yrborn[-2:])

    username = fname[:3] + lname[-3:] + yrborn[-2:]

    print(f"Generated Username: {username}")

limit = 0

while limit < 5:
    create_username = input("Do want to create a username? (Enter y/n) ").lower()

    if create_username == "y":
        username_generator()
        limit += 1
    elif create_username == "n":
        print("Bye")
        break
    else:
        print("Invalid response. You must enter y or n")

if limit == 5:
    print("Reached maximum number of usernames")

