data = [
    [7, 5, 3, 1],
    [8, 6, 4, 2]
]
list1 = data[0] + data[1]

# Bubble sort
for i in range(len(list1)):
    for j in range(0, len(list1) - i - 1):
        if list1[j] < list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print(list1)