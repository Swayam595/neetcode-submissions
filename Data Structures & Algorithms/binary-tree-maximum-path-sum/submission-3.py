# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]
        self.__postOrder(root, ans)
        return ans[0]
    
    def __postOrder(self, root: Optional[TreeNode], ans: List[int]) -> int:
        if root is None:
            return 0
        
        left_sub_tree_max_val = max(self.__postOrder(root.left, ans), 0)
        right_sub_tree_max_val = max(self.__postOrder(root.right, ans), 0)
        
        max_value_of_sub_tree = left_sub_tree_max_val + right_sub_tree_max_val + root.val

        ans[0] = max(max_value_of_sub_tree, ans[0])
        return root.val + max(left_sub_tree_max_val, right_sub_tree_max_val)