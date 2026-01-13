# Inverted Right-Angled Triangle Star Pattern

n = int(input("Enter the number of rows: "))

col = 5
for i in range(n):
    for j in range(col):
        print("*", end=" ")
    col -= 1
    print()