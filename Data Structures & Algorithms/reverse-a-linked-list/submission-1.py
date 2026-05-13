# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None
#         curr = head

#         while curr is not None:
#             nextNode = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nextNode
        
#         return prev

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.__reverse(head)
    
    def __reverse(self, head):
        if head is None:
            return None
        
        newHead = head

        if head.next is not None:
            newHead = self.__reverse(head.next)
            head.next.next = head
        
        head.next = None

        return newHead
        