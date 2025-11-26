# Function for Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Function for Binary Search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid  # Element found
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

# Main program
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Sorting the list using Selection Sort
print("\nUnsorted List:", numbers)
sorted_list = selection_sort(numbers)
print("Sorted List:", sorted_list)

# Searching for an element using Binary Search
key = int(input("\nEnter the number to search: "))
result = binary_search(sorted_list, key)

if result != -1:
    print(f"Element {key} found at position {result} (index starts from 0).")
else:
    print(f"Element {key} not found in the list.")
