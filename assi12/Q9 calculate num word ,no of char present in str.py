text = input("Enter a string: ")

char_count = 0
for char in text:
    if char != " ":  
        char_count += 1

word_count = 1 if text.strip() != "" else 0  
for char in text:
    if char == " ":
        word_count += 1

print("Number of characters:", char_count)
print("Number of words:",word_count)