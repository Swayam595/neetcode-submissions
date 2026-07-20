# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    # TC -> O(N * logK)
    # SC -> O(1)
    # K -> len lists
    # N -> # of nodes
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None

        block_size = 1

        while block_size < n:
            self.__mergeListByBlock_size(lists, block_size)
            block_size *= 2
        
        return lists[0]
    
    # TC -> O(N)
    # SC -> O(1)
    # N -> # of nodes
    def __mergeListByBlock_size(self, lists: List[Optional[ListNode]], block_size: int):
        for start in range(0, len(lists), 2 * block_size):
            mid = start + block_size
            end = min(start + block_size * 2, len(lists))

            if mid >= end:
                break

            l1 = lists[start]
            l2 = lists[mid]
                

            sorted_list = self.__mergeList(l1, l2)
            lists[start] = sorted_list
    
    # TC - O(A + B)
    # SC - O(1)
    # A -> len of l1
    # B -> len of l2
    def __mergeList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        tail = dummy_head

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1 is not None:
            tail.next = l1
        
        if l2 is not None:
            tail.next = l2
        
        return dummy_head.next