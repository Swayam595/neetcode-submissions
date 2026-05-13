# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.__inorder_array = self.__traverse(root)
        self.__idx = -1 if len(self.__inorder_array) == 0 else 0 
        

    def next(self) -> int:
        num = self.__inorder_array[self.__idx]
        self.__idx += 1
        return num
        

    def hasNext(self) -> bool:
        return 0 <= self.__idx < len(self.__inorder_array)
    
    def __traverse(self, root: Optional[TreeNode]) -> List[TreeNode]:
        inorder_array = []
        stack = []
        curr = root

        while curr is not None or len(stack) > 0:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                top = stack.pop()
                inorder_array.append(top.val)
                curr = top.right
        return inorder_array


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()