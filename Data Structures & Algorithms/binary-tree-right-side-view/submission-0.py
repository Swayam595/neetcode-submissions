# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        ans = []

        q = deque()
        q.append(root)

        while len(q) > 0:
            curr_level_len = len(q)

            for _ in range(curr_level_len):
                front = q.popleft()
                if front.left is not None:
                    q.append(front.left)
                if front.right is not None:
                    q.append(front.right)
            ans.append(front.val)
        
        return ans