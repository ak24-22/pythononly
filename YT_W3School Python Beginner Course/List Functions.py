#10) LIST FUNCTIONS
print("10. LISTS FUNCTIONS\n")

Football_Numbers = [10 , 11 , 7 , 9 ,8 ,1]
Avengers = ["Iron Man" , "Captain America" , "Hawkeye" , "Black Widow" , "Falcon" , "Hulk" , "Hulk"]
Avengers.extend (Football_Numbers) #This Function adds another list of data
Avengers.append ("Ant-Man") #This function can be used to extra data to the end of the list
Avengers.insert(2, "Thor") #This function inserts another item or data from a selected inmdex and ,moves the rest of the data up
Avengers.remove("Falcon") #This Function removes a selected item or data of your choice
Avengers.clear() #This Function remomes evrything in the list
Avengers.pop() #This Function remomes the last item in the list
Avengers.sort () #This Function puts the the list in an alphabetical  order from A-Z, number would go from smallest to biggest 1-100
Avengers.reverse () #The function will reverse the way it is printed e.g. 4 , 5, 2 , 6 ,3. it will be printed as 3 , 6 , 2 , 5 , 4
Avengers2 = Avengers.copy() #This function just copies the same data
print (Avengers2)
#The function "print (Avengers.index ())" will allow you to search what you're looking for and print it an an index. if you type a name that's not in the list you'll get an error
#The function "print (Avengers.count ())" counts how many times an item is listed, so if the data in the list has the word "Hulk" 2x time it will be printed as 2
