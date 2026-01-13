arr = [1, 2, 3, 4]

count = 0
i = 0
while i < len(arr) - 2:
    print(i, len(arr) - 2)
    if arr[i] < arr[i+1] < arr[i+2]:
            count += 1
    i += 1
print(count)