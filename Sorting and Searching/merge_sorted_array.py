'''
    Merge Sorted Array:
    
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements
        in nums1 and nums 2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
    To accomodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements 
        are set to 0 and should be ignored.
    nums2 has a length of n.
'''

# Suggestion: Start from the end of nums1, with indices decreasing.

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = j = 0
    if n == 0:
        return
    elif m == 0:
        for i in range(n):
            nums1[i] = nums2[i]
        return
        
    nums3 = []
    while i + j < m + n:
        if j >= n or (nums1[i] < nums2[j] and i < m):
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1
        
    for i in range(n + m):
        nums1[i] = nums3[i]
            
# Testing examples
array1 = [4,0,0,0,0,0]
array2 = [1,2,3,5,6]
m = 1
n = 5
merge(array1, m, array2, n)
print(array1)