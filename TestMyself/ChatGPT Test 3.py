# 1️⃣ Variables & Data Types

# Basic: Store your favorite movie, year of release, and main actor in variables and print them.

movie_name = "Dragon Tiger Gates"
movie_year = 2006
movie_actor = "Donnie Yen"

print(f"My favourite movie is, {movie_name}, and it was released in {movie_year} and one of the main actors is {movie_actor}")


print("\n")

# Slightly Harder: Ask the user for their height in cm and convert it to meters.


user_height = float(input("Enter your height in cm (don't put 2cm just put 2), Height: "))

# using: m = cm / 100
# cm = m * 100 

meters = user_height / 100

print(meters)

print("\n")

# Medium: Swap three variables without using a fourth one (e.g., a → b, b → c, c → a).

a = "11"
b = "22"
c = "33"

#option 1
# a = b # a = 22
# b = a # b = 11
# c = a # c = 11
# c = b # c = 22
# a = c # a = 11
# b = c # b = 33

#option 2
(a, b, c) = (a, c, b) = (b, a, c) = (b, c, a) = (c, a, b) = (c, b, a)


print(a, b, c)

print("\n")

# Challenging: Create a program that takes an amount in minutes and converts it to hours and minutes (e.g., 130 minutes → 2 hours, 10 minutes).

# using: mins = hrs / 60 
# hrs = mins * 60 

hrs = int(input("Enter Time in mins: "))
min = hrs / 60
clock_time = f"{min} hr/s"

print(clock_time)

# Tricky: Create a simple BMI calculator that asks for height (m) and weight (kg) and calculates BMI using BMI = weight / height².

height_m = float(input("Enter Height (m): "))
weight_kg = float(input("Enter Weight (kg): "))
bmi_calc = weight_kg / (height_m * height_m)

print(bmi_calc)

#######################################################################

# 2️⃣ User Input

# Basic: Ask the user for their birth month and print a response (e.g., "You were born in March!").

birth_month = input("Enter the month you were born in: ")

print("You were born in" + " " + birth_month.capitalize() +"!" )

# Slightly Harder: Ask for two numbers and print their average.

num1 = float(input("Enter A Number: "))
num2 = float(input("Enter Another Number: "))
average = (num1 + num2) / 2

print(average)

# Medium: Ask for a distance in kilometers and convert it to miles (1 km = 0.621371 miles).

distance = float(input("Enter how far the distance is (km): "))

home_school = distance * 0.621371

print(f"{home_school} miles")

# Challenging: Ask for the  user's first and last name separately, then print their initials.

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

print(f"You Initials Are: {first_name[0].capitalize()} {last_name[0].capitalize()}")

# Tricky: Ask for a number and check if it's prime (A prime number is only divisible by 1 and itself).

num = int(input("Enter A Number To If It Is A Prime Number or Not: "))

for i in range(2, num):
    if num % 1 == 0:
        print("It's Not A Prime Number!")
        break
    else:
        print("Yes, It's A Prime Number")


########################################################################

# 3️⃣ Conditional Statements (if, else, elif)

# Basic: Ask the user for a number and tell them if it's positive, negative, or zero.

user_number = float(input("Enter Number: "))

if user_number > 0:
    print("Positive")
elif user_number < 0:
    print("Negative")
else:
    print("Zero")

# Slightly Harder: Check if a given year is a leap year (A leap year is divisible by 4 but not 100, unless also divisible by 400).

year = int(input("Enter A Year: "))

if (year % 4 == 0  and not year % 100 == 0 ) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year") 

# Medium: Create a program that asks for a score and assigns a letter grade (A-F).

grades = {
    range(100, 101) : "A",
    range(80, 99): "B",
    range(60, 79) : "C",
    range(40, 59) : "D",
    range(20, 39) : "E",
    range(0, 19) : "F"
}

score = int(input("Enter Score: "))

for grades_range, letter in grades.items():
    if score in grades_range:
        print(f"Your grade is {letter}")
        break


