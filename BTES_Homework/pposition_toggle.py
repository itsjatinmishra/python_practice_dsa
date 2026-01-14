# Given a number n and a bit position p, toggle (flip) the bit at that position in Python.


# First Method for this question

def convertBinary(n):
    binary = ""
    if n == 0:
        return "0"
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary

n = 13
p = 2  # bit position from the right

res = convertBinary(n)
print(f"Binary Representation = {res}")

# Convert string to list
lst = list(res)

# Toggle the bit
# Calculate the correct index from the left
index = len(lst) - 1 - p

if lst[index] == '0':
    lst[index] = '1'
else:
    lst[index] = '0'

# Convert back to string
toggled_binary = "".join(lst)
print(f"Toggled Binary = {toggled_binary}")

# Convert back to integer
toggled_number = int(toggled_binary, 2)
print(f"Toggled Number = {toggled_number}")




#Second method to solve this question using bitwise operator

n = 13
p = 2 #Bit position to toggle (0-indexed from right)

mask = 1 << p
toggled_number_with_m = n ^ mask

print(f"Original Number: {n} (binary {bin(n)[2:]})")
print(f"Toggled Number: {toggled_number_with_m} (binary {bin(toggled_number_with_m)[2:]})")

