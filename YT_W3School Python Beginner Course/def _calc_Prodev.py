# got:
#   function
#   inputs for users
#   if/elif/else
#   while True/break loops
#   try/except error handling


def calc(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*" or op == "x":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Cannot be divided by 0"
        return num1 / num2
    else:
        return "Invalid Operator"

while True:
    try:
        num1 = float(input("Enter A Number: "))
        num2 = float(input("Enter Another Number: "))
        break
    except ValueError:
        print("Please enter a number or decimal number!")

op = input("Enter Operator: ")

calculator = calc(num1, op, num2)

print(calculator)
