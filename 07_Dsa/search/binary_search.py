def binary_seach(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [34,44,56,70,82,98,97]  
x = 97
result = binary_seach(arr, x)   

if result != -1:
    print('Element is present at index', str(result))
else:
    print('element not present in array')