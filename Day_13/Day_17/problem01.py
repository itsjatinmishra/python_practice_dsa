sentence = input("Enter a sentence please: ")

words = sentence.split()
count = 0

for item in words:
    if len(item) > 0:
        if (ord(item[0]) == 97 or ord(item[0]) == 101 or ord(item[0]) == 105 or ord(item[0]) == 111 or ord(item[0]) == 117 or
            ord(item[0]) == 65 or ord(item[0]) == 69 or ord(item[0]) == 73 or ord(item[0]) == 79 or ord(item[0]) == 85):
            count += 1

print("The number of vowels word is: ", count)