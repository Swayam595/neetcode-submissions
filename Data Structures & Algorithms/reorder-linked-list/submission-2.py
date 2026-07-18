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

        mid = self.__getListMid(head)
        head2 = mid.next
        # self.__print(head2)
        mid.next = None
        head2_reversed = self.__reverseList(head2)

        while head is not None and head2_reversed is not None:
            tail.next = head
            head = head.next
            tail = tail.next

            tail.next = head2_reversed
            head2_reversed = head2_reversed.next
            tail = tail.next
        
        tail.next = head
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