
n = int(input("Enter number of elements:"))

user_list = []

for i in range(n):
    element = input(f"Enter element {i+1}:")
    user_list.append(element)

# Sort the list based on the length of each element
user_list.sort(key=len)

print("List sorted by length of elements:",user_list)
print(user_list)
