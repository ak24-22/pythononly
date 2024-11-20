#24) TRY/EXCEPT
print("24.TRY/EXCEPT\n")

# number = int(input("Enter a number: "))
# print(number)

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: # Storing "ZeroDivisionError" as a variable
    print("err")
except ValueError:
    print("Invalid Text")