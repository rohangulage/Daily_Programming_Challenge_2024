def first_element_k_times(arr, k):
    count_map = {}
    
    for num in arr:
        count_map[num] = count_map.get(num, 0) + 1
    
    for num in arr:
        if count_map[num] == k:
            return num
    
    return -1

arr = [1, 3, 7, 4, 3, 4, 8, 7]
k = 2
print(first_element_k_times(arr, k))  
