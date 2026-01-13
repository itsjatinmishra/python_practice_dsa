input_list = ['a', 'b', 'c']
output_list = []

for i in range(0, 3):
    for j in range(i + 1, 3):
        # print(i, j)
        output_list.append((input_list[i], input_list[j]))

print(output_list)