# Challenging: Ask for three numbers and determine the largest.

z = 12
x = 65
y = 9
print(max(x,y, z))

#: Tricky: Create a simple text-based rock-paper-scissors game where the user plays against the computer.

import random

options = ("rock", "papers", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter Choice: (rock, papers or scissors): ")

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("TIE")
        elif player == "rock" and computer == "scissors":
            print("YOU WIN!")
        elif player == "paper" and computer == "rock":
            print("YOU WIN!")
        elif player == "scissors" and computer == "paper":
            print("YOU WIN!")
        else:
            print("YOU LOSE!")
        
        if not input("Play Again? (y/n): ").lower() == "y":
            running = False

print("Thanks for playing")


########################################################################

# 4️⃣ Loops (for, while)

# Basic: Print numbers from 1 to 20.

i=1
while i<= 20:
    print(i)
    i+=1

# Slightly Harder: Print the sum of all even numbers from 1 to 50.

total = 0
n = 1
while n <= 50:
    print(n)
    if n % 2 == 0:
        total += n
    n += 1
print(f"Sum of all is {total}")

# Medium: Print the multiplication table for a user-given number.

num = int(input("Enter a number: "))
#1
for x in range(0, 11):
    total = x * num
    print(f"{x} x {num} = {total}")

 #2   
# for x in range(0, 11):
#-----print(f"{x} x {num} = {x * num}")



# Challenging: Print all prime numbers between 1 and 100.

for p in range(1, 101):
        if p > 1:
            is_prime = True

            for j in range(2, int(p ** 0.5) +1 ):
                if p % j == 0:
                    is_prime = False
                    break
            if is_prime:
                print(p)



# Tricky: Create a program that repeatedly asks for a password until the user enters the correct one.

pw = "chat ai"
password = input("Enter Password: ")


# while True:
#     for password in pw:
#         password = input("Enter Password: ")
#     if password == pw:
#         print("Logging in...")
#         break
#     else:
#         print("Please Try Again")
# print("Good")




########################################################################

# 5️⃣ Functions

# Basic: Write a function that takes a name and prints "Hello, [name]!"



# Slightly Harder: Write a function that returns the square of a number.



# Medium: Write a function that returns the factorial of a number (Hint: Use n! = n * (n-1) * ... * 1).



# Challenging: Write a function that checks if a string is a palindrome (reads the same forward and backward).



# Tricky: Write a function that takes a list of numbers and returns the second largest number.



########################################################################

# 6️⃣ Lists & Dictionaries

# Basic: Store five of your favorite foods in a list and print them.



# Slightly Harder: Ask the user for five numbers and store them in a list, then print the largest.



# Medium: Create a dictionary where the keys are country names and the values are their capitals.



# Challenging: Ask the user for a sentence and count the occurrences of each word (Hint: Use a dictionary).



# Tricky: Given a list of numbers, return a new list containing only the unique ones.



########################################################################

# 7️⃣ Random & Games

# Basic: Generate and print a random number between 1 and 10.



# Slightly Harder: Flip a virtual coin (randomly print "Heads" or "Tails").



# Medium: Create a number guessing game (user guesses until they get it right).



# Challenging: Simulate rolling two dice and print their sum.



# Tricky: Create a simple text-based dice game where the user rolls against the computer.



########################################################################

# 8️⃣ String Manipulation

# Basic: Ask the user for a word and print it in uppercase.



# Slightly Harder: Reverse a string (e.g., hello → olleh).



# Medium: Count the number of vowels in a sentence.



# Challenging: Ask for a sentence and replace all spaces with hyphens.



# Tricky: Find the most frequent letter in a string.



########################################################################

# 9️⃣ Files (If you want to start working with files)

# Basic: Create a text file and write "Hello, World!" into it.



# Slightly Harder: Ask the user for a message and save it to a file.



# Medium: Read a file and print its contents.



# Challenging: Read a file and count the number of words in it.



# Tricky: Create a simple diary app where the user can add and read entries.



########################################################################