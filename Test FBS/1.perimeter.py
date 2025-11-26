length =int(input("enter the length of the perimeter:"))
breadth = int(input("enter the breath of the perimeter:"))
radius = int(input("enter the radius of the perimeter:"))

area = length*breadth
semicircle_area= 0.5*3.14*radius*radius

total_area = area + semicircle_area
perimeter = 2 * length + 2 * radius + 3.14 * radius 

print("area:",area)
print("perimeter:",perimeter)




