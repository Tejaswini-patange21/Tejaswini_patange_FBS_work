numbers = [12, 45, 23, 89, 77, 54]

n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] < numbers[j + 1]:
            
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

second_largest = numbers[1]

print("Sorted List:", numbers)
print("Second Largest Number:", second_largest)
