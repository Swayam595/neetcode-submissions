# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    # TC -> O(N)
    # SC -> O(W) ~ O(N / 2) ~ O(N)
    # N -> # of nodes in the tree
    # W -> max width of the tree in the queue i.e. O(N/2)
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "N"
        
        serialized_tree = []
        q = deque()

        q.append(root)

        while len(q) > 0:
            node = q.popleft()
            if node is not None:
                serialized_tree.append(f"{node.val}")
                q.append(node.left)
                q.append(node.right)
            else:
                serialized_tree.append("#")
        
        return ",".join(serialized_tree)

        
    # Decodes your encoded data to tree.
    # TC -> O(N)
    # SC -> O(W) ~ O(N / 2) ~ O(N)
    # N -> # of nodes in the tree
    # W -> max width of the tree in the queue i.e. O(N/2)
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == "N":
            return None

        data = data.split(",")

        root = TreeNode(val = data[0])
        
        i = 1
        q= deque()
        q.append(root)

        while len(q) > 0:
            node = q.popleft()

            if data[i] != "#":
                node.left = TreeNode(val = data[i])
                q.append(node.left)
            
            i += 1
            if data[i] != "#":
                node.right = TreeNode(val = data[i])
                q.append(node.right)
            i += 1
        
        return root
