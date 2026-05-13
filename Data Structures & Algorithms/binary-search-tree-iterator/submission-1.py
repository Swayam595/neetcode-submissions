# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.__stack = []
        self.__appendToStack(root)
        
        

    def next(self) -> int:
        top = self.__stack.pop()
        curr = top.right
        self.__appendToStack(curr)
        return top.val

    def hasNext(self) -> bool:
        return len(self.__stack) > 0
        
    def __appendToStack(self, root: Optional[TreeNode]) -> None:
        while root is not None:
            self.__stack.append(root)
            root = root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()