from collections import deque

def maxSlidingWindow(nums, k):
    if not nums:
        return []
    
    if k == 1:
        return nums
    
    deq = deque()
    result = []
    
    for i in range(len(nums)):
        if deq and deq[0] < i - k + 1:
            deq.popleft()
        
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        
        deq.append(i)
        
        if i >= k - 1:
            result.append(nums[deq[0]])
    
    return result

arr = [1, 3, -1, -3, 5, 3, 5, 7]
k = 3
print(maxSlidingWindow(arr, k))  
