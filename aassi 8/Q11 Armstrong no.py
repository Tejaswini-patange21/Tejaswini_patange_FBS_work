def countDigits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

def armstrongSum(n, digits):
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10
    return total


def armstrong(n):
    digits = countDigits(n)
    return n == armstrongSum(n, digits)

num = int(input("Enter a number:"))
if armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
