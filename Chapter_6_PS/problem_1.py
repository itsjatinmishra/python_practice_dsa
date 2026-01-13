a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))

if(a>b and a>c and a>d):
    print("A's value is greatest: ", a)
elif(b>a and b>c and b>d):
    print("B's value is greatest: ", b)
elif(c>b and c>a and c>d):
    print("C's value is greatest: ", c)
else:
    print("D's value is greatest: ", d)
