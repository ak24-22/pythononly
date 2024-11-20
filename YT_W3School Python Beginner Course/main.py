"""
Following the Course on W3Schools & through YouTube:
https://www.w3schools.com/python/python_intro.asp - Python Introduction
https://www.youtube.com/watch?v=rfscVS0vtbw - Learn Python - Full Course for Beginners [Tutorial)
"""

print("YT Video: Learn Python - Full Course for Beginners [Tutorial) - By freecodecamp.org \n")

print("++++++++++++++++++++++++++++++++++++\n")
#1) PRINTING "HELLO WORLD'
print("1. PRINTING HELLO WORLD'")
print("Hello World!\n")
print('Hello World!') # using ' ' can also be used to print anything


print("""Using these triple quotations allows you to print mulple lines at once""")

a = """ i am thw bes of the bats
oh yh 
dont mess
with me
otherwise 
You
Will
Die
!!!
"""
print(a)

print("++++++++++++++++++++++++++++++++++++\n")
#2) PRINTING SHAPES
print("2.PRINTING SHAPES\n")
print("    /|")
print("   / |")
print("  /  |")
print(" /___|")
print("++++++++++++++++++++++++++++++++++++\n")
print("-----------------------------------¦")
print("Extra Shapes                       ¦")
print("-----------------------------------¦")
print("1.Here is a Square                 ¦")
print("|-----|                            ¦")
print("|     |                            ¦")
print("|_____|                            ¦")
print("-----------------------------------¦")
print("2.Here is a Rectangle              ¦")
print("|-----|                            ¦")
print("|     |                            ¦")
print("|     |                            ¦")
print("|     |                            ¦")
print("|_____|                            ¦")
print("-----------------------------------¦")

print(" \n")

print("++++++++++++++++++++++++++++++++++++\n")
# 3) VARIABLES & DATA TYPES
print("3. VARIABLES & DATA TYPES\n")

# Variables & Data Types: Changing certain information in long codes by using Variables, (e.g. name & age)
# Common Data Types: String (Sentenses/Word/Letter), Inegar(Numbers), Float(Numbers with decimals) & Boolean (True/False)

print("3 different types of variables \n")
print("Camel Case:\n", "Each word is in caps except the 1st and has no spaces\n", "E.g.theBeastIsStrong")
print("Pascel Case:\n", "Each word is in caps and has no spaces\n", "E.g.ShrekSchoolAcademy")
print("Snake Case:\n", "Each word is Separated with '_'\n", "E.g.The_Dark_Knight")
# character_name = "Sasuke" #This a Variable used to change the name from "Alex" to "Sasuke"
# character_age = "33" #This is another variable used to change the age from"25" to "33"

# print("Thee was an old man named " + character_name +", ") #Changing the name from "John" to "Alex"
# print("and he was " + character_age + " years old. \n") #Changing the age from "70" to "25" "\n" can be used to add a new line

# character_name ="Naruto" #Variables can be updated and changed at amytime

# print("He like the name " + character_name +", ") #Changing the name from "John" to "Alex"
# print("and he liked being " +character_age+".\n") #Changing the text from "but he didnt like being 70" to "and he liked being 25"

# is_male = True #Exaple of Boolean

"""
Python has different data types that are built-in
____________________________________________________________________________________________________________________
Type     <==========> Data                          <=====================> Example                                |
____________________________________________________________________________________________________________________
Numeric  <----------> int, float & complex         <----------------------> x = 6
Text     <----------> str                          <----------------------> x = "Spider-Man"
Sequence <----------> list, tuple & range   
Mapping  <----------> dict                                                  x = {"names" : "Jack", "age" : "23"}
Set      <----------> set & frozenset
Boolean  <----------> bool                         <----------------------> x = True
Binary   <----------> bytes, bytearry & memoryview 
None     <----------> NoneType                     <----------------------> x = None 
______________________________________________________________________________________________________________________
**********************************************************************************************************************
Examples of Sequence Types >>
List:  x = ["apples", "bananas", "pears"] 
Tuple: x = ([)"apples", "bananas", "pears")
Range: x = range = (9)
**********************************************************************************************************************
Examples of Mapping Types >>
Set:  x = {"apples", "bananas", "pears"} 
Frozenset: x = ({"apples", "bananas", "pears"})
**********************************************************************************************************************
Examples of Binary Types >>
Byte:       x = b"Hello"
Bytearray:  x = bytearray(2)
Memoryview: x = memoryview(byte(8)




"""

