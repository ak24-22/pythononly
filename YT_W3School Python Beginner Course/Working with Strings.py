#4) WORKING WITH STRINGS
print("4. WORKING WITH STRINGS")
"""
Escape Character >>
Use  '\" "\' can make a '"###"' or "'###'"appear (i.e. double or single quotation)
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
Paretheses are: (), [] & {}
in terms of Data types > () are used in Tuples, [] are used in Lists & {} are used in dictionaries or sets
"""

print("4. WORKING WITH STRINGS\n")
print("You said, \"i am Spider-Mam\"")
print("I said, \"You are Bat-Mam\" \n")

print("\n")

print("Concatenation is when you have a string and then you add another string to it")
print("3 Ways to use concatenation are:\n")

print("1) \"String\" + Variable:")

var1 = "Monsters"

print("   a.Shrek School Academy are for " + var1)
print("   b.We " + var1 + " will kill you")
print("   c." + var1 + " are here!")

print("\n")

print("2) \"String {}\".format(Variable)")

var2 = "Monsters"

print("   a.Shrek School Academy are for {}".format(var2))
print("   b.{} are here to save us".format(var2))
print("   c.BANK ROBBER:\"Oh no, it's these {}, RUN!\" ".format(var2))

print("\n")

print("3) f\"String {Variable}\"")

var3 = "Monsters"

print("   a."+ f"Kill these {var3}")
print("   b."+ f"We have to Kill these {var3} otherwise it we'll die")
print("   c."+ f"{var3} are evil")

print("\n")

phrase = "Shrek School Academy" #Giving a String a variable and then pringing it
print(phrase + " Are For =\n \"Monsters\"") #taking a string and adding another string to it (aka: Concatenation)
print("Other ways to use concatenation are:")
print({}.format(phrase) " Are for Monsters")}

print(phrase.lower()) #this is a function that changes the string or text to lower case.
# To make it all upper case just put phrase.upper()
print(len(phrase)) #This Function tells us how many characters are in the string (I.E. The Length
print(phrase[0]) #This function tells you what the character number. These strings start at 0 and contibue
print(phrase.index("S")) #This function finds the letter in the string and prints it as a number.
# If the letter is not in the string and it is printed it will show an error.

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