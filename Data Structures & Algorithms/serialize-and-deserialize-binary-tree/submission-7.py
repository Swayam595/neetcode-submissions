# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        return self.__bfsSerializer(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == "N":
            return None
            
        data = data.split(",")
        q = deque()
        root = TreeNode(val = data[0])
        q.append(root)
        i = 1
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

    def __bfsSerializer(self, root: Optional[TreeNode]) -> str:        
        if root is None:
            return "N"
        
        serialize_list = []
        q = deque()

        q.append(root)

        while len(q) > 0:
            node = q.popleft()

            if node is not None:
                serialize_list.append(f"{node.val}")

                q.append(node.left) 
                q.append(node.right)
            else:
                serialize_list.append("#")
                

        return ",".join(serialize_list)
