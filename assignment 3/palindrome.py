num = int(input("Enter a 3-digit number: "))

a= num % 10
num = num // 10
b = num % 10
rev = (a*10)+b
c = num // 10
rev = (rev*10)+c
print("reverse 3-digit no.is",rev)

if(copy==rev):
       
      if(num == rev):
        print("The number is a palindrome")
      else:
        print("The number is not a palindrome")
else:
     print("enter a valid 3-digit number")



