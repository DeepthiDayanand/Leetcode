# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        if not root: 
            return 0
        
        def pathDiff(node, max_value, min_value):
            if not node:
                return max_value - min_value
            
            max_value = max(max_value, node.val)
            min_value = min(min_value, node.val)
            
            left = pathDiff(node.left, max_value, min_value)
            right = pathDiff(node.right, max_value, min_value)
            
            return max(left, right)
        
        return pathDiff(root, root.val, root.val)