# Day 8: Loops (for, while)

# -	Example: Loop through numbers and lists

check_list = ["1. Fuel", "2. Engine", "3. System", "4. Weather"] 

for checks in check_list:
    print(f"{checks} ✅")

# -	Exercise: Print the first 10 multiples of a number

i = 1
for i in range(1,11):
    print(i * 10)

# -	Challenge: Build a countdown timer

t = 10
for t in range(1,11):
    t += 1
print("Lift Off")

num = int(input("Enter TimesTable: "))

for b in range(1,16):
    print(f"{b} x {num} = {b*num}")


