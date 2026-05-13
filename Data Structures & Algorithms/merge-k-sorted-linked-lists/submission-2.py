# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # return self.__mergeKListsUsingMergeSort(lists)
        return self.__mergeKListsIteratively(lists)

    def __mergeKListsIteratively(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        
        if n == 0:
            return None

        block_size = 1

        while block_size < n:
            for start in range(0, n, block_size * 2):
                mid = start + block_size
                end = min(start + block_size * 2, n)

                if mid < end:
                    l1 = lists[start]
                    l2 = lists[mid]
                    lists[start] = self.__merge(l1, l2)
            block_size *= 2

        return lists[0]



    def __mergeKListsUsingMergeSort(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        if n == 0:
            return None

        self.__mergeSort(lists, 0, n - 1)
        return lists[0]
    
    def __mergeSort(self, lists, s, e):
        if e - s + 1 <= 1:
            return lists
        
        mid = s + (e - s) // 2
        self.__mergeSort(lists, s, mid)
        self.__mergeSort(lists, mid + 1, e)

        sorted_list = self.__merge(lists[s], lists[mid + 1])
        lists[s] = sorted_list

        return lists

    def __merge(self, l1, l2):        
        dummy_head = ListNode()
        tail = dummy_head

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
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