# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # return self.__reverse_k_group_recursive(head, k)
        return self.__reverse_k_group_iterative(head, k)

    # TC -> O(N + k)
    # SC -> O(1)
    # N -> # of nodes in the linked list
    def __reverse_k_group_iterative(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = ListNode()
        tail = dummy

        while head is not None:
            i = 0
            curr = head
            prev = None
            while i < k and curr is not None:
                prev = curr
                curr = curr.next
                i += 1
            
            if i < k:
                break
            
            prev.next = None
            new_head, new_tail = self.__reverse_list(head)
            tail.next = new_head
            new_tail.next = curr
            tail = new_tail
            head = curr

        return dummy.next

    # TC -> O(N + k)
    # SC -> O(N / k)
    # N -> # of nodes in the linked list
    def __reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        i = 0
        k_th_node = head
        prev = None
        while i < k and k_th_node is not None:
            prev = k_th_node
            k_th_node = k_th_node.next
            i += 1
        
        if i < k:
            return head
        
        prev.next = None
        new_head, tail = self.__reverse_list(head)
        tail.next = self.reverseKGroup(k_th_node, k)

        return new_head
        
    def __reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode, ListNode]:
        new_head = None
        tail = head
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = new_head
            new_head = curr
            curr = next_node
            
        return new_head, tail
            