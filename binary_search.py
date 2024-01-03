def binary_search(array, target):
    # Check if the target is outside the range of the array elements
    if target < array[0] or target > array[-1]:
        return -1   # Target is out of range, return -1 indicating not found

    low, high = 0, len(array) - 1   # Set initial low and high indices

    # Perform binary search
    while low <= high:
        mid = low + ((high - low) >> 1) # Calculate the middle index

        if array[mid] == target:    # If the middle element is the target
            return mid              # Return the index of the target element
        elif array[mid] < target:   # If the target is in the right half of the array
            low = mid + 1           # Update the low index to search in the right half
        else:                       # If the target is in the left half of the array
            high = mid - 1          # Update the high index to search in the left half

    return -1   # Return -1 if the target is not found in the array
    
def binary_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)    # A simple wrapper function to call the provided 'func' with arguments and keyword arguments
