# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # TC -> O(N)
    # SC -> O(1)
    # N -> # of nodes in the linked list
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        prev = dummy_head

        dummy_head.next = self.__reverse_list(head)
        
        i = 1
        curr = dummy_head.next

        while curr is not None and i < n:
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = curr.next
        return self.__reverse_list(dummy_head.next)

    # TC -> O(N)
    # SC -> O(1)
    # N -> # of nodes in the linked list
    def __reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev