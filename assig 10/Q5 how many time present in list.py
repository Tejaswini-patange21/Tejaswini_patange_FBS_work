
my_list =[4, 2, 7, 4, 9, 4, 1, 3]

num = int(input("Enter a number to search in the list: "))

found = False
count = 0

for i in range(len(my_list)):
    if my_list[i] == num:
        found = True
        count = count + 1

if found:
    print(num, "is present in the list.")
    print("It appears", count, "time(s).")
else:
    print(num, "is not present in the list.")
