def binary_search(arr, target):
    arr.sort()    
    low = 0
    high = len(arr) - 1

    while low >= low:
        median = (high + low) // 2
        if arr[median] == target:
            return True
        if arr[median] > target:
            low = median
        else:
            high = median
    return False


val = binary_search([1, 2, 3, 4, 5], 24) 

print(val) # false