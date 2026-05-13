# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return

        dummyHead = ListNode()
        tail = dummyHead

        mid = self.__findMid(head)

        l1 = head
        l2 = self.__reverseList(mid.next)

        mid.next = None

        while l1 is not None and l2 is not None:
            tail.next = l1
            l1 = l1.next
            tail = tail.next

            tail.next = l2
            l2 = l2.next
            tail = tail.next

        
        
        tail.next = l1
        head = dummyHead.next

    
    def __findMid(self, head):
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def __reverseList(self, head):
        prev = None
        curr = head

        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
        return prev       