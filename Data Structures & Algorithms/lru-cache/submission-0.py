class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.__cache_capacity = capacity
        self.__key_dict = dict()
        self.__dummy = Node()
        self.__tail = self.__dummy
        self.__cache_curr_len = 0

    def get(self, key: int) -> int:
        value = -1
        if key in self.__key_dict:
            node = self.__key_dict[key]
            value = node.val
            self.__remove_node_from_cache(node)
            self.__add_node_at_head(node)
        
        return value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.__key_dict:
            self.__put_new_key(key, value)
        else:
            node = self.__key_dict[key]
            node.val = value
            self.__remove_node_from_cache(node)
            self.__add_node_at_head(node)
    
    def __put_new_key(self, key, val):
        new_node = Node(key, val)
        if self.__cache_curr_len == self.__cache_capacity:
            tail_node = self.__get_tail_node()
            tail_node_key = tail_node.key
            tail_node.prev.next = None
            tail_node.prev = None
            del self.__key_dict[tail_node_key]
            self.__cache_curr_len -= 1
        self.__key_dict[key] = new_node
        self.__add_node_at_head(new_node)
        self.__cache_curr_len += 1

    def __get_tail_node(self):
        curr = self.__dummy.next
        while curr.next is not None:
            curr = curr.next
        return curr
    
    def __add_node_at_head(self, node):
        next_node = self.__dummy.next
        self.__dummy.next = node
        node.prev = self.__dummy
        if next_node is not None:
            node.next = next_node
            next_node.prev = node

    def __remove_node_from_cache(self, node):
        prev_node = node.prev
        next_node = node.next

        if prev_node is not None:
            prev_node.next = next_node
        
        if next_node is not None:
            next_node.prev = prev_node
