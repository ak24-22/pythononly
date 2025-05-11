print("Loops")

print("For Loops\n")
sibs = ["AR", "Maryam","Yusuf", "Sufyan", "Zayd", "Eamonn"]
for Sublings in sibs:
    print(Sublings + " are part of my family")
print("\n")
meat = ["Chicken","Meat", "Lamb", "Beef"]
food = ["Curry", "Burger"]
for me in meat:
    for fo in food:
        print(me, fo)
print("\n")

for letters in "Shrek School Academy":
    print(letters)
print("\n")

for nums in range(5,11):
    print(nums)
print("\n")

for foodyman in range(len(food)):
    print(food[foodyman])
print("\n")

for num in range (5):
    if num == 0:
        print("Woohoo, I'm the Champion")
    elif num == 1:
        print("Few, I'm 2nd!")
    else:
        print("Noo, I'm last!")