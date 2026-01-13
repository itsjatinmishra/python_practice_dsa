input_list = [
    [1, 2, 3],
    [3, 1, 2],
    [2, 3, 1]
]

initial_value = 0
row_size = len(input_list)
col_size = len(input_list[0])

for i in range(row_size):
    for j in range(col_size):
        initial_value ^= input_list[i][j]

# print(initial_value)
if(initial_value == 0):
    print("Congratulation ! The matrix is latin square !")
else:
    print("The matrix is not a latin square !")