original_list = [1, 4, 5, 8, 9, 12, 15, 18]

odd_list = []

for i in range(len(original_list)):
    if original_list[i] % 2 != 0: 
        odd_list.append(original_list[i])

print("Original List:", original_list)
print("List after removing even numbers:", odd_list)
