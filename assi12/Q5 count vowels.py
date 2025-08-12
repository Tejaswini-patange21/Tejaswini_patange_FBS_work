def countVowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count

input = input("Enter a string: ")
vowel = countVowels(input)
print("Number of vowels:", vowel)
