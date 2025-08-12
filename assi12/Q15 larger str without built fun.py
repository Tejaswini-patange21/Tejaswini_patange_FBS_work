str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

len1 = string_length(str1)
len2 = string_length(str2)

if len1 > len2:
    print("Larger string is:", str1)
elif len2 > len1:
    print("Larger string is:", str2)
else:
    print("Both strings are equal in length")
    
   