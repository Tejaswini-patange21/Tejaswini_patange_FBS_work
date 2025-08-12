my_dict = {"name": "deepu", "age": 32, "city": "London"}

key_to_remove = input("Enter the key to remove: ")

if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print("Updated dictionary:", my_dict)
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")