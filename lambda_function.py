from functools import reduce

#List of integers

numbers = [1,2,3,4,5,6,7,8,9,10]

#use of map() function

squared_of_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_of_numbers)

even_squared_numbers = list(filter(lambda x: x % 2 == 0, squared_of_numbers))

print(even_squared_numbers)

sum_even_squared = reduce(lambda x, y: x + y, even_squared_numbers)
print(sum_even_squared)