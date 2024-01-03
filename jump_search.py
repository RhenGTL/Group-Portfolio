import math # Import the math module for mathematical operations

def jump_search(arr, target):
    n = len(arr)    # Get the length of the array 'arr'
    
    # Determine the jump size for traversal, roughly the square root of the length of the array
    jump = int(math.sqrt(n))
    left, right = 0, 0  # Initialize the 'left' and 'right' pointers

    # Check if the target is outside the range of the array elements
    if target < arr[0] or target > arr[-1]:
        return -1   # Target is out of range, return -1 indicating not found

    # Perform jump search to find the range where the target might be present
    while right < n and arr[right] < target:
        left = right    # Update 'left' pointer
        right += jump   # Move 'right' pointer ahead by 'jump' steps

    # Perform linear search within the identified range
    for i in range(left, min(right, n)):    # Iterate through the identified range
        if arr[i] == target:    # If the target element is found
            return i    # Return the index of the target element

    return -1   # Return -1 if the target is not found in the array

def jump_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)    # A wrapper function to call the provided 'func' with arguments and keyword arguments
