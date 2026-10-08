# Python Beginner 



Sh1 = "Superman"
Sh2 = "Batman"
Sh3 = "Aquaman"
Batman_Speaks = 'Enough! How many more people are you going hurt?!'
Batman_Thoughts = 'Did he really forgive him? Or is he planning a something, a quick counter attack...?'
Krypt_Btrng_num = 15

print(f"{Sh2} stopped {Sh1} from killing {Sh3} and innocent people by throwing {Krypt_Btrng_num} Kryptonite Batarang. {Sh2} said, {Batman_Speaks.upper()}\n{Sh3} forgave {Sh1}, but {Sh2} was skeptical suspicious, thinking to himself {Batman_Thoughts}")

print(len(f"{Sh2} stopped {Sh1} from killing {Sh3} and innocent people by throwing {Krypt_Btrng_num} Kryptonite Batarang.{Sh2} said, {Batman_Speaks.upper()}\n{Sh3} forgave {Sh1}, but {Sh2} was skeptical suspicious, thinking to himself {Batman_Thoughts}"))

phrase = "Shrek Academy"
print(phrase.replace("Shrek", "Monster"))

print(Batman_Speaks[5])
print(Sh1[4])

print(Batman_Speaks.index("H"))

fav_num = 3
print(str(fav_num) + " is my favourite number!") # use str() when concatenation

print(pow(7,2)) # base, exponents (indices) eg num=7  x two 7s so 7 x 7 = 49 
print(pow(6, 2, 3)) # base, exponents (indices) and Modulus (%)
print(max(2,4))
print(min(0.050,0.103))
print(min(0.005,-0.003))
print(round(3.4))
print(round(3.5))
print(round(4.7))

# All math functions use --> "from math import *", it can override certain functions
# Specific math functions --> "from math import floor, ceil, sqrt"
from math import floor, ceil, sqrt
print(floor(12.5))
print(ceil(12.5))
print(sqrt(81))

name = input("Enter your name: ")
print(f"Good evening, {name}!")

characters = ["Gu Xun'er", "Cai Lin", "Ya Fei", "Xiao Yan", "Tang San", "Xiao Wu", "Dai Mubai", "Oscar", "Tanjiro", "Iron Man"]
print(characters[0:8]) # starts at 0 goes 8th value in list but doesn't include it, printing 7th value Oscar

tv = ["BTTH", "SL", "DS", "AA"]

Takeway_food = ["Pizza", "Burgers", "Chicken & Chips", "Subs", "Wraps", "Hot Dogs", "Kebab Rolls"]
print(Takeway_food[-1]) # prints backwards starts with -1 as the first value
currys = ["Butter Chicken", "Nihari", "kofta", "chicken curry", "lamb curry", "kebab curry", "aloo goobee"]

characters.extend(tv)
Takeway_food.append(currys) 
# append adds another list, 2 separate lists in 1 making it a nested list 
# extend joins the 2 list into 1 list, merging them together 

characters.insert(8, "Mikasa") # becomes 8th value and pushes everything after it, to the right. Only add 1 value (index, Object)  

currys.remove("Butter Chicken") # removes a chosen value from the list. if value repeated in list, 1st value is deleted
# currys.clear() deletes everything in the list
tv.pop() # removes the last item in the list 
print(tv.index("DS")) # finds the item in the list and prints the number
# currys.counts() a checks how many times a chosen value from the list, is repeated 
characters.sort() # sorts the list in ascendding order 
print(characters) # use the .sort() method first to print the list in asendding order
characters.reverse() # flips the order
print(characters) # # use the .reverse() method first to print the list in the flipped order
donghua_females = ["Gu Xun'er", "Cai Lin", "Ya Fei", "Xiao Wu"]
donghua_males = ["Xiao Yan", "Tang San", "Dai Mubai", "Oscar"]

donghua_characters = donghua_males + donghua_females
# create variables with lists

print(Takeway_food)
print(characters)
print(donghua_characters)

coordinates = (66,67) # tuples can not be changed, deleted or modified, i.e they are immutable
print(coordinates[1])
mapx = [(66,67),(3,5),(89,5)]
print(mapx[1][0])

# tuples use () and lists use []
def say_hi(name,age):
    print("Hello " + name + ", you are " + str(age) + " years old!" )

say_hi("Tony",36)



def favfood(username,fav_food):
    return f"{username} favourite food is {fav_food}!"

