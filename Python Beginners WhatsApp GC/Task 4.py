# Day 4: Operators & Expressions

# -	Example: Perform basic calculations
print(5 + 5)
a = 56 
b = -67
type(b) # this is an integer
print(a + b)

# -	Exercise: Use arithmetic operators to calculate BMI

weight_grams = float(input("Enter your weight in gram: ")) # converts g to kg eg 4000g = 40kg
user_weight = weight_grams / 1000
length_metres = float(input("Enter your height in centimetres: ")) # converts cm to m eg 400cm = 4m
user_height = length_metres / 100

calc_bmi = user_weight / (user_height ** 2)

print(f"Your bmi is {calc_bmi}")

# -	Challenge: Create a basic calculator

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
op = input("Enter an operator (+ = Add, - = Subtract, / = Divide, * or x = Times, % = Reminder, ** or ^ = Indices/To the power of):")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*" or op.lower() == "x":
    print(num1 * num2)
elif op == "%":
    print(num1 % num2)
elif op == "**" or op == "^":
    print(num1 ** num2)
elif op == "/":
    if num2 == 0:
        print("Cannot Divide by 0")
    else:
        print(num1 / num2)
else:
    print("Invalid Operator. You must put any of the following: + = Add, - = Subtract, / = Divide, * or x = Times, % = Reminder, ** or ^ = Indices/To the power of")
