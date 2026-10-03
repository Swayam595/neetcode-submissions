# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        q = deque()

        q.append(root)

        while len(q) > 0:
            q_len = len(q)
            for _ in range(q_len):
                front = q.popleft()

                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            ans.append(front.val)
        
        return ans