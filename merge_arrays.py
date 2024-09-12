def merge(arr1, m, arr2, n):
    last = m + n - 1
    
    i = m - 1
    j = n - 1
    
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[last] = arr1[i]
            i -= 1
        else:
            arr1[last] = arr2[j]
            j -= 1
        last -= 1
    
    while j >= 0:
        arr1[last] = arr2[j]
        j -= 1
        last -= 1

arr1 = [1, 2, 3, 0, 0, 0]
m = 3
arr2 = [2, 5, 6]
n = 3
merge(arr1, m, arr2, n)
print(arr1)  
