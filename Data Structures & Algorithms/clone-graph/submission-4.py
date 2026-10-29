"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # TC -> O(V + E)
    # SC -> O(V)
    # V -> # of vertices
    # E -> # of edges
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        if root is None:
            return None
        
        q = deque()
        copy_dict = dict()
        visited = set()

        copy_dict[root] = Node(root.val)
        q.append((root, copy_dict[root]))

        while len(q) > 0:
            node, copy = q.popleft()

            for neighbor in node.neighbors:
                if neighbor not in copy_dict:
                    copy_dict[neighbor] = Node(neighbor.val)
                    q.append((neighbor, copy_dict[neighbor]))

                copy.neighbors.append(copy_dict[neighbor])
        
        return copy_dict[root]
