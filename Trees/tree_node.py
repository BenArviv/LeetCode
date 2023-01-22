class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def create_tree(self, root, arr: list[int], index, length):
        root = None
        
        # Base case for recursion
        if index < length:
            temp = TreeNode(arr[index])  
            root = temp
            root.left = self.create_tree(root.left, arr, 2 * index + 1, length) # Insert left child
            root.right = self.create_tree(root.right, arr, 2 * index + 2, length) # Insert right child
        
        return root
    
    # Prints the tree pre-order
    def print_tree(self, root):
        if root:
            print(root.val, end = " ")
            self.print_tree(root.left)
            self.print_tree(root.right)