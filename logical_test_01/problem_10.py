numbers = [4, 3, 2, 10, 38, 1]

shift_count = 0

for i in range(1, len(numbers)):
    j = 0
    while j < i:
        if numbers[j] < numbers[i]:
            numbers[j], numbers[i] = numbers[i], numbers[j]
            shift_count += 1
        j += 1
print("Sorted list:", numbers)
print("Total shifts:", shift_count)