
list_of_lists = [[1, 5], [3, 2], [4, 8], [2, 1]]

list_of_lists.sort(key=lambda x: x[1])

print("Sorted list by second element of sublists:")
print(list_of_lists)


def bubbleSort(list1):
  
    for Pass in range(1,len(list1)):

        for i in range(len(list1)-Pass):
            if(list1[i][2]>list1[i+1][2]):
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1      

list2 = [52,14,23,66,80,90]
ans = bubbleSort(list2)
print(ans)