print("++++++++++++++++++++++++++++++++++++\n")
#4) WORKING WITH STRINGS
print("4. WORKING WITH STRINGS")
"""
Escape Character >>
Use  '\" "\' can make a '"###"' or "'###'"appear
Use "\n" to add a new line
Use "\t" to add a a big space, i.e like pressing tab
Use "\r" to make the next word carry on to the next line
Use "\\" to add a single \
Use "\b" to get rid the space, i.e. like pressing backspace
Other uses >>
Form Feed = "\f"
Octal Value = "\ooo"
Hex Value = "\xhh"
***************************************************************
Use "+" in between string to break it up into smaller chunks
Use "," to give small indentation
"""

print("4. WORKING WITH STRINGS\n")
print("You said, \"i am Spider-Mam\"")
print("I said, \"You are Bat-Mam\" \n")

phrase = "Shrek School Academy" #Giving a String a variable and then pringing it
print(phrase + " Are For =\n \"Monsters\"") #taking a string and adding another string to it (aka: Concatenation)
print(phrase.lower()) #this is a function that changes the string or text to lower case.
# To make it all upper case just put phrase.upper()
print(len(phrase)) #This Function tells us how many characters are in the string (I.E. The Length
print(phrase[0]) #This function tells you what the character number. These strings start at 0 and contibue
print(phrase.index("S")) #This function finds the letter in the string and prints it as a number.
## If the letter is not in the string and it is printed it will show an error.
print("\n")
movie = "dark knight"
print(movie)
print(movie.isupper()) #This function is True/False so Boolean
print(movie.upper().isupper()) #This function converts the String to all caps than says it is true
print(movie.replace("dark","moon")) #Changes a selected word for something else

quantity = 5
items = 654
price = 30.00
myorder = "I want to pay {2} pounds for {1} pieces of items {0}"
print(myorder.format(quantity, items, price)) #This function will one main variable and then add the others in the places you choose by using "{}"

print("++++++++++++++++++++++++++++++++++++\n")
#5) WORKING WITH NUMBERS
print("5. WORKING WITH NUMBERS\n")
#Python can print any number types
print(43)
print(36.321)
print(-56)
print(3-1*5+2/4) #Python can do complex equations
print(3-1*(5+5)/4)
num_1 = -4 #to name a variable with 2 or more words add an "_" between each word
print(num_1)
print(num_1 + 4) #To add from the variable it has to be insiide the brackets (parentheses)
print("\n")
#NUMBER FUNCTIONS
print("NUMBER FUNCTIOBS")
print(str(num_1) + " is fantasic") #Using the "str" function alllows the numbers to transform into a string
print(abs(num_1)) #abs stands for absolute value, so the absolute value of -4 is 4
print(pow(num_1 , 4)) #pow stands for power of
print(pow(6 , 4))
print(max(2 , 9)) #Prints out the biggest number in the list, to bring out the smallest number use the function min
print(min(2 , 9))
print(round(1.9)) #this rounds up decimal numbers
from math import * #this gives access to more maths fuctions
print(floor(3.5)) #pring the smaller number
print(ceil(10.9)) #print the bigger number
print(sqrt(4)) #print the square toot
print(10 % 3) #The "%" are knows as mods withe prints the remainder oonly

"""
Different Operators
-------------------
Arithmetic:
-----------
+ adds
- subracts
* times
/ Divides
** Exponnentiation
// Floor Division

Comparison:
-----------
== Equal 
!= Not Equal 
> Greater Than
< Less Than
>= Greater Than or Equal
<= Less Then or Eqaul

"""

print("++++++++++++++++++++++++++++++++++++\n")
#6) GETTING INPUT FROM USERS
print("6. GETTING INPUT FROM USERS\n")
name = input("Who are you? ") #The function "input" allows the user to interaction with the program
print("Nice to meet you, " + name + "!" )
age = input("Okay,nice. How old are you?: ")
print("No way, you are only," + age + "!" )

print("++++++++++++++++++++++++++++++++++++\n")
#7) BUILDING A CALCULATOR
print("7. BUILDING A CALCULATOR\n")
num1 = input("Enter a Number: """)
num2 = input("Enter a Number :""")
result = float (num1) + float(num2)
print(result)

print("++++++++++++++++++++++++++++++++++++\n")
#8) MAD LIBS GAME
print("8. MAD LIBS GAME\n")
movie = input ("Enter Fav Movie: ")
TV = input("Enter Fav TV Show: ")
character = input ("Enter Fav Character: ")
print(movie + "is my favourite movie")
print(TV + "is my favourite TV Sgow")
print(character + "is my favourite Character")

