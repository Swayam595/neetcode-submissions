# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.__reverse_list_iteration(head)
        return self.__reverse_list_recursive(head)

    # TC -> O(N)
    # SC -> O(N)
    # N -> # of nodes in the linked list
    def __reverse_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        next_node = self.__reverse_list_recursive(head.next)
        head.next.next = head
        head.next = None

        return next_node

    # TC -> O(N)
    # SC -> O(1)
    # N -> # of nodes in the linked list
    def __reverse_list_iteration(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev