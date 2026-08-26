# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def preorder(root):
            if not root:
                res.append("N")
                return
            
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return ",".join(res)
                
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.index = 0

        def dfs(root):
            if vals[self.index] == "N":
                self.index += 1
                return None

            root = TreeNode(int(vals[self.index]))
            self.index += 1
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            return root
        
        return dfs(root)


