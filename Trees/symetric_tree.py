'''
    Symetric Tree:
    
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around the center).
'''

from tree_node import TreeNode
def isSymmetric(self, root: TreeNode) -> bool:
        
        def XNOR(A, B) -> bool:
            xor = (A or B) and not (A and B) and not (not A and not B)
            return not xor
        
        def isSubSymetric(root1, root2) -> bool:
            if not XNOR(root1, root2):
                return False
            else:
                if root1 and root2:            
                    if root1.val != root2.val:
                        return False
                    
                    return isSubSymetric(root1.left, root2.right) and isSubSymetric(root1.right, root2.left)
                else:
                    return True
        
        return isSubSymetric(root.left, root.right)
