input_list = [1,2,3,4]
output_list = []


new_element = 1
for i in range(0, 4):
    initial_value = i
    for j in range(0,4):
        if(initial_value == i):
            continue
        else:
            new_element *= input_list[j]

output_list.append(new_element)

print(output_list)