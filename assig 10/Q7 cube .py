list1 = [2, 3, 4, 5]

cube_list = []

for i in range(len(list1)):
    num = list1[i]
    cube = num * num * num 
    cube_list.append(cube)

print("List1:",list1)
print("Cube List:", cube_list)
