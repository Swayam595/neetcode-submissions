# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_list = []
        self.__dfs(root, inorder_list)
        return inorder_list[k - 1]
    
    def __dfs(self, root: Optional[TreeNode], inorder_list: [int]) -> int:
        if root is None:
            return
        
        self.__dfs(root.left, inorder_list)
        inorder_list.append(root.val)
        self.__dfs(root.right, inorder_list)
    
        return