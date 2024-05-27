class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    
        result = []
        u_stack = []

        while root or u_stack:
            # If end of current left sub-tree
            if root is None:
                root = u_stack.pop()
                root = root.right
            
            # If can go left further
            else:
                result.append(root.val)
                u_stack.append(root)
                root = root.left

        return result
