#23) BUILDING A TRANSLATOR
print("23. BUILDING A TRANSLATOR\n")

def translate (Word):
    translation = ""
    for letters in Word:
        if letters.lower() not in "aioue":
            translation = translation + letters

        else:
            if letters.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
    return translation

print(translate(input("Enter a Word: ")))

