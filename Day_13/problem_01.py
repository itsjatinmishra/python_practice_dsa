#  Write a Python function that sorts a list of strings based on 
# the length of the strings 

# 1st method of sorting

list_01 = ["Hello", "Hi", "Hey", "Heelloo"]

def sorted_by_len_by_fun(data):
    return sorted(data, key=len)

print(sorted_by_len_by_fun(list_01))




# 2nd method of sorting

list_01 = ["hi", "cat", "apple", "go", "hello"]

# find max length
max_len = 0
for item in list_01:
    if len(item) > max_len:
        max_len = len(item)


# create list_02 (each index will contain a list) because there might be possibility that
# the two strings are of same size
list_02 = []
for i in range(max_len + 1):
    list_02.append([])

# place items based on their length
def sort_by_len(data):
    for item in data:
        index = len(item)
        list_02[index].append(item)
    return list_02


sorted_list = sort_by_len(list_01)

# flatten the list (remove empty buckets)
final_list = []
for bucket in sorted_list:
    for word in bucket:
        final_list.append(word)

print("Sorted by length:", final_list)