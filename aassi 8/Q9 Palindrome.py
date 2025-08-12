def palindrome(n):
    original = n
    reverse = 0
    while(n > 0):
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return original == reverse


num = int(input("Enter a number: "))
if palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
