input_list = [1, 2, 3, 4]
output_list = []

i = 0
while i < len(input_list):
    if i == 0:
        output_list.append(input_list[i])
    else:
        output_list.append(output_list[i - 1] * input_list[i])
    i += 1

print(output_list)