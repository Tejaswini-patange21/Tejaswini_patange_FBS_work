# Recursive function to find factorial
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

# Recursive function to find sum of series: 1! + 2! + ... + n!
def seriesSum(n):
    if n == 1:
        return fact(1)
    else:
        return fact(n) + seriesSum(n - 1)

# Main Program
n = int(input("Enter the value of n: "))
result = seriesSum(n)
print("Sum of the series 1! + 2! + ... +", n, "! is:", result)
