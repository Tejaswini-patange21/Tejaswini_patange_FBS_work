# Program to find all pairs of elements in a list with a given sum
numbers = [2, 4, 3, 7, 5, 8, 1, 9]
target_sum = 10

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):  # avoid duplicate pairs & self-pairing
        if numbers[i] + numbers[j] == target_sum:
            pairs.append((numbers[i], numbers[j]))

print(f"Pairs with sum {target_sum}: {pairs}")
