# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.__reverseListIterative(head)
        return self.__reverseListRecursive(head)
    
    # TC - O(N)
    # SC - O(1)
    # N -> len of the linked list
    def __reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        return prev_node

    # TC - O(N)
    # SC - O(N)
    # N -> len of the linked list
    def __reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        next_node = self.__reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return next_node
        
