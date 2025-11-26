numbers = [10, 20, 10, 30, 40, 20, 50, 30]

unique_list = []

for i in range(len(numbers)):
    duplicate = False
    for j in range(len(unique_list)):
        if numbers[i] == unique_list[j]:
            duplicate = True
            break
    if not duplicate:
        unique_list.append(numbers[i])

print("Original list:", numbers)
print("List after removing duplicates:", unique_list)
