def odd(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i
    return total

n = int(input("Enter the value of n: "))
result =odd(n)
print("Sum of all odd numbers from 1 to", n, "is:", result)
