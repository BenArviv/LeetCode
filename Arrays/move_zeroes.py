'''
    Move Zeroes:
    
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.
'''

def moveZeroes(nums: list[int]):
    counter = 0
    for x in nums:
        if x == 0:
            counter +=1 
    for i in range(0, counter):
        nums.remove(0)
        nums.append(0)

# Testing example
nums_list = [0,1,0,3,12]
moveZeroes(nums_list)
print(nums_list)