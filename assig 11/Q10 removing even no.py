
numbers = [10, 15, 22, 33, 40, 55, 60, 71]

odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print("Original List:", numbers)
print("List after removing even numbers:", odd_numbers)
