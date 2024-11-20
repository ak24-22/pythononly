#WRITING TO FILES
print("WRITING TO FILES\n")

superhero_id = open("superhero id.txt", "a") # Changing the mode to "w" will override and delete everything
#  so whatever you want writtin  will only be there in the file as everything is gone

superhero_id.write("\nfalcon - sam wilson")
# To make a new line in the in the file use "\n" at the beginning
# Be careful if you run it twice it will add the item on the same line with no gaps in bwtween


superhero_id.close()

# You can create a new file and name it with a different extention using "w". e.g...

sups = open("superhero_id10.html", "w")
sups.write("<p> Amazing paragraph</p>")
