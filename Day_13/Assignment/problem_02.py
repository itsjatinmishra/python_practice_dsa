list_01 = [1,2,3,4]

def product_element(list_01):
    product = 1

    for i in range(len(list_01)):
        product *= list_01[i]

    for i in range(len(list_01)):
        list_01[i] = (product // list_01[i])
    
    return list_01

print(product_element(list_01))