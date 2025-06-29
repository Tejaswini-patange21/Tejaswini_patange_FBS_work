num=int(input("Enter the three digit no:"))

a = num%10
num =num//10
c= num%10
d = num//10

sum = a+d+c

print("sum of three digit no is:",sum)