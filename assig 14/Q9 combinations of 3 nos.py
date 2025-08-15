numbers = [1, 2, -1, 0, 2, -2, 3, 4]
target = 3

num_list = list(set(numbers))
combinations = set()

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        for k in range(j + 1, len(num_list)):
            if num_list[i] + num_list[j] + num_list[k] == target:
                
                combinations.add(tuple(sorted((num_list[i], num_list[j], num_list[k]))))

print(f"Unique combinations of 3 numbers adding up to {target}:")
for combo in combinations:
    print(combo)
