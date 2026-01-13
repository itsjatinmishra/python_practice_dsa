#1.	Write a program to find the sum of all natural numbers up to n using a for loop.
n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n + 1):
    sum += i

print(sum)