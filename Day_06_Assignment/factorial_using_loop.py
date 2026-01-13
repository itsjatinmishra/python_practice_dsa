# find factorial of a number using loops
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial does not exist for negative numbers.")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial of", n, "is:", fact)