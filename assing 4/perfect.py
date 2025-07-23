num = int(input("Enter a number:"))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i


if(sum == num):
    print("perfect number is", num)
else:
    print("it is not perfect number", num)

    



