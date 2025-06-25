# Day 3: Type Conversion & Basic Input/Output

# -	Example: Convert string to integer and vice versa

a1 = "55"      # this is string  
a2 = int(a1)   # this is convering string into Integer

a3 = 55        # this is integer
a4 = str(a3)   # this is convering Integer into string

# -	Exercise: Take user input and display the data type

s = 4
type(s) # type() shows data type but will not print it 
print(type(s))  # Print: <class 'int'>

x=23.32 # this is float
type(x) # type() shows data type but will not print it 
print(type(x))  # Print: <class 'float'>

# -	Challenge: Build a simple age calculator

year_born = int(input("Enter the year you were born in: "))
this_year = int(input("Enter this year: "))

calc_age = this_year - year_born

print(f"You are {calc_age}")
