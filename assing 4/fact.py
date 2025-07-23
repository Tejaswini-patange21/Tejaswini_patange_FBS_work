n = int(input("Enter a number: "))
fact = 1


for i in range(1, n + 1):
        fact*= i

if (n < 0):
    print("Factorial is negative numbers:")
elif(n == 0):
    print("The factorial is:")
else:
     print("The factorial of", n, "is:", fact)

     