
text = input("Enter a string: ")

count = 0

for char in text:
    if 'a' <= char <= 'z':
        count += 1

# Display the result
print("Number of lowercase characters:", count)