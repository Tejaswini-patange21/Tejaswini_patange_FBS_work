numbers = [10, 20, 30, 40, 50]
reversed_list = []

index = len(numbers) - 1
while index >= 0:
    reversed_list.append(numbers[index])
    index -= 1

print("Original list:", numbers)
print("Reversed list:", reversed_list)
