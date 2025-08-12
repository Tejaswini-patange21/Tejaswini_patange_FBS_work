def anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = input("Enter first string: ").replace(" ", "").lower()
string2 = input("Enter second string: ").replace(" ", "").lower()

if anagrams(string1, string2):
    print("Both strings are anagrams. Deleting both")
    string1 = ""
    string2 = ""
else:
    print("Strings are not anagrams.")

print("String 1 after check:", string1)
print("String 2 after check:", string2)
