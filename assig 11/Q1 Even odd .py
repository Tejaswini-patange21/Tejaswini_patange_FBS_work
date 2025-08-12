numbers = [10, 23, 45, 66, 78, 91, 34, 55, 88]

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Original List:", numbers)
print("Even Numbers List:", even_list)
print("Odd Numbers List:", odd_list)
