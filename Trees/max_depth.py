'''
    Maximum Depth of Binary Tree:
    
    Given the root of a binary tree, return its maximum depth.
'''

from tree_node import TreeNode

def max_depth(root: TreeNode) -> int:
    if not (root.left or root.right):
        return 1
    else:
        if root.left:
            left = max_depth(root.left)
        if root.right:
            right = max_depth(root.right)
        
        return 1 + max(left, right)
    
# Testing examples
arr = [1,None,2]
root = TreeNode()
root = root.create_tree(root, arr, 0, len(arr))
root.print_tree(root)
print(max_depth(root))