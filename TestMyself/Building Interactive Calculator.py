print("Building a Calculator\n")
name = input("Enter Your Name: ")
print("Hi, " + name + "!")

ready = input("Are You Ready?") 

if ready == "y":
    print("Good, let's go!")
elif ready == "yes":
    print("Good, let's go!")
elif ready == "yeah":
    print("Good, let's go!")
elif ready == "Y":
    print("Good, let's go!")
elif ready == "Yes":
    print("Good, let's go!")
elif ready == "Yeah":
    print("Good, let's go!")
else:
    print("Maybe next time, then.. ")

print("\n")

num1 = float (input("Enter A Number: "))
op = input("Enter Operator: ")
num2 = float (input("Enter A Second Number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")

