# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.__node_count = 0
        self.__found = False
        self.__ans = None

        self.__findKthSamllest(root, k)
        return self.__ans
    
    def __findKthSamllest(self, root, k):
        if root is None or self.__found:
            return
        
        self.__findKthSamllest(root.left, k)
        
        self.__node_count += 1
        if self.__node_count == k:
            self.__ans = root.val
            self.__found = True

        self.__findKthSamllest(root.right, k)
        
        return