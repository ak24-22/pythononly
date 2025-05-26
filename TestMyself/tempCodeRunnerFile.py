# For Loop
num = int(input("Enter Number of Times Table: "))
limit = int(input("Enter Number You Want To Go To: "))

print("\n")

for i in range(1, limit + 1):
    print(f"{num} x {limit} = {i*num}")
    
print("\n")

# While Loop
# o = 0    
# while o < 12:
#     o += 1
#     print(f"{num} x {o} = {o*num}")