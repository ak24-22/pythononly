#READING FILES
print("READING FILES\n")

# Opening modes in python are:
# "r" = read - Only read the file, no editing or changeing
# "w" = writing - Only edit or change the file a bit
# "a"  = append - Only add new information at the end, no changing or modifying it
# "r+" = read & reite - You can read the file and edit it

concat_file = open("Concat.txt", "r") # storing the file in a variable and can only read the file
#print(concat_file.readable()) # This key word will check to see if the file is readable,
# if the file is readable it will be printed in a boolean expression depending on the mode you typed
# e.g. if the mode is "r" then it will be printed with a "True" otherwiise it will be printed as "False"

#print(concat_file.read()) # This will print out the file and show everything -
#print(concat_file.readline()) # This will print out the lines individually, i.e. printin 1 line at a time
#print(concat_file.readlines()) # This will print out the fine as a list
# if you want a specific line to be printed out then an index by using, []. e.g. "print(concat_file.readlines()[0])"
# Another way to open the file is using for loops;
for con in concat_file.readlines():
    print(con)
#print(concat_file.close()) # Closeing file

