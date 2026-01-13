list_01 = [48,25,66,77,85,65,25]

first_occurence = -1
target = 25
i = 0

while i < len(list_01):
    if list_01[i] == target:
        first_occurence = i
        break
    i += 1

print(first_occurence)