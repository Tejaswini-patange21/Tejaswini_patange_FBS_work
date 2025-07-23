start = int(input("Enter the start: "))
stop = int(input("Enter the stop: "))



for num in range(start, stop + 1):
    if num % 7 == 0 and num % 5 == 0:
        print(num)

print("Numbers between start and end divisible by 7 and multiple of 5:")        


