arr = [46, 56, 58, 43, 52, 12, 5]

max_value = arr[0]
largest_position_index = 0

for i in range(len(arr)):
    if arr[i] > max_value:
        max_value = arr[i]
        largest_position_index = i

print(largest_position_index)