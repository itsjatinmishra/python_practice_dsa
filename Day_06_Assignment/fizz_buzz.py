#•	Write a program to print numbers from 1 to n,
#  replacing multiples of 3 with "Fizz",
#  5 with "Buzz", and both with "FizzBuzz"
n = int(input("Enter the number until you want to check the multiple: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")