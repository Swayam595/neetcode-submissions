# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # TC - O(N)
    # SC - O(N)
    # N -> # of nodes in the tree
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        q = deque()
        
        q.append([root, -float('inf'), float('inf')])

        while len(q) > 0:
            node, left, right = q.popleft()

            if not (left < node.val and node.val < right):
                return False

            if node.left is not None:
                q.append([node.left, left, node.val])
            
            if node.right is not None:
                q.append([node.right, node.val, right])

        return True