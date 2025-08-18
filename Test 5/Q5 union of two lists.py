
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

union_list = list1.copy()

for item in list2:
    if item not in union_list:
        union_list.append(item)

print("Union of two lists:", union_list)