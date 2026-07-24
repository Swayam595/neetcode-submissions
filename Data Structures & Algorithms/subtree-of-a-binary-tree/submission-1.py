# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.__isSubtreeBruteForce(root, subRoot)

    def __isSubtreeBruteForce(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.__found = False

        return self.__dfsTraverse(root, subRoot)

    def __dfsTraverse(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.__found:
            return True
        
        if root is None:
            return False or self.__found

        if root.val == subRoot.val:
            self.__found = self.__compare(root, subRoot)

        found_in_l = self.__dfsTraverse(root.left, subRoot)
        found_in_r = self.__dfsTraverse(root.right, subRoot)

        return self.__found or found_in_l or found_in_r
    
    def __compare(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False
        
        if root.val != subRoot.val:
            return False

        found_in_l = self.__compare(root.left, subRoot.left)
        found_in_r = self.__compare(root.right, subRoot.right)

        return found_in_l & found_in_r


