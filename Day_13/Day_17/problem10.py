str_input = input("Enter a string please: ")

new_dict = {}

# Initialize counts
for item in str_input:
    new_dict[item] = 0

# Count each character
for item in str_input:
    new_dict[item] += 1

output = []
for key, value in new_dict.items():
    if value == 1:
        output.append(key)

print(output)