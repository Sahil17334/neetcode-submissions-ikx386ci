# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, remaining):
            if not root:
                return False
            
            remaining -= root.val

            if not root.left and not root.right:
                return remaining == 0
            
            return helper(root.left, remaining) or helper(root.right, remaining)
        return helper(root, targetSum)
            
