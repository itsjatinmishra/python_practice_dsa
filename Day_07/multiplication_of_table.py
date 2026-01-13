# Program to print multiplication table of a given number

n = int(input("Enter the number for multiplication table: "))

print(f"\nMultiplication Table of {n}:\n")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")