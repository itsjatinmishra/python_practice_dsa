# First method to count no of bits
def convertToBinary(n):
    binary = ""
    while (n > 0):
        rem = n % 2
        binary = str(rem) + binary
        n = n // 2
    return binary

n = 15
res = convertToBinary(n)
# print(res)

lst_res = list(res)
# print(lst_res)

count = 0
for i in range(len(lst_res)):
    if(lst_res[i] == '1'):
        count = count + 1

print("The count of one's in a bits is: ", count)




#Second method by using Bitwise opearator
n = 15
num = n
def bitwiseMehod(num):
    count = 0
    while num > 0:
        if num & 1:
            count = count + 1
    num = num >> 1  # it will discart last bit so we will check next bit

    return count

ans = bitwiseMehod(num)
print("The number of count is: ", ans)
