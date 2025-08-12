def fibonacci(n):
    a, b = 1, 1
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1


n = int(input("Enter the number of terms: "))
print("Fibonacci series:")
fibonacci(n)
