# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # TC -> O(N * M)
    # SC -> O(W1 + W2) ~ O(N / 2 + M / 2) ~ O(N + M)
    # N -> # of nodes in the tree
    # M -> # of nodes in the subtree
    # W1 -> Max width of the tree
    # W2 -> Max width of the subtree
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)

        while len(q) > 0:
            node = q.popleft()

            if node.val == subRoot.val and self.__compare(node, subRoot):
                return True
            
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        
        return False
    
    def __compare(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        q = deque()
        q.append([tree1, tree2])

        while len(q) > 0:
            node1, node2 = q.popleft()

            if node1 is None and node2 is None:
                continue
            
            if node1 is None or node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            
            q.append([node1.left, node2.left])
            q.append([node1.right, node2.right])
        
        return True