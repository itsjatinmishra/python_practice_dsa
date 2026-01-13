# Write a Python function that finds all keys in a dictionary 
# that have a specific value 

def keys_with_value(data, target):
    result = []
    for key, value in data.items():
        if value == target:
            result.append(key)
    return result

data = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 30
}

print(keys_with_value(data, 30))