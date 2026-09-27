# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # TC -> O(N + M)
    # SC -> O(max(N, M))
    # N -> len of l1
    # M -> len of l2
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 is not None and l2 is not None:
            num1 = l1.val
            num2 = l2.val
            num = num1 + num2 + carry
            digit = num % 10
            carry = num // 10

            node = ListNode(digit)
            tail.next = node
            tail = tail.next
            l1 = l1.next
            l2 = l2.next

        tail, carry = self.__add_remaining(l1, tail, carry)
        tail, carry = self.__add_remaining(l2, tail, carry)

        if carry:
            tail.next = ListNode(1)
        
        return dummy.next        
    
    def __add_remaining(self, l: Optional[ListNode], tail: Optional[ListNode], carry: int) -> None:
        while l is not None:
            num = l.val + carry
            digit = num % 10
            carry = num // 10

            node = ListNode(digit)

            tail.next = node
            tail = tail.next
            l = l.next
        
        return tail, carry