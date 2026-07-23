# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        q = deque()
        tree_val_range = [-float('inf'), float('inf')]
        q.append([root, tree_val_range])

        while len(q) > 0:
            node, tree_val_range = q.popleft()

            if not (tree_val_range[0] < node.val and node.val < tree_val_range[1]):
                return False
            

            left_sub_tree_val_new_range = [tree_val_range[0], min(tree_val_range[1], node.val)]
            right_sub_tree_val_new_range = [max(tree_val_range[0], node.val), tree_val_range[1]]

            if node.left is not None:
                q.append([node.left, left_sub_tree_val_new_range])
            
            if node.right is not None:
                q.append([node.right, right_sub_tree_val_new_range])

        return True