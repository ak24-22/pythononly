#17) DICTIONARIES
print("17. DICTIONARIES\n")
#In Python, these dictionaries can be used to give a key a value, similar to a real dictionary
daynames = {
    "Mon" : "Monday",
    "Tue" : "Tuesday",
    "Wed" : "Wednesday",
    "Thurs" : "Thursday",
    "Fri" : "Friday",
    "Sat" : "Saturday",
    "Sun" : "Sunday",
}
print(daynames["Sat"])
print(daynames.get("kla", "Not a Valid day name")) #This is another way to find and print a keyword
#But if there's not key like the example above, then you can give it a value