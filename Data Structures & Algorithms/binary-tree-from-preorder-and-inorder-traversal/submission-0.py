# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.__preorder = preorder
        self.__inorder = inorder
        self.__preorder_index = 0
        self.__inorder_index_dict = {val: i for i, val in enumerate(self.__inorder)} 

        return self.__build(0, len(self.__inorder) - 1)

    def __build (self, l, r):
        if l > r:
            return None
        
        root_val = self.__preorder[self.__preorder_index]
        self.__preorder_index += 1
        mid = self.__inorder_index_dict[root_val]

        root = TreeNode(root_val)
        root.left = self.__build(l, mid - 1)
        root.right = self.__build(mid + 1, r)

        return root