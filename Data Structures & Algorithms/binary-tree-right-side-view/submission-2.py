# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    # TC -> O(N)
    # SC -> O(W) ~ O(N/2) ~ O(N)
    # W -> max width of the tree which can be N/2 
    # N -> # of nodes in the tree
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