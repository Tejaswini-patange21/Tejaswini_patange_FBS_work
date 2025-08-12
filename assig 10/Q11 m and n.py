numbers = [10, 15, 20, 30, 40, 45, 60, 75, 90]

m = 5
n = 10

print("Numbers divisible by", m, "and", n, "are:")
for i in range(len(numbers)):
    if numbers[i] % m == 0 and numbers[i] % n == 0:
        print(numbers[i])
