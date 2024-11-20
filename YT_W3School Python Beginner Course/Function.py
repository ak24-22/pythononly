#12) FUNCTIONS
print("12. FUNCTIONS\n")

# To start functions use "def", which stands for, define
# You can name you function anything you like, e.g. def bat():
# You can use any type of Data in functions like boolean, floats integers,strings, lists, sets, dictionaries, etc..
# Parameters & Arguments are used to pass data or information in functions
# Parameters are variables that are given in () and can only work inside the function
# Arguments are values which are sent to functions when they are called
# The number of parameters has to equal the number of arguments


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
