# take input
sentence = input("Enter the sentence please: ").lower()

lst = sentence.split()

temp_str = ""
for i in lst:
    temp_str += i.capitalize() + " "

print(temp_str)