# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    # TC -> O(N)
    # SC -> O(N)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False

        queue = deque()
        queue.append(p)
        queue.append(q)

        while len(queue) > 0:
            node_1 = queue.popleft()
            node_2 = queue.popleft()

            if node_1 is None and node_2 is None:
                continue
            
            if node_1 is None or node_2 is None:
                return False
            
            if node_1.val != node_2.val:
                return False
            
            queue.append(node_1.left)
            queue.append(node_2.left)

            queue.append(node_1.right)
            queue.append(node_2.right)
        
        return True
            
