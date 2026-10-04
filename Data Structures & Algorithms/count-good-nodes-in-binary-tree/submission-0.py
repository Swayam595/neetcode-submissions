# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # TC -> O(N)
    # SC -> O(H)
    # N -> # of nodes in the tree
    # H -> Height of the tree i.e. log(N) if balanced else N if skwed tree
    def goodNodes(self, root: TreeNode) -> int:
        return self.__count_good_nodes(root, root.val)
    
    def __count_good_nodes(self, root: TreeNode, max_val: int) -> int:
        if root is None:
            return 0
        
        count = 0
        if root.val >= max_val:
            count += 1

        max_val = max(max_val, root.val)

        left_sub_tree_good_nodes_count = self.__count_good_nodes(root.left, max_val)
        right_sub_tree_good_nodes_count = self.__count_good_nodes(root.right, max_val)

        return count + left_sub_tree_good_nodes_count + right_sub_tree_good_nodes_count