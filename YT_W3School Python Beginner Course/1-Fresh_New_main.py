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
num1 = float(input("Enter A Number: "))
op = input("Enter An Operator: ")
num2 = float(input("Enter Another Number: "))

calc_answer = calc(num1, op, num2) 

print(calc_answer)

