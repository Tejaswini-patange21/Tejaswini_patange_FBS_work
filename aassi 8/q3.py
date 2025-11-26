def sumOfSeries(num ):
    ans = 0
    for i in range(1,num):
        ans = ans + i
    return ans 

def fact(num):
    sum = 0
    fact = 1

    for i in range(1, sum+1):
        fact = fact * 1
    sum = sum+fact    
    return sum

def exponent(num):
    sum = 0
    for i in range(1,num+1):
        ans= num**1
        sum += ans
    return sum  

while(True):
    print("calling 1st function")
    print("calling 2nd function")
    print(" calling 3rd function")
ch = int(input("Enter choice"))
if(ch==1):
    num = int(input("Enter choice"))
if(ch==1):
        num = int(input("Enter the number"))
        print(sumOfSeries(num))

elif(ch==2):
    num=int(input("Enter the number"))
    print(fact(num))

elif(ch==3):
    num = int (input("Enter the number"))
    print(exponent(num))
else:
    print(result)
    print("Exit")    

