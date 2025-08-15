words = ["listen", "silent", "enlist", "rat", "tar", "art", "evil", "vile", "veil", "live"]

anagram_groups = {}

for word in words:
    sorted_word = ''.join(sorted(word))
    
    if sorted_word in anagram_groups:
        anagram_groups[sorted_word].append(word)
    else:
        anagram_groups[sorted_word] = [word]

print("Grouped Anagrams:")
for group in anagram_groups.values():
    print(group)

