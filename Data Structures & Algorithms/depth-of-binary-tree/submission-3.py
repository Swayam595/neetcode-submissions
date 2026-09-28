# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # TC -> O(N)
    # SC -> O(H)
    # N -> number of nodes in the binary tree
    # H -> Height of the binary tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_sub_tree_depth = self.maxDepth(root.left)
        right_sub_tree_depth = self.maxDepth(root.right)

        return 1 + max(left_sub_tree_depth, right_sub_tree_depth)