# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # TC -> O(N)
    # SC -> O(1)
    # N -> len of the linked list
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        
        mid = self.__find_mid(head)
        h1 = head
        h2 = mid.next

        mid.next = None

        h2_reversed = self.__reverse_list(h2)

        dummy_head = ListNode()
        tail = dummy_head

        while h1 is not None and h2_reversed is not None:
            tail.next = h1
            h1 = h1.next
            tail = tail.next

            tail.next = h2_reversed
            h2_reversed = h2_reversed.next
            tail = tail.next
        
        if h1 is not None:
            tail.next = h1
        
        if h2_reversed is not None:
            tail.next = h2_reversed
        
    
    # TC -> O(N)
    # SC -> O(1)
    # N -> len of the linked list
    def __find_mid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow

    # TC -> O(N)
    # SC -> O(1)
    # N -> len of the linked list
    def __reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev