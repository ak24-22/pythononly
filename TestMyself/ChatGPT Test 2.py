# 1. VARIABLES & DATA TYPES

# 1️⃣ Basic: Store your name, age, and favorite color in variables and print them.

name = "AK"
age = 22
fav_colour = "Blue"

print(f"Hey, my name is {name}, and I am {age} years old. My fav colour is {fav_colour}")

# 2️⃣ Slightly Harder: Ask the user for their birth year and calculate their age.

birth = int(input("Enter the year you were born in: "))

user_age = 2025 - birth

print(f"You are {user_age} years old")

# 3️⃣ Medium: Swap the values of two variables without using a third variable.

a = 22
b = 44

a,b = b,a

print(a, b)

# 4️⃣ Challenging: Ask the user for the length and width of a rectangle, then calculate and print the area and perimeter.

# option 1
length = float(input("Enter a number: "))
width = float(input("Enter another number: "))

area = length * width
perimeter = 2 * (length + width)
 

print(f"The area of a rectangle is {area}")
print(f"The perimeter of a rectangle is {perimeter}")

#option 2
def calcap():
    length = float(input("Enter a number: "))
    width = float(input("Enter another number: "))
    
    area = length * width
    perimeter = 2 * (length + width)

    return area and perimeter
calcap(area and perimeter)



# 5️⃣ Tricky: Create a simple currency converter that converts dollars to another currency using a fixed exchange rate.

currency = input("Enter the currency: ")
amount = float(input("Enter your price: "))
currency_conversion = input("Enter the currency you want to convert it to: ")

exchange_rates = {
    "GBP-USD" : 0.50,
    "USD-GBP" : 5.00,
    "EUR-GBP" : 0.90,
    "GBP-EUR" : 1.00,
    "EUR-USD" : 2.50,
    "USD-EUR" : 3.00
}

currency_pair = f"{currency}-{currency_conversion}"

if currency_pair in exchange_rates:
    converted_amount = amount * exchange_rates[currency_pair]
    print(f"{amount} {currency} is equal to {converted_amount:.2f} {currency_conversion}")
else:
    print("Sorry, That currency is not available.")
#=======================================================================

# 2. USER INPUT

# 1️⃣ Basic: Ask the user for their name and greet them.

user_name = input("Enter Name: ")

print(f"Hello, {user_name}!")

# 2️⃣ Slightly Harder: Ask for two numbers and print their sum, difference, product, and quotient.

number_1 = int(input("Enter A Number: "))
number_2 = int(input("Enter Another Number: "))

sum = number_1 + number_2
difference = number_1 - number_2
product = number_1 * number_2
quotient = number_1 / number_2

print(sum)
print(difference)
print(product)
print(quotient)

# 3️⃣ Medium: Ask for a number and determine if it is even or odd.

nums = int(input("Enter A Number: "))

if nums % 2 == 0:
    print("True")
else:
    print("Odd")

# 4️⃣ Challenging: Create a simple tip calculator that asks for a bill amount and tip percentage, then calculates the total amount.

def tip_calc():
    bill_amount = float(input("Enter Your Bill: "))
    tip_percent = float(input("Enter Your Tip as a percentage, e.g. 10%: "))

    tip_amount = (tip_percent / 100) * bill_amount
    total_amount = tip_amount + bill_amount

    print(f"Tip: ${tip_amount:.2f}")
    print(f"Total bill: ${total_amount:.2f}")

tip_calc()

# 5️⃣ Tricky: Ask the user for their age, then tell them how many days, hours, and minutes they've lived.

users_age = int(input("Enter Age: "))

days = users_age * 365
hours = users_age * 24
minutes = users_age * 60

print(f"You have lived for {days} days,{hours} hours and {minutes} minutes!")

#=======================================================================

# 3. CONDITIONAL STATEMENTS (IF, ELSE, ELIF)

# 1️⃣ Basic: Ask the user for a number and check if it’s positive, negative, or zero.

user_num = int(input("Enter A Number: "))

if user_num % 2 == 0:
    print("True")
else:
    print("False")

# 2️⃣ Slightly Harder: Ask for a password and check if it matches a pre-set password.

preset_password = "JBourne47"

user_password = input("Enter Password: ")

if user_password == preset_password:
    print("Access Granted!")
else:
    print("Access Denied!")


