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