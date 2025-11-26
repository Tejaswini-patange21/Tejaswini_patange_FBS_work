n = int(input("Enter the value of n: "))


for i in range(1, n + 1):
    if i % 2 != 0 and i % 3 != 0:
        print(i)

print("Integers from 1 to n not divisible by 2 and 3:")        
