# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # TC - O(2 * n) ~ O(n)
    # SC - O(2 * h) ~ O(n)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]
        visit = [False]

        while len(stack) > 0:
            curr = stack.pop()
            visited = visit.pop()

            if curr is not None:
                if visited:
                    ans.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)

                    stack.append(curr.right)
                    visit.append(False)

                    stack.append(curr.left)
                    visit.append(False)
        
        return ans