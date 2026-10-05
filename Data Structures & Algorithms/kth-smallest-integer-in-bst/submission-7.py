# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return self.__dfs_with_extra_space(root, k)
        tmp = [0, None]
        self.__dfs_optimized(root, k, tmp)
        return tmp[1].val

    # TC -> O(N)
    # SC -> O(N + H)
    # N -> # of nodes
    # H -> Height of the tree
    def __dfs_with_extra_space(self, root: Optional[TreeNode], k: int) -> int:
        inorder_list = []
        self.__dfs(root, inorder_list)
        return inorder_list[k - 1]
    
    def __dfs(self, root: Optional[TreeNode], inorder_list: [int]) -> int:
        if root is None:
            return
        
        self.__dfs(root.left, inorder_list)
        inorder_list.append(root.val)
        self.__dfs(root.right, inorder_list)
    
        return

    # TC -> O(N)
    # SC -> O(H)
    # N -> # of nodes
    # H -> Height of the tree
    def __dfs_optimized(self, root: Optional[TreeNode], k: int, tmp: [int, None | Optional[TreeNode]]) -> None:
        if root is None or tmp[1] != None:
            return
        
        self.__dfs_optimized(root.left, k, tmp)
        
        tmp[0] += 1
        if tmp[0] == k:
            tmp[1] = root
            return
        
        self.__dfs_optimized(root.right, k, tmp)
        return