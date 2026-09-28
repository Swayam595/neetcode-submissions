class Node:
    def __init__(self, key: int = 0, val: int = 0, next: Node = None, prev: Node = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    # TC -> O(1)
    # SC -> O(N)
    # N -> capacity of the cache
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__dict = dict()

        self.__head = Node()
        self.__tail = Node()

        self.__head.next = self.__tail
        self.__tail.prev = self.__head

    def get(self, key: int) -> int:
        value = -1
        if key in self.__dict:
            node = self.__dict[key]
            self.__remove_node(node)
            self.__insert_node(node)
            value = node.val
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.__dict:
            node = self.__dict[key]
            node.val = value
            self.__remove_node(node)
            self.__insert_node(node)
        else:
            self.__put_new_key(key, value)

    def __put_new_key(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        if self.__capacity == len(self.__dict):
            self.__remove_tail()
        self.__insert_node(new_node)

    def __insert_node(self, node: Node) -> None:
        self.__insert_at_head(node)
        self.__insert_key_in_dict(node)
    
    def __insert_at_head(self, node: Node) -> None:
        next_node = self.__head.next

        self.__head.next = node
        node.next = next_node

        next_node.prev = node
        node.prev = self.__head

    def __insert_key_in_dict(self, node: Node) -> None:
        self.__dict[node.key] = node

    def __remove_tail(self) -> None:
        tail = self.__tail.prev
        self.__remove_node(tail)

    def __remove_node(self, node: Node) -> None:
        self.__remove_node_from_cache(node)
        self.__remove_key_from_dict(node.key)
    
    def __remove_node_from_cache(self, node: Node) -> None:
        next_node = node.next
        prev_node = node.prev

        prev_node.next = next_node
        next_node.prev = prev_node

    def __remove_key_from_dict(self, key: int) -> None:
        del self.__dict[key]
        
    
