"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # TC -> O(N)
    # SC -> O(1)
    # N -> len of the linked list
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        
        self.__create_copy(head)
        self.__join_random_pointer(head)
        head, copied_head = self.__extract_copied_linked_list(head)

        return copied_head
    
    def __create_copy(self, head: 'Optional[Node]') -> None:
        while head is not None:
            next_node = head.next
            copied_node = Node(head.val, next_node)
            head.next = copied_node
            head = next_node
    
    def __join_random_pointer(self, head: 'Optional[Node]') -> None:
        while head is not None:
            copied_node = head.next
            
            if head.random is not None:
                random_node = head.random
                random_node_copied = random_node.next
                copied_node.random = random_node_copied
            
            head = copied_node.next

    def __extract_copied_linked_list(self, head: 'Optional[Node]') -> ('Optional[Node]', 'Optional[Node]'):
        dummy1 = Node(0)
        tail1 = dummy1

        dummy2 = Node(0)
        tail2 = dummy2

        while head is not None:
            h1 = head
            h2 = head.next

            next_node = head.next.next

            tail1.next = h1
            tail1 = tail1.next

            tail2.next = h2
            tail2 = tail2.next

            head.next = next_node
            head = next_node
        
        return (dummy1.next, dummy2.next)



        