data = [1, 3, 3, 7, 7, 7, 9, 9, 9]
dict01 = {}


def find_mode():
    for i in data:
        if i in dict01:
            dict01[i] += 1
        else:
            dict01[i] = 1

max_count = 0
max_count_index = -1
max_count_tie = []

for key, value in dict01.items():
    if value > max_count:
        max_count = value
        max_count_index = key
        max_count_tie = [key]
    elif value == max_count:
        max_count_tie.append(key)

if len(max_count_tie) == 1:
    print(max_count_tie[0])
else:
    min_value = max_count_tie[0]
    for i in range(len(max_count_tie)):
        if(max_count_tie[i] < min_value):
            min_value = max_count_tie[i]
    
    print(min_value)


# print("Frequencies:", dict01)
# print("Max count is:", max_count)
# print("Number(s) with max count:", max_count_tie)

