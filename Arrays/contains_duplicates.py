'''
    Contains Duplicates:
    
    Given an integer array nums, return True if any value appears at least twice in the array, 
    and return False if every element is distinct.    
'''

def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        prev = nums[0]
        for i in range(1, n):
            if nums[i] >= prev: # If the list is alreadu sorted we don't need to sort it again
                prev = nums[i]
            else:
                nums.sort()
                break

        for i in range(1, n):
            if nums[i - 1] == nums[i]:
                return True
        
        return False