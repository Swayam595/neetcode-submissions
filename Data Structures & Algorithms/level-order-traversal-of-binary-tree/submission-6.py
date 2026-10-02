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
    # N -> # of nodes
    # W -> Max width of the tree i.e N/2
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: 
            return []

        q = deque()
        ans = []

        q.append(root)

        while len(q) > 0:
            q_len = len(q)
            curr_level = []

            for _ in range(q_len):
                front = q.popleft()
                curr_level.append(front.val)

                if front.left:
                    q.append(front.left)
                
                if front.right:
                    q.append(front.right)
            ans.append(curr_level)
        
        return ans