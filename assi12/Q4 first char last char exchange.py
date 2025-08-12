def firstLast(s):
    if len(s) <= 1:
        return s  
    return s[-1] + s[1:-1] + s[0]

str100 = input("Enter a string: ")
new_string = firstLast(str100)

print("Original String:", str100)
print("New String after swapping first and last characters:", new_string)



