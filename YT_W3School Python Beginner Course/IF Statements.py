#13) RETURN STATEMENTS (IN FUNCTIONS)
print("13. RETURN STATEMENTS\n")

is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")

elif is_tall and not is_male:
    print("You are tall but not male")
elif not is_tall and is_male:
    print("You are a male but not tall")
else:
    print("You are niether male nor tall")