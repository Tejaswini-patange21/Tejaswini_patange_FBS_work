#to find reverse of a two digit number
num = int (input("enter the two digit no:"))

a = num//10
b = num%10

reverse = b * 10 + a 

print ("reverse two digit no",reverse) 
