'''
    Binary Tree Level Order Traversal:
    
    Given the root of a binary tree, return the level order traversal of its nodes' values
    (i.e., from left to right, level by level).
'''

from tree_node import TreeNode

def levelOrder(root: TreeNode) -> list[list[int]]:
        
    def levelOrderRec(root, i, arr) -> list[list[int]]:
        if root == None or root.val == None:
            return None
        
        if len(arr) < i:
            arr.append([])
        arr[i - 1].append(root.val)
        i += 1
        levelOrderRec(root.left, i, arr)
        levelOrderRec(root.right, i, arr)
        
        return arr
        
    if root == None:
        return []
    output = [[]]
    levelOrderRec(root, 1, output)
    
    return output

# Testing example
arr = [3,9,20,None, None,15,7]
root = TreeNode()
root = root.create_tree(root, arr, 0, len(arr))
print(levelOrder(root))