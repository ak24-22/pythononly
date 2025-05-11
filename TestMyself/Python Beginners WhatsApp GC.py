# day 1: Write a script that prints your name and favorite hobby

# name = "Abdul-Kareem"
# hobbs = "Playing games & Watching movies/Dramas/Animation"

# print(f"Hello, my name is, {name}, and my hobbies are, {hobbs}")

# day 2: Create a profile generator

# name = "Abdul-Kareem"
# age = 26
# sex = "male"
# Phone_No = "07547309186"

# print(name)
# print(age)
# print(sex)
# print(Phone_No)

# Exercise: Store and display user details

# person_name = "Ak"
# person_age = 26
# email_address = "akareem.ali5@gmail.com"
# program_lang = "python"

# print(person_name)
# print(person_age)
# print(email_address)
# print(program_lang)


# Challenge: Simple Calcculator  

# num1 = float(input("Enter A Number: "))
# num2 = float(input("Enter Another Number: "))
# op = input("Enter An Operator: ")

# if op == "+":
#      print(num1 + num2)
# elif op == "-":
#      print(num1 - num2)
# elif op == "*":
#      print(num1 * num2)
# elif op == "/":
#      if num2 == 0:
#          print("You can't divide by zero")
#      else:
#          print(num1 / num2)
# else:
#      print('Invalid Operator')

# day 3: Create an Age Calcculator  

# option 1
# bornyear = int(input("Enter the year you were born in: "))
# age = 2025 - bornyear

# print(f"you are {age} years old!")

# option 2
# year_born = int(input("Enter the year you were born in:"))
# month_born = int(input("Enter the month you were born in (1-12):"))
# day_born = int(input("Enter the day in the month you were born in (1-31):"))

# present_year = 2025
# present_month = 4
# present_day = 19

# specific_age =  present_year - year_born
# month_left = present_month - month_born
# day_left = present_day - day_born

# if month_born > present_month or month_born == present_month and day_born > present_day:
#     specific_age -= 1 
#     if day_born < present_day: 
#         month_left += 12 
#     print(f"you are {specific_age} years old!\nTheres {month_left} months left and {day_left} days for your bday")
# elif month_born == present_month and day_born == present_day:
#     print(f"you are {specific_age} years old!\nToday is your bday")
# else:
#         print(f"you are {specific_age} years old!\nTheres {month_left} months left and {day_left} days for your bday")


# # day 4 string slicing

# slice 1
# p = "snake"
# print(p[::-1]) 
# print(p) 

# slice 2
# s = "Hello, Python"
# print(s[0:5])

# Day 6: Control Flow (if-elif-else)

# Example: Check if a number is even or odd

# num = 2
# if num % 2 == 0:
#     print ("Even")
# else:
#     print("Odd")

# Exercise: Validate user age for voting eligibility

# vote_age = int(input("Enter Your Age: "))
# if vote_age >= 18 and age < 121:
#     print("You Can Vote because you are over the age requirement!")
# elif vote_age > 12 and age < 17:
#     print("You Cannot Vote because you have met the conditions")  
# else:
#     print("Please Enter An Appropriate Age ") 

# Challenge: Build a simple login system

# u = "AKa111"
# p = "PASSWORD"
# usersname = input("Enter Username: ")
# password = input("Enter Password: ")

# if usersname == u and password == p:
#     print("Logging in...")
# elif usersname != u and password == p:
#     print("Wrong Username. Please Try Again!")
# elif usersname == u and password != p:
#     print("Wrong Password. Please Try Again!")
# else:
#     print("Wrong Username and Password. Please Try Again!")

# Day 7: Weekly Challenge - Create a mini form that collects user details, checks for empty inputs, and prints a summary

# my mini form: how to get in touch
# f_name = input("Enter Your First Name: ")
# l_name = input("Enter Your Last Name: ")
# email = input("Enter Your Email Address: ")
# phone_num = int(input("Enter Your Phone Number: "))

# if f_name == "":
#     print("Please Enter your First Name")
# else:
#     print(f_name)
# if l_name == "":
#     print("Please Enter your Last Name")
# else:
#     print(l_name)
# if email == "":
#     print("Please Enter your Email Address")
# else:
#     print(email)
# if phone_num == "":
#     print("Please your Phone Number")
# else:
#     print(phone_num)

# mini_form = [f_name , l_name , email , phone_num]

# print(f"Summary of your details {mini_form}")

# Day 8: Loops (for, while)
# - Example: Loop through numbers and lists

# i = 1
# while i <= 5:
#     print(i)
#     i+=1

# - Exercise: Print the first 10 multiples of a number

# j = 2
# while j <= 20:
#     print(j)
#     j+= 2

# - Challenge: Build a countdown timer

# n = 10
# while n >= 1:
#     print(n)
#     n-= 1
# print("TIME IS UP!!!")

