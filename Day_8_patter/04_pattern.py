# Number Pyramid Pattern

n = int(input("Enter the number of rows: "))

space = n - 1
col = 1

for i in range(1, n + 1):
    for s in range(space):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for k in range(i - 1, 0, -1):
        print(k, end="")

    print()
    space -= 1