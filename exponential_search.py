def binary_search(arr, target, left, right):
    if target < arr[left] or target > arr[right]:
        return -1

    while left <= right:
        mid = left + ((right - left) >> 1)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def exponential_search(arr, target):
    if arr[0] == target:    # Check if the target is the first element of the array
        return 0            # Return the index 0 if the target is found at the beginning of the array

    i = 1           # Initialize 'i' for exponential probing
    n = len(arr)    # Get the length of the array

    # Find the range for binary search using exponential probing
    while i < n and arr[i] <= target:
        i <<= 1     # Double 'i' for exponential growth

    # Perform binary search within the range for the target element
    return binary_search(arr, target, i >> 1, min(i, n) - 1)

def exponential_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)    # A wrapper function to call the provided 'func' with arguments and keyword arguments
