def binary_search(target, arr):
    arr.sort()    

    low = 0
    high = len(arr) - 1
    while low <= high:
        # With every iteration we need to calculate new median
        median = (low + high) // 2
        if arr[median] == target:
            return True
        if arr[median] < target:
            low = median + 1
        else: 
            high = median - 1 
    return False


searched = binary_search([1, 2, 3, 4, 5], 24) 

print(searched) # false

