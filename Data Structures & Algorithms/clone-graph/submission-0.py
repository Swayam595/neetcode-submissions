"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
            
        q = deque()
        visited = set()

        copy = Node(val = node.val) 
        
        copy_dict = {
            node: copy
        }
        
        q.append(node)
        q.append(copy)

        while len(q) > 0:
            first = q.popleft()
            second = q.popleft()

            if first in visited:
                continue

            visited.add(first)

            for neighbour in first.neighbors:
                if neighbour not in copy_dict:
                    neighbour_value = neighbour.val
                    neighbour_copy = Node(val = neighbour_value)
                    copy_dict[neighbour] = neighbour_copy
                else:
                    neighbour_copy = copy_dict[neighbour]

                second.neighbors.append(neighbour_copy)
                
                q.append(neighbour)
                q.append(neighbour_copy)

        return copy