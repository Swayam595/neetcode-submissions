# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
            
        return self.__merge_sort(lists, 0, len(lists) - 1)
    
    def __merge_sort(self, lists: List[Optional[ListNode]], l: int, r: int) -> Optional[ListNode]:
        if l >= r:
            return lists[l]
        
        mid = l + (r - l) // 2

        left_list = self.__merge_sort(lists, l, mid)
        right_list = self.__merge_sort(lists, mid + 1, r)

        return self.__merge(left_list, right_list)
    
    def __merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

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
        
        return dummy.next