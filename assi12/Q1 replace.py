str1 = input("Enter the string")
new_string = ""

for s in str1:
    if s =="a":
        new_string += '$'
    else:
        new_string += s

print("modified string:",new_string)            


