#Global variable
a = 10
z = 100
print(id(a)) # it will give memory location of a = 10

def update():
    global a
    print(id(a)) # it will give memory location of a = 10

    a = 15
    print(id(a)) # it will give memory location of local_variable a = 15

    globals()['a'] = 30
    globals()['z'] = 1500

    print(a)

update()

print('Global a: ', a)
print('Global z: ', z)