# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -float('inf')
        
        def subtree(node: Optional[TreeNode]) -> int:
            nonlocal max_path
            if not node:
                return 0
            
            leftST = max(subtree(node.left), 0)
            rightST = max(subtree(node.right), 0)
            
            max_path = max(max_path, leftST +rightST + node.val)
            
            return max(leftST + node.val, rightST + node.val)
        
        subtree(root)
        return max_path
            
        
        
        
        
