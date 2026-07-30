"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # return self.__cloneGraphByDfs(node, dict())
        return self.__cloneGraphByBfs(node)
    
    # TC - O(V + E)
    # SC - O(V)
    # V - is the number of vertices (nodes) in the graph.
    # E - is the number of edges in the graph.
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

    # TC - O(V + E)
    # SC - O(V)
    # V - is the number of vertices (nodes) in the graph.
    # E - is the number of edges in the graph.
    def __cloneGraphByBfs(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        seen = dict()
        seen[node] = Node(node.val)

        q = deque([node])

        while len(q) > 0:
            curr = q.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in seen:
                    seen[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                seen[curr].neighbors.append(seen[neighbor])

        return seen[node]