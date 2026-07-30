"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.__cloneGraphByDfs(node, dict())
    
    def __cloneGraphByDfs(self, node: Optional['Node'], seen: dict()) -> Optional['Node']:
        if node is None:
            return None
        
        if node in seen:
            return seen[node]
        
        clone = Node()
        clone.val = node.val
        seen[node] = clone

        for neighbor in node.neighbors:
            clone_neighbor = self.__cloneGraphByDfs(neighbor, seen)
            clone.neighbors.append(clone_neighbor)
        
        return clone