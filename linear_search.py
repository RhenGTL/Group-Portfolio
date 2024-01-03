def linear_search(arr, target):
    # Iterate through the array 'arr' using enumeration
    for i, element in enumerate(arr):
        if element == target:
            return i
        elif element > target:
            return -1

    return -1
    
def linear_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)    # A wrapper function to call the provided 'func' with arguments and keyword arguments
