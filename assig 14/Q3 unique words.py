# Program to find unique words and their frequency using set
strings_list = ["apple orange banana","banana apple mango","mango orange banana apple"]

all_words = set()
for sentence in strings_list:
    words = sentence.split()
    all_words.update(words)

word_frequency = {}
for word in all_words:
    count = 0
    for sentence in strings_list:
        count += sentence.split().count(word)
    word_frequency[word] = count

print("Unique words:", all_words)
print("Word frequencies:")
for word, freq in word_frequency.items():
    print(f"{word}: {freq}")

