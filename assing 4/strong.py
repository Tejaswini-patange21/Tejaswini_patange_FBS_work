num = int(input("Enter a number: "))
temp = num
sum_of_fact = 0


while (temp > 0):
    digit = temp % 10
    sum_of_fact += sum_of_fact(digit)
    temp //= 10

if(sum_of_fact == num):
    print("Strong Number is:",num)
else:
    print("its not Strong Number:",num)

    
