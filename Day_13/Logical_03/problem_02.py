list01 = [1,2,3,4]

output01 = []

i = 0

output01.append(list01[i])
while i < len(list01):
    sum = 0
    if (i < len(list01) - 1):
        sum += output01[i] + list01[i + 1]
        output01.append(sum)
    i += 1

print(output01)