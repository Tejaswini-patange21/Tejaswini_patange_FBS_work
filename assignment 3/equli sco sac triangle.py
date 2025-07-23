a = float(input("Enter length of first side: "))
b = float(input("Enter length of second side: "))
c = float(input("Enter length of third side: "))

if(a + b > c and b + c > a and c + a > b):
    if a == b == c:
        print("The triangle is Equilateral.")
    elif(a == b or b == c or c == a):
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The given sides do not form a valid triangle.")
