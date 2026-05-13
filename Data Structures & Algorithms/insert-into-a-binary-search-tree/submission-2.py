# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # return self.__insertIntoBSTRecursively(root, val)
        return self.__insertIntoBSTIteratively(root, val)

    def __insertIntoBSTRecursively(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.__insertIntoBSTRecursively(root.left, val)
        elif val > root.val:
            root.right = self.__insertIntoBSTRecursively(root.right, val)
        
        return root
    
    def __insertIntoBSTIteratively(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if root is None:
            return new_node
        
        curr = root
        inserted = False

        while curr is not None and not inserted:
            if val < curr.val:
                if curr.left is None:
                    curr.left = new_node
                    inserted = True
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = new_node
                    inserted = True
                curr = curr.right
        
        return root
