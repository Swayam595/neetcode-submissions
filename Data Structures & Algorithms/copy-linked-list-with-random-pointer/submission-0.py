"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while curr is not None:
            nextNode = curr.next
            newNode = Node(x = curr.val)
            newNode.next = nextNode
            curr.next = newNode
            curr = nextNode
        
        tail1 = head

        while tail1 is not None:
            tail2 = tail1.next
            if tail1.random is not None:
                tail2.random = tail1.random.next
            tail1 = tail1.next.next
        
        dummy = Node(x = -1)
        tail = dummy
        curr = head

        while curr is not None:
            copiedNode = curr.next
            nextNode = copiedNode.next
            tail.next = copiedNode
            tail = tail.next
            curr.next = nextNode
            curr = nextNode
        
        return dummy.next