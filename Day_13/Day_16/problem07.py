list_01 = [46,56,58,43,52,12,5]

def bubble_sort(list_01):
    for i in range(len(list_01)):
        for j in range(len(list_01) - 1 - i):
            if list_01[j] > list_01[j + 1]:
                # swap(list_01, j, j + 1)
                list_01[j], list_01[j+1] = list_01[j + 1], list_01[j]

bubble_sort(list_01)
print("The final list after sorting is: ", list_01)