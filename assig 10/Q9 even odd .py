n = int(input("Enter number of elements in the list: "))

main_list = []
even_list = []
odd_list = []

i = 0
while i < n:
    num = int(input("Enter element {}: ".format(i + 1)))
    main_list.append(num)
    i = i + 1

i = 0
while i < n:
    if main_list[i] % 2 == 0:
        even_list.append(main_list[i])
    else:
        odd_list.append(main_list[i])
    i = i + 1

print("Original List:", main_list)
print("Even List:", even_list)
print("Odd List:", odd_list)
