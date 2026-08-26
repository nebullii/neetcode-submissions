# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root: return 0

            if root.val >= maxVal: 
                result = 1
            else:
                result = 0
            
            maxVal = max(maxVal, root.val)

            result += dfs(root.left, maxVal)
            result += dfs(root.right, maxVal)
            return result

        return dfs(root, root.val)


