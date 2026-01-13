#count number of digit without using string len() function or other function
n = int(input("Enter the number please: "))

count = 0
while n > 0:
    count += 1
    n = n // 10

print(count)