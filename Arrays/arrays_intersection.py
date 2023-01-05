'''
    Intersection of Two Arrays II:
    
    Given two integer arrays nums1 and nums 2, return an array of their intersection.
    Each element in the result must appear as many times as it shows in both arrays and you may return 
        the result in any order.
'''

def intersect(nums1: list[int], nums2: list[int]) -> int:
    new_list = []
    cont = 0
    for x in nums1:
        if x in nums2:
            new_list.append(x)
            nums2.remove(x)
    return new_list

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))
