# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # TC -> O(N)
    # SC -> O(H) ~ O(N)
    # N -> # of nodes in the tree
    # H -> recursive call stack space i.e. height of the tree
    ##  i.e. O(log(N)) if the tree is balanced
    ##  else O(N) if tree is skewed
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]
        self.__dfs(root, ans)
        return ans[0]
        
    def __dfs(self, root: Optional[TreeNode], ans: list[int]) -> int:
        if root is None:
            return 0
        
        left_sub_tree_sum = max(self.__dfs(root.left, ans), 0)
        right_sub_tree_sum = max(self.__dfs(root.right, ans), 0)

        max_val_of_sub_tree = left_sub_tree_sum + right_sub_tree_sum + root.val

        ans[0] = max(ans[0], max_val_of_sub_tree)
        return root.val + max(left_sub_tree_sum, right_sub_tree_sum)
