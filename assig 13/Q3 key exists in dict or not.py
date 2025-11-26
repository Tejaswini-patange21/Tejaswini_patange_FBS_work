my_dict = {"name": "tanmayi", "age":4,"city": "pune"}

key = input("Enter the key to check: ")

if key in my_dict:
    print(f"Key '{key}' exists in the dictionary.")
else:
    print(f"Key '{key}' does NOT exist in the dictionary.")