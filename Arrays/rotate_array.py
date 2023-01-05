'''
    Rotate array:
    
    Given an array, rotate the array to the right by k steps, where k is non-negative.
'''
def rotate(nums, k):
    new_k = k % len(nums)
    if new_k == 0: # Completes full cycle, hence result is the same
        return nums
    nums2 = [0] * len(nums)
    for i in range(0, len(nums)):
        j = i + new_k if i + new_k < len(nums) else i + new_k - len(nums)
        nums2[j] = nums[i]
    
    for i in range(0, len(nums)):
        nums[i] = nums2[i]
        
# Example testing:
numList = [1,2,3,4,5,6,7]

print(numList)
rotate(numList, 3)
print(numList)