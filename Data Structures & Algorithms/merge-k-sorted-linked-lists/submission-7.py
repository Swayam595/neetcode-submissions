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
        
        return self.__mergeSort(lists, 0, n - 1)
    
    # TC -> O(N)
    # SC -> O(1)
    # N -> # of nodes
    def __mergeSort(self, lists: List[Optional[ListNode]], start: int, end: int) -> None:
        if start > end:
            return None
        
        if start == end:
            return lists[start]
        
        mid = start + (end - start) // 2
        l1 = self.__mergeSort(lists, start, mid)
        l2 = self.__mergeSort(lists, mid + 1, end)

        lists[start] = self.__mergeLists(l1, l2)

        return lists[start]

    
    # TC - O(A + B)
    # SC - O(1)
    # A -> len of l1
    # B -> len of l2
    def __mergeLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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