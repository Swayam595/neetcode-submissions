# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # TC -> O(N)
    # SC -> O(N)
    # N -> # of nodes in the tree
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:           
        q = deque()
        q.append(root)

        while len(q) > 0:
            node = q.popleft()
            if node is None:
                continue

            temp_left = None
            temp_right = None

            if node.left is not None:
                temp_left = node.left
            
            if node.right is not None:
                temp_right = node.right
            
            node.left = temp_right
            node.right = temp_left

            q.append(temp_left)
            q.append(temp_right)
        
        return root