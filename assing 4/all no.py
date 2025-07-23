start = int(input("Enter the start: "))
stop = int(input("Enter the stop: "))
divisor = int(input("Enter the number to divide by: "))


for num in range(start, stop + 1):
    if num % divisor == 0:
        print(num) 

print("Numbers between start and stop divisible by divisor:",divisor)        
