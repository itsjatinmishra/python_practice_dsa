#empty tuple

a = ()

print(type(a))

# if we want to create a tuple with one element then we should use this syntx:= a = (1,)

b = (1,)
print(type(b))

# tuble are immutable, In simple word, we can't change its elements

demoTuple = ("Jatin", "Avtar", 55.5, 55, True)

print(demoTuple)

# demoTuple[1] = "Change Avtar"    Here it throw an error because we can't change it


''' Following are some methods'''

demoTup = (1,25,55,66,81,9,96,8,8)

print(demoTup.index(55))
print(demoTup.count(8))
print(55 in demoTup)

repeatedTup = demoTup * 3

print(repeatedTup)

newTup = (1,2,3)
a,b,c = newTup
print(a)
print(b)
print(c)