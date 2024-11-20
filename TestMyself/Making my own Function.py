print("Making my own Function")

def calc():
    num1 = float(input("Enter a number: "))
    op = input("Ennter an operation: ")
    num2 = float(input("Enter another number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("invalid operation")

calc()

print(calc())
