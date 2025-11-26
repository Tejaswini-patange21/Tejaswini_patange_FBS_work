text = input("Enter a string: ")

letters_count = 0
digits_count = 0

for char in text:
    if char.isalpha():       # Check if it's a letter
        letters_count += 1
    elif char.isdigit():     # Check if it's a digit
        digits_count += 1

print("Number of letters:", letters_count)
print("Number of digits:", digits_count)