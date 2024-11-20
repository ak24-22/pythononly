#22) 2D LISTS AND NESTED LOOPS
print("22. 2D LISTS AND NESTED LOOPS\n")

print("2D Lists\n")

numbergrid = [
    [1, 2, 3],
    [4, 5, 6,],
    [7, 8, 9,],
    [0],
]

print(numbergrid[2][1])
# The first "[]" is the rows and the second "[]" is columns

print("Nested for Loop\n")

for row in numbergrid:
    print(row)

for row in numbergrid:
    for col in row:
        print(col)
