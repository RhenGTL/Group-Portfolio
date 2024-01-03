def ternary_search(arr, target, left, right):
    # Perform ternary search within the specified range [left, right]
    while left <= right:
        # Calculate two midpoints dividing the range into three parts
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target: # If target found at mid1
            return mid1
        if arr[mid2] == target: # If target found at mid2
            return mid2

        if target < arr[mid1]:  # If target is in the first third
            right = mid1 - 1
        elif target > arr[mid2]:    # If target is in the last third
            left = mid2 + 1
        else:            # If target is in the middle third
            left = mid1 + 1
            right = mid2 - 1

    return -1   # Return -1 if the target is not found in the array

def ternary_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)    # A wrapper function to call the provided 'func' with arguments and keyword arguments
