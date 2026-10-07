# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # TC -> O(N)
    # SC -> O(N + H) ~ O(N)
    # N -> # of nodes in the tree
    # H -> len of the call stack i.e. height of the tree 
    ##      ~ O(log(N)) for a balanced binary tree
    ##      O(N) for a skewed tree
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_node_dict = dict()

        for i, val in enumerate(inorder):
            inorder_node_dict[val] = i
            
        self.__preorder_index = 0
        return self.__build_tree(preorder, inorder, inorder_node_dict, 0, len(preorder) - 1)

    def __build_tree(self, preorder: List[int], 
                           inorder: List[int],
                           inorder_node_dict: dict[int: int],
                           l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        
        node_val = preorder[self.__preorder_index]
        mid = inorder_node_dict[node_val]

        self.__preorder_index += 1
        
        node = TreeNode(val = node_val)
        node.left = self.__build_tree(preorder, inorder, inorder_node_dict, l, mid - 1)
        node.right = self.__build_tree(preorder, inorder, inorder_node_dict, mid + 1, r)

        return node
            