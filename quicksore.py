def quicksort(arr):
    if len(arr) <=1:
        return(arr)
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
arr = [10, 3, 5 , 6, 4, 9, 32, 2, 26, 245, 124, 13]
sorted_arr = quicksort(arr)
print("lista ordenada:", sorted_arr)
    