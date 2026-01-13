# Diamond Pattern

n = int(input("Enter the number of rows: "))

half = n // 2
space = half
col = 1

for i in range(1, n + 1):
    
    for s in range(space):
        print(" ", end="")

    for j in range(col):
        print("*", end="")

    print()

    if i <= half:
        col += 2
        space -= 1
    else:
        col -= 2
        space += 1