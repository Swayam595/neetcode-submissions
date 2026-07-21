# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # TC -> O(log(N))
    # SC -> O(1)
    # N -> # of nodes in the Tree
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root is not None:
            if p.val <= root.val and root.val <= q.val:
                return root
            
            if q.val <= root.val and root.val <= p.val:
                return root
            
            if p.val < root.val and q.val < root.val:
                root = root.left
            else:
                root = root.right
        
        return None
