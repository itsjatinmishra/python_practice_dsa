n = int(input("Enter the value of n: "))

for i in range(1, n+1):
    ch = ord('A')
    for j in range(i):
        print(chr(ch+j), end=" ")
    print()