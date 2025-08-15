# Python program to find the two numbers whose product is maximum

numbers = [3, 5, -10, -20, 15, 8]

num_set = set(numbers)

max_product = None
num1 = num2 = None

num_list = list(num_set)

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        product = num_list[i] * num_list[j]
        if max_product is None or product > max_product:
            max_product = product
            num1, num2 = num_list[i], num_list[j]

print("The two numbers are:", num1, "and", num2)
print("Maximum product is:", max_product)
