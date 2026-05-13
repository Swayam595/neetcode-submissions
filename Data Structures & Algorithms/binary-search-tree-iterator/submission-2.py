# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.__curr = root
        self.__stack = []

    def next(self) -> int:
        while self.__curr is not None:
            self.__stack.append(self.__curr)
            self.__curr = self.__curr.left

        top = self.__stack.pop()
        self.__curr = top.right
        return top.val

    def hasNext(self) -> bool:
        return self.__curr is not None or len(self.__stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()