# 3️⃣ Medium: Create a simple grade calculator that takes a score and assigns a letter grade (A, B, C, etc.).

#Easy option

score = int(input("Enter score: "))

if score == 100:
    print("A*")
elif 90 <= score <= 99: # means score >= 90 and score <= 99
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
elif 50 <= score <= 59:
    print("E")
elif 40 <= score <= 49:
    print("F")
elif 30 <= score <= 39:
    print("G")
else:
    print("U")

#Hard option

grades = {
    range(100, 101) : "A*",
    range(90, 100) : "A",
    range(80, 90) : "B",
    range(70, 80) : "C",
    range(60, 70) : "D",
    range(50, 60) : "E",
    range(40, 50) : "F",
    range(30, 40) : "G",
    range(0, 30) : "U"
}

score = int(input("Enter score: "))

for grades_range, letters in grades.items():
    if score in grades_range:
        print(f"Your grade is {letters}")
        break

# 4️⃣ Challenging: Ask the user for the current temperature and suggest what to wear based on the weather.

season = input("What's the weather? Type the season: ")

if season == "winter":
    print("Wear warm clothes, it will be cold")
elif season == "summer":
    print("Wear light clothes, it will be hot")
elif season == "autumn":
    print("Wear waterproof clothes, it will be all wet when you go out")
elif season == "spring":
    print("Wear light clothes but a bit warm, it will be bit cold but mostly warm")
else:
    print("Not a season")    

# 5️⃣ Tricky: Create a basic login system where a user must enter a correct username and password to "log in."

username = input("Username: ")
password = input("Password: ")

log_username = "aka900"
log_password = "airborne"

if username == log_username and password == log_password:
    print("Logging in...")
else:
    print("Please try again")



#=======================================================================
# 4. LOOPS (FOR, WHILE)

# 1️⃣ Basic: Print numbers from 1 to 10 using a loop.

for index in range (1, 11):
    print(index)

# 2️⃣ Slightly Harder: Ask for a number and print its multiplication table up to 10.

numbers = int(input("Enter A Number:"))

for index in range(0, 12):
    print(f"{numbers} x {index} = {index * numbers}")

# 3️⃣ Medium: Create a countdown timer that counts down from 10 to 1, then prints "Blast off!"

for i in range(10, 0, -1):
        print(i)
print("Blast Off!")

# 4️⃣ Challenging: Ask for a number and print all even numbers from 1 to that number.

i = int(input("Enter Number:"))
while i < 100:
    i += 2
    print(i)

# 5️⃣ Tricky: Create a number guessing game where the user has to guess a random number between 1 and 10. Give hints if they guess too high or too low.

import random

secret_num = random.randint(1, 10)

while True:
    guess = int(input("Enter A Number To Play A Game: "))

    if guess < secret_num:
        print("Too low! Please Guess Again.")
    elif guess > secret_num:
        print("Too High! Please Guess Again.")
    else:
        print("Congrats! You Have Got The Correct Number!")
        break


#=======================================================================

# 5. FUNCTIONS

# 1️⃣ Basic: Write a function that takes a name as input and prints a greeting.

def greet_user():
    name = input("Enter Name: ")
    print(f"Hello, {name}!")
greet_user()

# 2️⃣ Slightly Harder: Write a function that takes two numbers and returns their sum.

def add2nums(number1, number2):
    sum = number1 + number2
    return sum
print(add2nums(22, 34))

# 3️⃣ Medium: Write a function that checks if a number is even or odd and returns the result.

def num_true():
    user_num = int(input("Enter A Number: "))

    if user_num % 2 == 0:
        print("True")
    else:
        print("False")

num_true()

# 4️⃣ Challenging: Write a function that takes a temperature in Celsius and converts it to Fahrenheit.

# Formula - (°C × 9/5) + 32 = °F

def convert_temp():
    tempC = int(input("Enter Weather: "))
    result = (tempC * 9 / 5) + 32
    return result 

print(convert_temp())

# 5️⃣ Tricky: Write a function that takes a number and returns its factorial (e.g., factorial(5) → 5 × 4 × 3 × 2 × 1 = 120).

# Formula - n! = n x (n-1) x ... x 1

def factorial():
    n = int(input("Enter Number: "))
    result = 1

    for i in range(1, n + 1):
        result *= i
    
    return result 

print(factorial()) 

#=======================================================================

