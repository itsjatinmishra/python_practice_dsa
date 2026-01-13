sentence = input("Enter a sentence and I will give you in a reverse order: ")
word = sentence.split()

output = word[::-1]
new_str = ""

for i in output:
    new_str += " " + i

print(new_str[1:])