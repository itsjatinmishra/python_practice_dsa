# Write a program to reverse a number using a while loop.
n = int(input("Enter the number which you want to reverse: "))

print("The number you have entered: ", n)

rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n = n // 10

print("The reversed number is: ", rev)