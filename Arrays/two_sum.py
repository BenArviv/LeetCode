'''
    Two Sum:
    
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up
        to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
'''

def twoSum(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    if n == 2: # List containes just two elements
        return [0, 1]
    sorted = True
    
    nums2 = [nums[0]]
    for i in range(1, n): # Copies the list to a new one in order to sort it
        nums2.append(nums[i])
        if nums[i] < nums[i - 1]:
            sorted = False
    if not sorted:
        nums2.sort()
        
    i = 0
    j = n - 1
    res_list = []
    sum = nums2[i] + nums2[j]
    
    while i <= j:
        if sum == target:
            res_list.append(i)
            res_list.append(j)
            break
        elif sum > target:
            j -= 1
            sum = nums2[i] + nums2[j]
        else:
            i += 1
            sum = nums2[i] + nums2[j]
        
    index1 = nums2[res_list[0]]
    index2 = nums2[res_list[1]]
    res_list[0] = nums.index(index1) # Sets actual indices according to the original list
    res_list[1] = nums.index(index2)
    
    if res_list[0] == res_list[1]: # A number appears twice in the list
        nums.remove(nums[res_list[1]])
        res_list[1] = nums.index(index2) + 1
    
    return res_list
    
# Testing examples
nums = [3, 2, 3]
target = 6
print(twoSum(nums, target))