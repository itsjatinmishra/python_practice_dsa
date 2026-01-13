input_list = [1, 5, 3, 7, 9]

sorted_list = sorted(input_list)

candidate01 = 1

for i in sorted_list[-3:]:
    candidate01 *= i

candidate02 = 1

for i in sorted_list[:2]:
    candidate02 *= i
candidate02 *= sorted_list[-1]

result =  max(candidate01, candidate02)

print(result)

c1, c2 = 1, 1

print(c1, c2)