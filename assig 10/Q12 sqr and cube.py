
n = 5  
number_list = []
square_list = []
cube_list = []

for i in range(1, n + 1):
    number_list.append(i)             # Adding the number
    square_list.append(i * i)         # Square 
    cube_list.append(i * i * i)       # Cube 

print("Number List:", number_list)
print("Square List:", square_list)
print("Cube List:", cube_list)
