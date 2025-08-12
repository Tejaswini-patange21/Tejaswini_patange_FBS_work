dict1 = {"name": "shruti", "age": 21}

dict2 = {"city": "pune", "country": "india"}

merged_dict = {}

for key in dict1:
    merged_dict[key] = dict1[key]

for key in dict2:
    merged_dict[key] = dict2[key]

print("Merged dictionary:", merged_dict)