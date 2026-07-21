# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
            
        q = deque()
        q.append(root)

        while len(q) > 0:
            node = q.popleft()

            left_child = node.left
            right_child = node.right

            node.left = right_child
            node.right = left_child

            if left_child is not None:
                q.append(left_child)
            
            if right_child is not None:
                q.append(right_child)
        
        return root