num = int(input("Enter a number:"))

original_num = num

num_digits =len(str(num))

sum_of_powers = 0

while (num > 0):
    digits = num % 10
    sum_of_powers += digits **num_digits
    num = num//10

if (original_num == sum_of_powers):
    print("Armstrong no.is:",original_num)
else:
    print("is not armstrong no.is:",original_num)        
