#2.	Write a program to count even and odd numbers from 10 user inputs using a while loop.
even_count = 0
odd_count = 0

for i in range(10):
    n = int(input(f"Enter value {i + 1}: "))
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("The even count is:", even_count)
print("The odd count is:", odd_count)