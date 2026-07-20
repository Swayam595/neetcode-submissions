# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    # TC -> O(L * K * min(M, N))
    # SC -> O(1)
    # L -> Square root of len of K
    # K -> len lists
    # N -> len of l1
    # M -> len of l2
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        i = 0
        max_iter = int(len(lists) ** 0.5)

        while i <= max_iter:
            self.__mergeListByInterval(lists, 2 ** i)
            i += 1
        
        return lists[0]
    
    # TC -> O(K * min(N, M))
    # SC -> O(1)
    # K -> len lists
    # N -> len of l1
    # M -> len of l2
    def __mergeListByInterval(self, lists: List[Optional[ListNode]], interval):
        for i in range(0, len(lists), 2 * interval):
            l1_index = i
            l1 = lists[l1_index]

            l2_index = i + interval if i + interval < len(lists) else -1
            if l2_index == -1:
                l2 = None
            else:
                l2 = lists[l2_index]

            sorted_list = self.__mergeList(l1, l2)
            lists[l1_index] = sorted_list
    
    # TC - O(min(N, M))
    # SC - O(1)
    # N -> len of l1
    # M -> len of l2
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