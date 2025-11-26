def sumOfDigits(num):

    sum = 0 
    while(num>0):
        a = num % 10
        num = num // 10
        sum = sum + a
    print(f'sum of the no {sum}')   

num = int(input('enter the no'))

sumOfDigits(num)
print(num) 