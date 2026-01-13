matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

m = len(matrix)
n = len(matrix[0])
s_row = 0
s_col = 0
e_row = m - 1
e_col = n - 1
count = 0

total_size = m * n

output = []
while(count < total_size):
    for i in range(s_col, e_col + 1):
        if(count < total_size):
            output.append(matrix[s_row][i])
            count += 1
    s_row += 1

    for i in range(s_row, e_row + 1):
        if(count < total_size):
            output.append(matrix[i][e_col])
            count += 1
    e_col -= 1

    j = e_col
    while(j >= s_col):
        if(count < total_size):
            output.append(matrix[e_row][j])
            count += 1
        j -= 1
    e_row -= 1

    k = e_row
    while(k >= s_row):
        if(count < total_size):
            output.append(matrix[k][s_col])
            count += 1
        k -= 1
    s_col += 1


print(output)