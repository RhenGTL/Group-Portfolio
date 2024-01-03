def interpolation_search(arr, target):
    # Initialize low and high indices for the search range
    low, high = 0, len(arr) - 1

    # Perform interpolation search while the target is within the array boundaries
    while low <= high and target >= arr[low] and target <= arr[high]:
        # If only one element is remaining
        if low == high:
            if arr[low] == target:  # Check if the remaining element is the target
                return low          # Return the index if the target is found
            return -1               # Return -1 if the target is not found

        # Calculate the probable position using interpolation formula
        diff = arr[high] - arr[low]
        pos = low + ((target - arr[low]) * (high - low)) // diff

        if arr[pos] == target:  # If the probable position matches the target
            return pos          # Return the index of the target element
        elif arr[pos] < target: # If the target is in the right part of the array
            low = pos + 1       # Update the low index to search in the right part
        else:                   # If the target is in the left part of the array
            high = pos - 1      # Update the high index to search in the left part

    return -1   # Return -1 if the target is not found in the array

def interpolation_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)    # A wrapper function to call the provided 'func' with arguments and keyword arguments
