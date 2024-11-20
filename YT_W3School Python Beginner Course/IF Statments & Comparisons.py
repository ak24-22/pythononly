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