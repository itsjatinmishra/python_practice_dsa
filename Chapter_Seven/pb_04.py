n = int(input("Enter the number up to which you want to find the sum of natural numbers: "))

# total = sum(range(1, n + 1))
# print("The sum of first", n, "natural numbers is:", total)

total = n * (n + 1) // 2
print("The sum of first", n, "natural number is: ", total)
