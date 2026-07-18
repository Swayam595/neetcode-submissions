# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return 
        
        dummy_head = ListNode()
        tail = dummy_head

        l1 = head
        mid = self.__getListMid(l1)

        l2 = mid.next
        mid.next = None
        
        l2 = self.__reverseList(l2)

        while l1 is not None and l2 is not None:
            tail.next = l1
            l1 = l1.next
            tail = tail.next

            tail.next = l2
            l2 = l2.next
            tail = tail.next
        
        tail.next = l1
        head = dummy_head.next
    
    def __getListMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def __reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
    
    def __print(self, head):
        while head is not None:
            print(f"{head.val}", end="->")
            head = head.next