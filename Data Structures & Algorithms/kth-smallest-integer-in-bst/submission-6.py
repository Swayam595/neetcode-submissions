# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # TC -> O(N)
    # SC -> O(N)
    # N -> # pf nodes in the tree
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.__inorder_list = list()
        self.__inorder_traversal(root)
        return self.__inorder_list[k - 1]
    
    def __inorder_traversal(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        
        self.__inorder_traversal(root.left)
        self.__inorder_list.append(root.val)
        self.__inorder_traversal(root.right)
        return
        
