"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # TC -> O(V * E)
    # SC -> O(V * E)
    # V -> # of vertices
    # E -> # of edges
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        root = Node(node.val)
        q = deque()
        q.append((node, root))
        copy_node = dict()

        copy_node[node] = root
        visited = set()

        while len(q) > 0:
            node, copy = q.popleft()
            if node in visited:
                continue

            visited.add(node)

            for neighbor in node.neighbors:
                if neighbor not in copy_node:
                    copy_node[neighbor] = Node(neighbor.val)

                copy.neighbors.append(copy_node[neighbor])
                q.append((neighbor, copy_node[neighbor]))
        
        return root
