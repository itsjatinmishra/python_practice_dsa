input_list01 = [1,5,3,7,9]

def maximum_product(input_list01):
    n = len(input_list01)

    max_product = -1
    for i in range(n):
        for j in range(n):
            if i != j:
                product = input_list01[i] * input_list01[j]
                max_product = max(max_product, product)
    
    return max_product


print(maximum_product(input_list01))