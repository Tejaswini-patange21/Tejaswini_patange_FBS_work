text = input("Enter a string: ")

words = text.split()

freq = {}

for word in words:
    word = word.lower()  # for case-insensitive counting
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for word, count in freq.items():
    print(f"{word}: {count}")