# option 2

# import time
# secs = int(input("Enter the countdown in seconds: "))

# for i in range(0,10):
#     print(i)
#     time.sleep(1)

# print("TIME IS UP!!!")

# Day 9: Loop Control Statements (break, continue)
# - Example: Skip even numbers in a loop

# p = 1
# while p <= 20:
#     print(p)
#     p+=2


# g = 10
# while g > 0:
#     print(g)
#     g -= 1
# print("GO!!!")

# Extra Loop task: go down in 2s e.g. 24,22,20,18, etc

# x = 24
# while x > 0:
#     print(x)
#     x -= 2

# - Exercise: Print all vowels in a string

# alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# vowels = ["a", "e", "i", "o", "u"]

# for letter in alphabet: 
#     if letter in vowels:
#         print(f"{letter} is a Vowel")

# - Challenge: Create a number guessing game

# secret_num = 90
# user_guess = ""
# num_of_guess = 0
# limit_guess = 5
# out_of_guesses = False

# while secret_num != user_guess and not out_of_guesses:
#     if num_of_guess < limit_guess:
#         user_guess = int(input("Guess the Number: "))
#         num_of_guess += 1
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("Out of Guesses, You Lose!")
# else:
#     print("You Win!")

# hangman game

# secretWord = "cat"
# guessLetter = ""
# guessCount = 0
# guessLimit = 10
# outOfGuesses = False

# while secretWord != guessLetter and not outOfGuesses:
#     if guessLimit < guessCount:
#         guessLetter = input("Guess the Letter")
#         guessCount += 1 
#     else:
#         outOfGuesses = True

# if outOfGuesses:
#     print("Out Of Guesses, You Lose!")
# else:
#     print("You Win!")
# Day 10: Functions & Parameters

# - Example: Create a function that adds two numbers

# def add2nums(num1, num2):
#     return num1 + num2

# print(add2nums(44, 55))

# - Exercise: Write a function that returns the square of a number

# def square_num(num):
#     return num * num

# print(square_num(5))

# - Challenge: Build a simple unit converter
                                    
# def converter():
#     print("Remember, for length m/cm 1 times 100 and for mass kg/g 1 times 1000")
   
#     convert_type = input("What do you want to convert? ")
    
#     num = float(input("Enter Number: "))
  
#     if convert_type == "length":
#         result = num * 100
#         print(f"{result}cm")
#     elif convert_type == "mass":
#         result = num * 1000
#         print(f"{result}g")
#     else:
#         print("Invalid Converter")

# converter()

# Extra Loop tasks

# task 1










# Day 11: Built-in Functions & Scope

# - Example: Use len(), max(), and min()

# word = "WindowsOS"
# print(len(word))
# print(min(99,999))
# print(max(99,999))

# - Exercise: Find the largest number in a list

# num_list = [12, 0.34, 0.5, 66/100]
# print(max(num_list))

# - Challenge: Implement a basic tax calculator

#  the tax calculation formula:
#  Tax rate = (Tax amount/Price before tax) × 100% 
# eg 5/20 × 100% = 25%.

# def taxCalc():
#     try:
#         tax_amount = float(input("Enter Tax Amount: "))
#         price_b4_tax = float(input("Enter Price Before Tax: "))

#         if price_b4_tax <= 0:
#             print("ERROR! The price before tax can't be 0")
#         else:  
#             taxRate = (tax_amount/price_b4_tax) * 100
#             print(f"The Tax Rate is {taxRate:.2f}%")

#     except ValueError:
#         print("ERROR! Please Enter Numbers Only!")
# taxCalc()



# Day 12: Lists & Tuples

# - Example: Store and retrieve student names

# student_names = ["Jack Reacher", "James Bond", "Jason Bourne", "Alex Rider",]
# print(student_names)
# - Exercise: Sort a list of numbers

# listnums = [5, 6, 378, 9, 1, 0, 2, 7]
# listnums.sort()
# print(listnums)

# - Challenge: Create a to-do list app

# print("My To Do List")
# new_task = input("New Task? (Enter: y/n) ")
# tasks = []
# while new_task == "y":
#     task = input("Task: ")
#     date = input("Date: ")
#     time = input("Time: ")
#     new_task = input("New Task? (Enter: y/n) ")
#     tdt=[task, date, time]
#     tasks.append(tdt)
# if not tasks:
#     print("No Tasks Today")
# else:
#     print("All Tasks:")
#     for t in tasks:
#         print(t)

# Day 13: Dictionary Basics

# - Example: Store and retrieve student data
student_data = {
    "Name" : "Sufyan Ali",
    "Age" : 14,
    "DOB" : "26/05/11",
    "Phone No." : "+447796360451"
}
print(student_data)

# - Exercise: Count word occurrences in a sentence

# - Challenge: Build a simple contact book



