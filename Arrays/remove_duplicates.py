'''
    Remove duplicates from sorted array:

    Given an integer array nums sorted in non-decreasing order,
    remove the duplicates in-place such that each unique element appears only once.
    The relative order of the elements should be kept the same.
    if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
    It does not matter what you leave beyond the first k elements.
    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array.
    You must do this by modifying the input array in-place with O(1) extra memory.
'''
def removeDuplicates(nums) -> int:
    k = 1
    currentDuplicate = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == currentDuplicate:
            continue
        else:
            currentDuplicate = nums[i]
            nums[k] = currentDuplicate
            k += 1
    return k

# Examples testing
currNums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expectedNums = [0, 1, 2, 3, 4]

print(removeDuplicates(currNums))
