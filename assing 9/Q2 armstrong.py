def count(num):
    if(num!=0):
        return 1 + count(num//10)
    else:
        return 0
    
def armstrong(num,c):
    if(num !=0):
        digits = num % 10
        return(digits**c)+armstrong(num//10,c) 
    else:
        return 0
    
num = int(input("Enter the number")) 
c = count(num)
ans = armstrong(num,c)
if(ans==num):
    print("it is armstrong number")
else:
    print("not a armstrong number")     