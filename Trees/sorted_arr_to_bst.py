'''
    Convert Sorted Array to Binary Search Tree:
    
    Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
'''

import math
from tree_node import TreeNode

def sortedArrayToBST(nums: list[int]) -> TreeNode:
    import math
    
    def convertRec(nums, root) -> TreeNode:
        if nums == []:
            root = None
            return
        n = math.floor(len(nums) / 2)
        root.val = nums[n]
        root.left = TreeNode()
        root.right = TreeNode()
        root.left = convertRec(nums[:n], root.left)
        root.right = convertRec(nums[n + 1:], root.right)
        
        return root
    
    root = TreeNode()
    root = convertRec(nums, root)
    
    return root

# Testing examples
array = [-10,-3,0,5,9]
root = sortedArrayToBST(array)
root.print_tree(root)