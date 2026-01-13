matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

row_size = len(matrix)
col_size = len(matrix[0])

border_sum = 0

for i in range(row_size):
    for j in range(col_size):
        
        #top row or bottom row
        if i == 0 or i == row_size - 1:
            border_sum += matrix[i][j]
        elif j == 0 or j == col_size - 1:
            border_sum += matrix[i][j]

print(border_sum)