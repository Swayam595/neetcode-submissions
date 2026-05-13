# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        tail = dummy_head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        self.__appendRestOfTheList(list1, tail)
        self.__appendRestOfTheList(list2, tail)
    
        return dummy_head.next

    def __appendRestOfTheList(self, list_head, tail):
        while list_head is not None:
            tail.next = list_head
            list_head = list_head.next
            tail = tail.next 