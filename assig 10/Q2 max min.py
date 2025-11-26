numbers = [12, 45, 7, 89, 34, 22, 1, 99, 56]

maximum = numbers[0]
minimum = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]
    if numbers[i] < minimum:
        minimum = numbers[i]

print("Maximum element is:", maximum)
print("Minimum element is:", minimum)



