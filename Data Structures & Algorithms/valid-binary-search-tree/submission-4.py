# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # TC -> O(N)
    # SC -> O(W) ~ O(N / 2) ~ O(N)
    # N -> # of nodes in the tree
    # W -> max width of the tree i.e. O(N / 2)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()

        q.append([root, -float('inf'), float('inf')])

        while len(q) > 0:
            node, min_val, max_val = q.popleft()

            if not (min_val < node.val < max_val):
                return False
            
            if node.left is not None:
                q.append([node.left, min_val, node.val])
            
            if node.right is not None: 
                q.append([node.right, node.val, max_val])
        
        return True