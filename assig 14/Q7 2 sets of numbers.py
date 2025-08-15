# Python program to find missing numbers in both sets using set operations
set1 = {1, 2, 3, 4, 5, 7}
set2 = {2, 3, 5, 6, 8}

missing_set2 = set1 - set2
missing_set1 = set2 - set1

print("Numbers missing in second set compared to first:", missing_set2)
print("Numbers missing in first set compared to second:", missing_set1)
