# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        def maxGain(root):
            if not root:
                return 0
            
            leftSum = max(maxGain(root.left), 0)
            rightSum = max(maxGain(root.right), 0)

            curMax = root.val + leftSum + rightSum
            self.max_sum = max(curMax, self.max_sum)

            return root.val + max(leftSum, rightSum)
        
        maxGain(root)
        return self.max_sum
