# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # TC -> O(N)
    # SC -> O(B)
    # N -> Number of nodes in the tree p and q when they are equal
    # B -> Max breadth of either tree
#       Best: O(log N) for balanced trees
#       Worst: O(N) for skewed trees
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False

        queue = deque()
        queue.append(p)
        queue.append(q)

        while len(queue) > 0:
            node1 = queue.popleft()
            node2 = queue.popleft()
            
            if node1 is None and node2 is None:
                continue
            
            if node1 is None or node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            
            queue.append(node1.left)
            queue.append(node2.left)

            queue.append(node1.right)
            queue.append(node2.right)

        return True