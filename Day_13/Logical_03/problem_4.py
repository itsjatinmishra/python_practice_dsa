list01 = [1,2,3,5]

max_value = -1

for i in range(len(list01)):
    if list01[i] > max_value:
        max_value = list01[i]

total_sum = 0
for i in range(max_value + 1):
    total_sum += i

print(total_sum)

obtained_sum = 0
for i in range(len(list01)):
    obtained_sum += list01[i]

print(obtained_sum)

