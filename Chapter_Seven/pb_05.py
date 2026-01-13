n = int(input("Enter the number up to which you want to find the sum of natural numbers: "))

fact = 1
if(n < 0 or n == 1):
    print(1)

for i in range(2, n + 1):
    fact *= i
print("The factorial of ", n, " is: ", fact)
