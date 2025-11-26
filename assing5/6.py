n = int(input("Enter the value n: "))
count = 0       
num = 2         

while(count < n):
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if(prime):
        print(num, end=" ")
        count += 1
    num += 1

print("The first prime numbers:",n)
