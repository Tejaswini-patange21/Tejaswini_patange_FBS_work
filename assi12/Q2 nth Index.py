def removeChar(string, n):
    if n < 0 or n >= len(string):
       return "Invalid index" 
    return string[:n] + string[n+1:]


input_str = input("Enter a string:")

n = int(input("Enter a indexed number:"))
result = removeChar(input_str, n)
print("Original String:", input_str)
print("After removing character at index", n, ":", result)
