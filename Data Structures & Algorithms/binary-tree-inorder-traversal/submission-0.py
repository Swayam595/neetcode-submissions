# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.__inorderTraversalRecursively(root, [])
    
    def __inorderTraversalRecursively(self, root: Optional[TreeNode], ans) -> List[int]:
        if root is None:
            return ans
        
        self.__inorderTraversalRecursively(root.left, ans)
        ans.append(root.val)
        self.__inorderTraversalRecursively(root.right, ans)

        return ans
        