username = input("Enter You Name: ")
fav_food = input("Enter Your Favourite Food: ")
user_fav_food = favfood(username,fav_food)

print(user_fav_food)

def base_x_exponent(base,exponent):
    result = base ** exponent
    return f"{base} x {exponent} = {result}"

base = float(input("Enter a number (Base): "))
exponent = float(input("Enter another number (for Exponents or Indices): "))
answer = base_x_exponent(base,exponent)

print(answer)

numbers_one = 12
if numbers_one >= 12:
    print("You can play")
else:
    print("Not ellegible to play")


def calc(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*" or op == "x": # or use Membership Operator e.g. op in ["*", "x"] if you have more 2 options
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Can't divide by 0"
        return num1 / num2
    else:
        return "Invalid Operator. Select: +, -, *, / " 

try:
    num1 = float(input("Enter A Number: "))
    num2 = float(input("Enter Another Number: "))

except ValueError:
    print("Numbers or Decimal Numbers Only")
    exit()

op = input("Enter An Operator: ")

calc_answer = calc(num1, op, num2) 

print(calc_answer)

daysConvert = {
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday"
}

print(daysConvert.get(8, "Not a day"))

monthConvert = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}

print(monthConvert["Oct"]) # .get() is better

i = 0

while i <= 10:
    print(i)
    i += 1 # 0 + 1 = 1

print("Finished listing 0 to 10\n")

k = 10

while k>= 0:
    print(k) 
    k-= 1 # 10 - 1 = 9

print("Finished listing 10 to 0")


secret_word = "Pizza"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter the secret word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You Lose! You Are Out Of Guesses!")
else:
    print("Well Done! You Have Guessed The Word!")

h = 5

while h >= 1:
  print(i)
  h-=1
print("Blast Off!")



n = int(input("Enter A Number: "))

j = 1
total = 0

while j <= n:
  total += j
  j += 1

print(total)  



secret = "Deadman"
password = input("Enter Password: ")

while password != secret:
  print("Access Denied! Try Again.")
  password = input("Enter Password: ")
  
print("Access Granted!")
 

l = 0
while l <= 20:
  print(l)
  l+=2

secret_food = "pizza"
limit_guesses = 3
guesses = ""
count_guesses = 0

while guesses != secret_food and count_guesses < limit_guesses:
    guesses = input("Guess the word: ") 
    count_guesses += 1

if guesses == secret_food:
    print("You Win!")
else:
    print("You Lose!")

num = int(input("Enter A Number: "))
tables = int(input("Enter A Multiplication Table: "))
g = 1

while g <= tables:
    print(f"{num} x {g} = {num * g}")
    g+=1

numbers = int(input("Enter a number: "))
count = 0

while numbers > 0:
    numbers = numbers // 10 # numbers //= 10 
    count += 1

print(f"{count} digits")

for letter in "Power Rangers":
    print(letter)


avengers = ["Iron Man", "Captain America", "Hawkeyr", "Hulk", "Black Widow"]

for superhero in avengers:
    print(f"{superhero} is an Avenger")


num_table = int(input("Enter Multiplication Table: "))

for n in range(0, 13):
    print(f"{n} x {num_table} = {n * num_table}")

for index in range(5):
    if index == 0:
        print("First Iteration!")
    else:
        print("Not First Anymore!")

def raise_to_power(base_num, pow_num):
    result =1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2,3))

num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(num_grid[1][1]) # 5

for rows in num_grid:
    for col in rows:
        print(col)


def translate(word):
    translation = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter A Word: ")))

# try/except

# When it applies: User input — they might type anything, Files — might not exist, Networks — might be down, APIs — might return errors and Parsing data — might be corrupt

# When it doesn't: When you can check with an if instead — like your division-by-zero check

# Why: if handles predictable problems (you know the condition to check). try/except handles unpredictable problems (you can't check everything in advance).

# Check calc() function:
# --> The user's input → unpredictable (they could type anything) → use try/except
# --> Division by zero → predictable (you can check if num2 == 0) → use if

# For common operations, you can expect specific errors:

# Operation ============ Common Error
# int("hello") --------- ValueError
# float("abc") --------- ValueError
# int("3.5") ----------- ValueError
# num / 0 -------------- ZeroDivisionError
# my_list[99] ---------- IndexError
# my_dict["missing"] --- KeyError
# open("nofile.txt") --- FileNotFoundError
# undefined_variable --- NameError

# Run the code when errors occur. The last line of the error message tells you the error type.



