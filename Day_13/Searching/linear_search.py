list_01 = [5,8,37,46,56,58]

def linear_sort(target):
    for i in range(len(list_01)):
        if list_01[i] == target:
            return i

print(linear_sort(target=37))
    