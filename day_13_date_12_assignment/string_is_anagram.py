input_str_01 = input("Enter the first string: ").lower()
input_str_02 = input("Enter the second string: ").lower()

if sorted(input_str_01) == sorted(input_str_02):
    print("The string is ANAGRAM")
else:
    print("The string is NOT an ANAGRAM")