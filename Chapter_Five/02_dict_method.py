d = {} # this is empty dictonary
marks = {
    "name": "Jatin Mishra",
    "age": 23,
    "role": "CEO",
    "work": "Own business",
    59: "Luck"
}

print(marks.items()) # it will give us the (key value pair in the form of tuples)
print(marks.keys()) # it will give us the (only the key)
print(marks.values()) # it will give us the (only the values)
marks.update({"age": 24, "Renuka": 100}) #it will update the value and also add the key value pair if we want
# of dictonary because dictonary is mutable, we can change it

# print(marks.items())

print(marks.get("name")) #it prints none        #this will simply return the specified key value
print(marks["name"]) #its shows us an error
