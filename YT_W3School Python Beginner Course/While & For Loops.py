#20) WHILE/FOR LOOP
print("20. WHILE/FOR LOOP\n")

print("FOR LOOP\n")

for letters in "Barnet Hill Academy":
    print(letters)

print("\n")

sibs = ["AR", "Yusuf", "Sufyan", "Zayd", "Eamonn"]
for brothers in sibs: #The variable brothers can be changed to anything but dont forget to print that variable
    print(brothers + " is my brother")

print("\n")

for index in  range (10): #this will print out the numbers up to but not including 10 (i.e. from 0-9)
    print(index)

print("\n")

for index in range(5, 15): #this will print out numbers from 5-14 but not 15
    print(index)

print("\n")

# If you want the 2nd loop to work you have to include the sibs lists
# Otherwise you will get an eror message
sibs = ["AR", "Yusuf", "Sufyan", "Zayd", "Eamonn"]
for lil3bros in sibs[-3:]:
    print(lil3bros)

print("\n")

for index in range (5):
    if index == 0:
        print("1st Lineer are always winners")
    else:
        print("Losers")

print("\n")


insectsanimals = ["Spider", "Ant", "Bat"]
pronouns = ["Man", "Woman", "boy", "girl"]

for inam in insectsanimals:
    for noun in pronouns:
        print(inam, noun) # This will print out every combination in the lists

num = [1, 2, 3, 4,5]
for no_3 in num:
    if no_3 == 3:
        print("got it!")
        continue
    print (no_3)

print("\n")

print("WHILE LOOPS\n")

i = 1
while i <= 10:
    print(i)
    i += 1 # This shortcut "+=" means i = i +1
print("Done With Loop")

print("\n")

i = 0
while i < 11:
     if i == 6:
         break
     print(i)
     i += 1

a = 3
while a > 0:
    print(a)
    a -= 1
print("GO!")










