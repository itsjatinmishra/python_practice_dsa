def reverse_every_second_word(words):
    for i in range(1, len(words), 2):
        new_word = words[i]
        print(new_word[::-1])


sentence = input("Enter the sentence please: ")
words = sentence.split()

reverse_every_second_word(words)