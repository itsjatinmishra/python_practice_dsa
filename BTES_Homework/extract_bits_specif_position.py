# Give any number, extract bits from position1 to position2


def convertBinary(n):
    binary = ""
    if n == 0:
        return "0"
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary

n = 29
res = convertBinary(n)[::-1]
pos1 = 1 #include
pos2 = 3 #include

new_res = res[pos1: pos2 + 1]
# print(new_res)

final_res = new_res[::-1]
# print(final_res)




# Second method to use of Bitwise Operator
n = 15
pos1 = 1
pos2 = 3

# Step 1: Calculate the total number of bits we want
k = pos2 - pos1 + 1

n = n >> (pos1 - 1)

c_and = (1<<k) - 1

final_res = (n & c_and)

print("Extracted bits (decimal):", final_res)
print("Extracted Binary form:", bin(final_res)[2:])