# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.__reverse_k_group_recursive(head, k)
        # return self.__reverse_k_group_iterative(head, k)

    # TC -> O(N + k)
    # SC -> O(1)
    # N -> # of nodes in the linked list
    def __reverse_k_group_iterative(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = ListNode()
        tail = dummy

        while head is not None:
            i, next_kth_node, prev_node = self.__get_kth(head, k)
            
            if i < k:
                break
            
            prev_node.next = None
            new_head, new_tail = self.__reverse_list(head)
            tail.next = new_head
            new_tail.next = next_kth_node
            tail = new_tail
            head = next_kth_node

        return dummy.next

    # TC -> O(N + k)
    # SC -> O(N / k)
    # N -> # of nodes in the linked list
    def __reverse_k_group_recursive(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
    
        i, next_kth_node, prev_node = self.__get_kth(head, k)
        
        if i < k:
            return head
        
        prev_node.next = None
        new_head, tail = self.__reverse_list(head)
        tail.next = self.reverseKGroup(next_kth_node, k)

        return new_head

    def __get_kth(self, head: Optional[ListNode], k: int) -> (int, Optional[ListNode], Optional[ListNode]):
        i = 0
        prev = None
        while i < k and head is not None:
            prev = head
            head = head.next
            i += 1

        return i, head, prev
        
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
            