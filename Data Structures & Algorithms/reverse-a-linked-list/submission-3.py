# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.__reverseListIterative(head)
        return self.__reverseListRecursive(head)

    def __reverseListIterative(self, head):
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
    
    def __reverseListRecursive(self, head):
        if head is None or head.next is None:
            return head
        
        new_head = self.__reverseListRecursive(head.next)

        head.next.next = head
        head.next = None

        return new_head