print("++++++++++++++++++++++++++++++++++++\n")
#9) LISTS
print("9. LISTS\n")
print("Lists are used  t organise and structure  large amounts of data")
Superheros = ["Spider Man" , "Iron Man" , "Captain America" , "Hawkeye" , "Black Widow" , "Falcon" , "Hulk"] #Square brackets are used to hold a list of data in python. it can also hold  other types  of data like strings and/or boolean and/or numbers
# index starts at 0 in python, however if you want select the data from the back of the list it starts at !-1

print(Superheros[0])   #this will print the first index which is Spiderman
print(Superheros[-1])  #this will print the last index which is Hulk  pring this as -1 tells python that i want to satart from the back
print(Superheros[1:])  #this will print out the list staring from iron man
print(Superheros[2:5]) #This will print out everything from captian america to but not including falcon
Superheros[0] = "Thor" #Modifying and changing a selected data in the list, so i changed the first index, which starts from 0 so it's spiderman to thor
print(Superheros[0])

print("++++++++++++++++++++++++++++++++++++\n")
#10) LIST FUNCTIONS
print("10. LISTS FUNCTIONS\n")

Football_Numbers = [10 , 11 , 7 , 9 ,8 ,1]
Avengers = ["Iron Man" , "Captain America" , "Hawkeye" , "Black Widow" , "Falcon" , "Hulk" , "Hulk"]
Avengers.extend (Football_Numbers) #This Function adds another list of data
Avengers.append ("Ant-Man") #This function can be used to extra data to the end of the list
Avengers.insert(2, "Thor") #This function inserts another item or data from a selected inmdex and ,moves the rest of the data up
Avengers.remove("Falcon") #This Function removes a selected item or data of your choice
Avengers.clear() #This Function remomes evrything in the list
Avengers.pop() #This Function remomes the last item in the list
Avengers.sort () #This Function puts the the list in an alphabetical  order from A-Z, number would go from smallest to biggest 1-100
Avengers.reverse () #The function will reverse the way it is printed e.g. 4 , 5, 2 , 6 ,3. it will be printed as 3 , 6 , 2 , 5 , 4
Avengers2 = Avengers.copy() #This function just copies the same data
print (Avengers2)
#The function "print (Avengers.index ())" will allow you to search what you're looking for and print it an an index. if you type a name that's not in the list you'll get an error
#The function "print (Avengers.count ())" counts how many times an item is listed, so if the data in the list has the word "Hulk" 2x time it will be printed as 2

print("++++++++++++++++++++++++++++++++++++\n")
#11) TUPLES
print("11. TUPLES\n")
print("Tuples are similar to lists as they a type of data structure but the difference is they connot be change or modified, i.e. immutable")
axis = (1 , 2 , 3)  # these curved brackets means that it will stay and cannot be change unlike lists which use square bracket which can be edited
axis [1] = 4 #This will not work because tuples are immutable and if you run it, python will say ther is an error
print(axis [2])
#You can list tuples by using "[]" and then use "()"

print("++++++++++++++++++++++++++++++++++++\n")
#12) FUNCTIONS#12) FUNCTIONS
print("12. FUNCTIONS\n")

# To start functions use "def", which stands for, define
# You can name you function anything you like, e.g. def bat():
# You can used any type of Data in functions like boolean, floats integers or strings
# Parameters & Arguments are used to pass data or information in functions
# Parameters are variables that are given in ()
# Arguments are values which are sent to functions when they are callled

def say_who_you (name , age) : #To start functions use "def"
    print("You're " + name + " , and you are " + str (age))

say_who_you("Zayd" , 9) #Anything is these brackets is called Arguments

def Joker(mood):
    print (mood)
    if mood == 'Happy':
        print ("Laughs")
    else:
        print ("Cries")
Joker("Sad")

print("\n")

print("RETURN STATEMENTS\n")
#The "return" sends the information back to python from the function
def cube (num):
    return num * num * num
result = cube (2)
print(result)

def multiply(num1, num2):
    return num1 * num2
answer = multiply(5,5)
print(answer)

print("++++++++++++++++++++++++++++++++++++\n")
#14) IF STATEMENTS
print("14. IF STATEMENTS\n")

is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")

elif is_tall and not is_male:
    print("You are tall but not male")
elif not is_tall and is_male:
    print("You are a male but not tall")
