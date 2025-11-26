a = float(input("Enter length of first side: "))
b = float(input("Enter length of second side: "))
c = float(input("Enter length of third side: "))

if(a + b > c and a + c > b and b + c > a):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
