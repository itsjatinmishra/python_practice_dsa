def generate_one_letter_words(word):
    result = []

    for i in range(len(word)):
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch != word[i]:
                new_word = word[:i] + ch + word[i+1:]
                print(new_word)
                result.append(new_word)
        
        return result
    

word = "hot"
print(generate_one_letter_words(word))

# word = "hot"
# i = 1
# first = word[:i]
# ch = 'a'
# end = word[i+1:]

# print(first, ch, end)