else:
    print("You are niether male nor tall")

print("++++++++++++++++++++++++++++++++++++\n")
#15) IF STATEMENTS AND COMPARISONS
print("15. IF STATEMENTS AND COMPARISONS\n")
def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(23, 222, 56))

print("++++++++++++++++++++++++++++++++++++\n")
#16) BUILDING A BETTER CALCULATOR
print("16. BUILDING A BETTER CALCULATOR\n")

num1 = float (input("Enter your first number: "))
op = input("Enter Operator")
num2 =float (input("Enter your second number: "))

if op == "+":
   print (num1 + num2)
elif op == "-":
    print (num1 - num2)
elif  op == "*":
    print (num1 * num2)
elif  op == "/":
    print (num1 / num2)
else:
    print ("Invalid Operator")

print("++++++++++++++++++++++++++++++++++++\n")
#17) DICTIONARIES
print("17. DICTIONARIES\n")
#In Python, these dictionaries can be used to give a key a value, similar to a real dictionary
daynames = {
    "Mon" : "Monday",
    "Tue" : "Tuesday",
    "Wed" : "Wednesday",
    "Thurs" : "Thursday",
    "Fri" : "Friday",
    "Sat" : "Saturday",
    "Sun" : "Sunday",
}
print(daynames["Sat"])
print(daynames.get("kla", "Not a Valid day name")) #This is another way to find and print a keyword
#But if there's not key like the example above, then you can give it a value

print("++++++++++++++++++++++++++++++++++++\n")
#20) WHILE/FOR LOOP
print("20. WHILE/FOR LOOP\n")

for letters in "Barnet Hill Academy":
    print(letters)

print("\n")

sibs = ["AR", "Yusuf", "Sufyan", "Zayd", "Eamonn"]
for brothers in sibs: #The variable brothers can be be changed to anything but dont forget to print that variable
    print(brothers + " is my brother")

print("\n")

for index in  range (10): #this will print out the numbers up to but not including 10 (i.e. from 0-9)
    print(index)

print("\n")

for index in range(5, 15): #this will print out numbers from 5-14 but not 15
    print(index)

print("\n")

for lil3bros in range(len(sibs)):
    print(sibs[lil3bros])

print("\n")

for index in range (5):
    if index == 0:
        print("1st Lineer are always winners")
    else:
        print("Losers")

print("\n")


insectsanimals = ["Spider", "Ant", "Bat"]
pronouns = ["Man", "Woman", "boy", "girl"]

for inam in insectsanimals:
    for noun in pronouns:
        print(inam, noun) # This will print out every combonation in the lists

num = [1, 2, 3, 4,5]
for no_3 in num:
    if no_3 == 3:
        print("got it!")
        continue
    print (no_3)

print("\n")

#18) WHILE LOOPS
print("18. WHILE LOOPS\n")

i = 1
while i <= 10:
    print(i)
    i += 1 # This shortcut "+=" means i = i +1
print("Done With Loop")

print("\n")

i = 0
while i < 11:
     if i == 6:
         break
     print(i)
     i += 1

print("++++++++++++++++++++++++++++++++++++\n")
#19) BUILDING A GUESSING GAME
print("19. BUILDING A GUESSING GAME\n")

secret_word = "ALIS"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = True

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input ("Guess the Word")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You Lose!")
else:
    print("You Win")

print("++++++++++++++++++++++++++++++++++++\n")
#21) EXPONENT FUNCTION
print("21. EXPONENT FUNCTION\n")

#Exponen dunction allows you to take number and raise it to to a specific power - like indices

print(2**3) #This is 2^3 (2 x 2 x 2= 8). "^" means power of

def powerup (basenum, powernum):
    result = 1
    for index in range (powernum):
        result = result * basenum
    return result

print(powerup(4, 3))

print("++++++++++++++++++++++++++++++++++++\n")
#22) 2D LISTS AND NESTED LOOPS
print("22. 2D LISTS AND NESTED LOOPS\n")

print("2D Lists\n")

numbergrid = [
    [1, 2, 3],
    [4, 5, 6,],
    [7, 8, 9,],
    [0],
]

print(numbergrid[2][1])
# The first "[]" is the rows and the second "[]" is columns

print("Nested for Loop\n")

for row in numbergrid:
    print(row)

for row in numbergrid:
    for col in row:
        print(col)

print("++++++++++++++++++++++++++++++++++++\n")
#23) BUILDING A TRANSLATOR
print("23. BUILDING A TRANSLATOR\n")
