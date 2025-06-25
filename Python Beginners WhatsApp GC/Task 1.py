# Day 1: Introduction to Python

# -	Example: Print a welcome message

print("Welcome to programming in Python!\nHappy Programming!")

# -	Exercise: Check your Python version

print("\n")
print("In Command Prompt type:\n  python --version\nIn Code Editors - 2 Options\nOption 1:")

import sys
print(f"Python Version (Long Version): {sys.version}")

print("Option 2:")

print(f"Python Version (Short Version): {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

print("\n")
# -	Challenge: Write a script that prints your name and favourite hobby

name = "Abdul - Kareem Ali"
hobbies = "\n-Socialising with freinds and family \n-Gaming\n-Watching:\n  -Movies\n  -TV Shows\n  -Animes\n  -Donghuas\n  -Cartoons"


print(f"Hey, my name is, {name} and my hobbies are: {hobbies}")

