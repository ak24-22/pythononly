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
print(10 % 3) #The "%" are knows as moduls with the prints the remainder only

"""
Different Operators
-------------------
Arithmetic:
-----------
+ Adds
- Subracts
* Multiply
/ Divides
% Modulus = Divides the numbers BUT it only prints the remainder. e.g. 10 % 2 = 5, but python will print out 0  
** Exponentiation = Power of, i.e. indices, e.g. 2**3 is 2^3, which is (2 x 2 x 2= 8)
// Floor Division = Divides the numbers then round them down to the nearest number. e.g. 15/2 = 7.5, then round down to 7 

Comparison:
-----------
== Equal 
!= Not Equal 
> Greater Than
< Less Than
>= Greater Than or Equal
<= Less Then or Equal
e
"""