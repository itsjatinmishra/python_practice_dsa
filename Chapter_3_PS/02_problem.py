name = input("Enter your name: ")

letter = ''' Hello <|Name|>
Your are Selected <|Date|>
'''

print(letter.replace("<|Name|>", name).replace("<|Date|>", "23-11-2025")) #Here we apply chaining as many as we want
