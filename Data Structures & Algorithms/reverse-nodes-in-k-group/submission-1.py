# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.__reverse_k_group(head, k)

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
            