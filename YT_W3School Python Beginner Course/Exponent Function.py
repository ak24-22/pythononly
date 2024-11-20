#21) EXPONENT FUNCTION
print("21. EXPONENT FUNCTION\n")

#Exponen dunction allows you to take number and raise it to to a specific power - like indices

print(2**3) #This is 2^3 (2 x 2 x 2= 8). "^" means power of

def powerup (basenum, powernum):
    result = 1
    for index in range (powernum):
        result = result * basenum
    return result

print(powerup(4, 3))