# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        s = 0

        def helper(root):
            nonlocal s

            if not root:
                return False
            
            s += root.val
            
            if not root.left and not root.right:
                if s == targetSum:
                    return True
            
            if helper(root.left):
                return True
            if helper(root.right):
                return True
            s -= root.val
            return False
        return helper(root)