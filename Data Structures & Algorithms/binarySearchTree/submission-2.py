class TreeNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.__root = None


    def insert(self, key: int, val: int) -> None:
        if self.__root is None:
            self.__root = TreeNode(key, val)
        else:
            self.__insert_recursively(self.__root, key, val)

    def get(self, key: int) -> int:
        curr = self.__root

        while curr is not None:
            if key == curr.key:
                return curr.val
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        
        return -1


    def getMin(self) -> int:
        if self.__root is None:
            return -1

        return self.__getMinNode(self.__root).val

    def getMax(self) -> int:
        if self.__root is None:
            return -1
    
        return self.__getMaxNode(self.__root).val

    def remove(self, key: int) -> None:
        self.__root = self.__remove_recursively(self.__root, key)


    def getInorderKeys(self) -> List[int]:
        curr = self.__root
        inorder_list = []

        while curr is not None:
            if curr.left is None:
                inorder_list.append(curr.key)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right is not None and pred.right != curr:
                    pred = pred.right
                
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    inorder_list.append(curr.key)
                    curr = curr.right
        
        return inorder_list

    def __insert_recursively(self, root, key, val):
        if root is None:
            return TreeNode(key, val)
        
        if key < root.key:
            root.left = self.__insert_recursively(root.left, key, val)
        elif key > root.key:
            root.right = self.__insert_recursively(root.right, key, val)
        else:
            root.val = val
        
        return root      

    def __remove_recursively(self, root, key):
        if root is None:
            return None
        
        if key < root.key:
            root.left = self.__remove_recursively(root.left, key)
        elif key > root.key:
            root.right = self.__remove_recursively(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_node = self.__getMinNode(root.right)
                root.key = min_node.key
                root.val = min_node.val
                root.right = self.__remove_recursively(root.right, min_node.key)
        return root
            
    def __getMinNode(self, root):
        while root.left is not None:
            root = root.left
        
        return root
    
    def __getMaxNode(self, root):
        while root.right is not None:
            root = root.right
        
        return root
