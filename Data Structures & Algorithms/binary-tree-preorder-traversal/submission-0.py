# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root

        ans = []

        while curr is not None or len(stack) > 0:
            if curr is not None:
                ans.append(curr.val)
                if curr.right is not None:
                    stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        
        return ans