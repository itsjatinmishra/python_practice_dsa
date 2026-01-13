friends = ["jatin", 1, 2.50, 'a', 7681912638]

# print(len(friends)) #strings are immutable

friends[0] = "kamal"
friends.append("Rohan")

print(friends)

print(friends[1:3])

numbers = [7,6,8,1,9,1,2,6,3,8]
# numbers.reverse()
print(numbers)

# numbers.insert(2,5)
# numbers.remove(8)
# numbers.sort()
# rmElement = numbers.pop(1)
# print(rmElement)

print(numbers[::-1]) #This is not modifiying the list but, it reversed it simply