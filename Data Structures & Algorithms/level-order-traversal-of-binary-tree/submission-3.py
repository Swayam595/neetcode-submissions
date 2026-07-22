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
    # W -> Max width of the tree i.e. N/2
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        
        q = deque()
        q.append(root)

        while len(q) > 0:
            curr_level = []
            len_q = len(q)

            for _ in range(len_q):
                node = q.popleft()
                curr_level.append(node.val)
                
                if node.left is not None:
                    q.append(node.left)
                
                if node.right is not None:
                    q.append(node.right)
            
            ans.append(curr_level)
        
        return ans