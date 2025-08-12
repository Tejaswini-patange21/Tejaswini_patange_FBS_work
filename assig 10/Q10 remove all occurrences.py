list1 = [2, 5, 3, 2, 8, 2, 6]

element_to_remove = 2
new_list = []

for i in range(len(list1)):
    if list1[i] != element_to_remove:
        new_list.append(list1[i])

print(" List:",list1)
print("Element to Remove:", element_to_remove)
print("List after Removal:", new_list)
