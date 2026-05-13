class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.__cache_capacity = capacity
        self.__cache_curr_len = 0

        self.__key_dict = dict()

        self.__dummy_head = Node()
        self.__dummy_tail = Node
        
        self.__dummy_head.next = self.__dummy_tail
        self.__dummy_tail.prev = self.__dummy_head
        

    def get(self, key: int) -> int:
        value = -1
        if key in self.__key_dict:
            node = self.__key_dict[key]
            value = node.val
            self.__remove_node(node)
            self.__insert_node(node)
        
        return value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.__key_dict:
            self.__put_new_key(key, value)
        else:
            node = self.__key_dict[key]
            node.val = value
            self.__remove_node(node)
            self.__insert_node(node)
    
    def __put_new_key(self, key, val):
        new_node = Node(key, val)
        if self.__cache_curr_len == self.__cache_capacity:
            self.__remove_tail()
            self.__cache_curr_len -= 1
            
        self.__insert_node(new_node)
        self.__cache_curr_len += 1
    
    def __insert_node(self, node):
        self.__insert_at_head(node)
        self.__insert_key_in_key_dict(node)
        
    def __insert_at_head(self, node):
        next_node = self.__dummy_head.next

        self.__dummy_head.next = node
        node.prev = self.__dummy_head
        
        node.next = next_node
        next_node.prev = node
    
    def __insert_key_in_key_dict(self, node):
        key = node.key
        self.__key_dict[key] = node


    def __remove_tail(self):
        tail = self.__dummy_tail.prev
        self.__remove_node(tail)

    def __remove_node(self, node):
        self.__remove_node_from_cache(node)
        self.__remove_key_from_key_dict(node)
    
    def __remove_node_from_cache(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
    
    def __remove_key_from_key_dict(self, node):
        key = node.key
        del self.__key_dict[key]