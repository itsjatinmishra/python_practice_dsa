#find the first non-repeating character

# To find the first non-repeating character,
# you can use a two-pass approach: first, 
# count the frequency of each character in the string.
# Second, iterate through the string again and return the first character with a frequency count of one.


text = input("Enter a String please: ")

new_dict = {}
count = 0
for i in text:
    new_dict.update({i: count})


for i in text:
    if i in new_dict:
        new_dict[i] += 1
    else:
        new_dict[i] = 1

print(new_dict)

for key, value in new_dict.items():
    if new_dict[key] == 1:
        print(key)
        break