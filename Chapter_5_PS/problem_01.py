word = {
    "billi": "cat",
    "madad": "help",
    "kursi": "chair"
}

n = input("Enter the word you want the meaning in English: ")

ans = word.get(n)
print(ans)