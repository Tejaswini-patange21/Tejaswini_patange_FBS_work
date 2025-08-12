def reverseNum(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

num = int(input("Enter a number: "))
result = reverseNum(num)
print("Reverse of", num, "is:", result)
