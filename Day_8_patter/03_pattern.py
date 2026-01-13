'''
    *
   ***
  *****
 *******
*********
'''


# Pyramid Star Pattern

n = int(input("Enter the number of rows: "))

space = n - 1
col = 1
for i in range(n):
    for k in range(space):
        print(" ", end=" ")
    for j in range(col):
        print("*", end=" ")
    col += 2
    space -= 1
    print()