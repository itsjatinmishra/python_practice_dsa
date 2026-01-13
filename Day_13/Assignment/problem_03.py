list_01 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

def rotation_90_deg(list_01):
    output = []
    row_len = len(list_01)
    col_len = len(list_01[0])
    for i in range(row_len):
        new_row = []
        for j in range(col_len - 1, -1, -1):
            new_row.append(list_01[j][i])
        output.append(new_row)
    return output

print(rotation_90_deg(list_01))

