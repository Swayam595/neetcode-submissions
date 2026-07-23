# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:        
        inorder_index_dict = {val: i for i, val in enumerate(inorder)}
        self.__inorder_index = 0
        return self.__buildTree(preorder, inorder_index_dict, 0, len(inorder_index_dict) - 1)

    def __buildTree(self, preorder: List[int],
                        inorder_index_dict: dict, l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        
        node_val = preorder[self.__inorder_index]
        self.__inorder_index += 1
        mid = inorder_index_dict[node_val]

        node = TreeNode(val = node_val)        

        node.left = self.__buildTree(preorder, inorder_index_dict, l, mid - 1)
        node.right = self.__buildTree(preorder, inorder_index_dict, mid + 1, r)

        return node