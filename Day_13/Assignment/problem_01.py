def transpose(list_01):
    output = []
    row_len = len(list_01)
    col_len = len(list_01[0])
    for i in range(row_len):
        new_row = []
        for j in range(col_len):
            new_row.append(list_01[j][i])
        output.append(new_row)
    
    return output

list_01 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(transpose(list_01)) 

