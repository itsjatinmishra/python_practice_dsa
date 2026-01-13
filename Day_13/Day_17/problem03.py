max_value = -1

arr = [10,55,66,6,17]

for item in arr:
    if item > max_value:
        max_value = item

second_largest = -1
for item in arr:
    if item == max_value:
        continue
    elif item > second_largest:
        second_largest = item

print("The second largest number is: ", second_largest)