char_list01 = ['a', 'b', 'c']


def permutation(char_list01):
    output = []
    n = len(char_list01)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    output.append((char_list01[i], char_list01[j], char_list01[k]))
    
    return output
print(permutation(char_list01))
