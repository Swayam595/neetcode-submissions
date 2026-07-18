# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_reversed = self.__reverseList(head)

        head_reversed_after_removal = self.__removeNthNodeFromBegining(head_reversed, n - 1)

        self.__print(head_reversed_after_removal)

        head = self.__reverseList(head_reversed_after_removal)

        return head
    
    def __reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev
    
    def __removeNthNodeFromBegining(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode()

        tail = dummy_head
        node_to_remove = head

        while n > 0 and node_to_remove is not None:
            tail.next = node_to_remove
            tail = node_to_remove
            node_to_remove = node_to_remove.next
            n -= 1
        
        if node_to_remove is not None:
            tail.next = node_to_remove.next

        return dummy_head.next

    def __print(self, head):
        while head is not None:
            print(f"{head.val}", end = "->")
            head = head.next