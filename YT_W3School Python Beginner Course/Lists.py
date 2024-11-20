#9) LISTS
print("9. LISTS\n")

Superheros = ["Spider Man" , "Iron Man" , "Captain America" , "Hawkeye" , "Black Widow" , "Falcon" , "Hulk"]
#Square brackets are used to hold a list of data in python. it can also hold  other types  of data like strings and/or boolean and/or numbers
# index starts at 0 in python, however if you want select the data from the back of the list it starts at !-1

print(Superheros[0])   #this will print the first index which is Spiderman
print(Superheros[-1])  #this will print the last index which is Hulk  pring this as -1 tells python that i want to satart from the back
print(Superheros[1:])  #this will print out the list staring from iron man
print(Superheros[2:5]) #This will print out everything from captian america to but not including falcon
Superheros[0] = "Thor" #Modifying and changing a selected data in the list, so i changed the first index, which starts from 0 so it's spiderman to thor
print(Superheros[0])
