# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.__node_count = 0
        self.__found = False
        self.__ans = None

        self.__findKthSmallest(root, k)
        return self.__ans
    
    def __findKthSmallest(self, root, k):
        # return self.__findKthSmallestRecursiveDFS(root, k)
        return self.__findKthSmallestIterativeDFS(root, k)
    
    def __findKthSmallestRecursiveDFS(self, root: Optional[TreeNode], k: int) -> int:
        if root is None or self.__found:
            return
        
        self.__findKthSmallestRecursiveDFS(root.left, k)
        
        self.__node_count += 1
        if self.__node_count == k:
            self.__ans = root.val
            self.__found = True

        self.__findKthSmallestRecursiveDFS(root.right, k)

        return

    def __findKthSmallestIterativeDFS(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        node_count = 0

        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            node_count += 1
            if node_count == k:
                self.__ans = curr.val
                break
            curr = curr.right
        
        return self.__ans