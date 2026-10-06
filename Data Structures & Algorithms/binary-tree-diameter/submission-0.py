# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.__max_diameter = 0
        self.__find_diameter(root)
        return self.__max_diameter 
    
    def __find_diameter(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.__find_diameter(root.left)
        right = self.__find_diameter(root.right)

        self.__max_diameter = max(self.__max_diameter, left + right)
        return max(left, right) + 1