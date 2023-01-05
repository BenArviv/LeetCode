'''
    Single Number:
    
    Given a non-empty array of integers nums, every element appears twice except for one.
    Find that single one.
    
    You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

def singleNumber(nums) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
        
    new_list = []
    for x in nums:
        if not x in new_list:
            new_list.append(x)
        else:
            new_list.remove(x)

    return new_list[0]

# Example testing
nums = [4,1,2,1,2]

print(singleNumber(nums))