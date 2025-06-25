    # Beginner Level – Basics of Loops
# 
# Task 1: Print Numbers
# Use a for loop to print numbers from 1 to 10.
# Use a while loop to print numbers from 10 to 1 (in reverse).
#task
print("1-10 using a for loop")
for p in range(1, 11):
    print(p)

#task
print("10-0 using a while loop")
o=10
while o>=0:
    print(o)
    o-=1
#extra
print("10-0 using a for loop")
for i in range(10, -1, -1):
    print(i)

#extra
print("1-10 using a while loop")
u=0
while u<=10:
    print(u)
    u+=1

# Task 2: Print Even or dOd Numbers
# Use a loop to print all even numbers between 1 and 20.
# Modify to print all odd numbers.

#for loop-even numbers 1-20
for y in range(1,21):
    if y % 2 == 0:
        print(y)

#for loop-odd numbers 1-20
for t in range(1,21):
    if t % 2 != 0:
        print(t)

#while loo[-even numbers 1-20
r=0
while r<=20:
    if r % 2 == 0:
        print(r)
#while loo[-odd numbers 1-20
e=0
while e<=20:
    if e % 2 != 0:
        print(e)

# Task 3: Multiplication Table
# Use a for loop to print the 5 times table up to 12.
# Use a while loop for the same.

num=5
for w in range(1,13):
    print(f"{num} x {w} = {num*w}")
    w+=1

q=1
while q<=12:
    print(f"{num} x {q} = {num*q}")
    q+=1

# Task 4: Countdown Timer
# Ask the user for a starting number and countdown to 0 using while.

a = int(input("Enter a number: "))
while a>=0:
    print(a)
    a-=1


#  Intermediate – Logic and Conditions
# 
# Task 5: Sum of Numbers
# Ask the user for a number n, then use a loop to calculate the sum from 1 to n.

n=int(input("Enter a number: "))
total = 0

for s in range(1, n+1):
    total+=s
sum=(f"sum is {total}")
print(sum)

d=int(input("Enter a number: ")) 
total = 0
f = 1
while f <= d:
    total+=f
    f+=1

add=(f"sum is {total}")
print(add)

#  Task 6: Guess the Number
# Generate a random number and ask the user to guess until they get it right. Use a while loop.

limit = 0

while limit < 5:
    secretnum = int(input("Enter The Secret Number: "))
    limit += 1

    if secretnum == 46:
        print("Correct!")
        break
    elif secretnum >= 40 and secretnum <= 50:
        print("Close!")
    else: 
        print("Wrong number!")

if limit == 5 and secretnum != 46:
    print("Out Of Guesses! The number was 46")

# Task 7: Password Retry
# Let the user enter a password. Give them 3 attempts max using a while loop.

pw = ""
limit = 0

while limit < 5:
    pw = input("Enter Your Password: ")
    limit+=1

    if pw == "Dell":
        print("Logging In...")
        break
    else:
        print("Wrorng Password, try again!")

if limit == 5 and pw != "Dell":
        print("Refresh To reset device")

#  Task 8: Skip Multiples
# Use a for loop to print numbers from 1 to 50 but skip multiples of 3.

#option 1
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)

#option 2
for i in range(1,51):
    if i % 3 != 0:
        print(i)

# Task 9: Average Calculator
# Ask the user to input 5 numbers using a loop. Then calculate and print the average.

#For Loop
total = 0

for i in range(5):
    nums = int(input("Enter Number: "))
    total += nums

average = total / 5
print(f"sum is {total}")
print(f"Average is {average}")

#While Loop
total = 0
j = 1

while j <= 5:
    nums = int(input("Enter Number: "))
    total += nums
    j += 1

average = total / 5
print(f"sum is {total}")
print(f"Average is {average}")


# Advanced – Nested Loops and Patterns
# 
# Task 10: Number Pyramid
# 1
# 12
# 123
# 1234
# Use nested for loops to print this.

rows = 5

for i in range(1, rows + 1):
    for j in range(i, rows + 1):
        print(j, end="")
    print()


# Task 11: Stars Pattern
# *
# **
# ***
# ****
# 
# Then reverse it:
# ****
# ***
# **
# *
# 
# Task 12: Prime Number Checker
# Ask the user for a number and use a loop to check if it’s a prime.
# 
# Task 13: Multiples Finder
# Ask the user for a number n, and find all multiples of n from 1 to 100.

# Challenging – Problem Solving
#
# Task 14: FizzBuzz
# Print numbers from 1 to 100.
# For multiples of 3, print “Fizz”.
# For multiples of 5, print “Buzz”.
# For multiples of both, print “FizzBuzz”.
#
#  Task 15: Factorial Calculator
# Ask the user for a number n, use a loop to calculate n! (n factorial).
#
#  Task 16: Palindrome Checker (no slicing)
# Ask the user for a word. Use a while loop to check if it reads the same forward and backward.
# 
# Task 17: Reverse Digits
# Ask for a number and use a loop to reverse its digits. (e.g., 1234 → 4321)
# 
# Task 18: Number Guessing Game with Score
# Let the user guess a random number between 1-100.
# Keep track of the number of attempts.
# Give hints ("Too high" / "Too low").
