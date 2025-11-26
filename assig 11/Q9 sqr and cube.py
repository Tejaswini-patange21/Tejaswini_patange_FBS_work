
n = int(input("Enter how many numbers you want: "))

numbers = []
squares = []
cubes = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    squares.append(num * num)
    cubes.append(num * num * num)

print("Numbers List:", numbers)
print("Squares List:", squares)
print("Cubes List:", cubes)
