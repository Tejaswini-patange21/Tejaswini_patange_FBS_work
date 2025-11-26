list1 = [10, 20, 30, 40, 50]
duplicate_list = []

for i in range(len(list1)):
    duplicate_list.append(list1[i])

print("List:", list1)
print("Duplicate List:", duplicate_list)
print("Are both lists pointing to same memory?",list1 is duplicate_list)
