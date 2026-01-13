import ast
data = ast.literal_eval(input())

list_data = data[0]
k = data[1]
n = len(list_data)

dict_demo = {}

# Count frequencies
for i in range(n):
    element = list_data[i]
    if element in dict_demo:
        dict_demo[element] += 1
    else:
        dict_demo[element] = 1

# Find elements that appear more than n/k times
result = []
for key, value in dict_demo.items():
    if value > (n / k):
        result.append(key)

# Return [0] if no elements found, otherwise return the list
if len(result) == 0:
    print([0])  # Return [0] not 0
else:
    print(result)