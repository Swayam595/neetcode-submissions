# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.__inorderTraversalRecursively(root, [])
        # return self.__inorderTraversalIteratively(root)
        return self.__inorderMorisTraversal(root)

    def __inorderTraversalIteratively(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        curr = root
        stack = []

        while curr is not None or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        
        return ans
    
    def __inorderMorisTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        curr = root

        while curr is not None:
            if curr.left is None:
                ans.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right is not None and prev.right != curr:
                    prev = prev.right
                
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    ans.append(curr.val)
                    curr = curr.right
        
        return ans


    def __inorderTraversalRecursively(self, root: Optional[TreeNode], ans) -> List[int]:
        if root is None:
            return ans
        
        self.__inorderTraversalRecursively(root.left, ans)
        ans.append(root.val)
        self.__inorderTraversalRecursively(root.right, ans)

        return ans
        