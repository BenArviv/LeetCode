'''
    Validate Binary Tree Search:
    
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).
'''

from tree_node import TreeNode
import math

def isValidBST(root: TreeNode) -> bool:

    def validate(node, low=-math.inf, high=math.inf):
        # Empty trees are valid BSTs.
        if not node:
            return True
        # The current node's value must be between low and high.
        if node.val <= low or node.val >= high:
            return False

        # The left and right subtree must also be valid.
        return (validate(node.right, node.val, high) and
                validate(node.left, low, node.val))

    return validate(root)
        
# Testing examples
arr = [5,4,6,None,None,3,7]
root = TreeNode()
root = root.create_tree(root, arr, 0, len(arr))
print(isValidBST(root))