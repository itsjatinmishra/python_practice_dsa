text = input("Enter a string: ")


new_dict = {}
for i in text:
    if i in new_dict:
        new_dict[i] += 1
    else:
        new_dict[i] = 1

# print(new_dict)


new_str = ""
for key, value in new_dict.items():
    if value == 1:
        new_str += key
    else:
        new_str += key + str(value)   # convert number to string

print(new_str)