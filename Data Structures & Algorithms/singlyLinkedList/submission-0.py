class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.__head = ListNode(-1)
        self.__tail = self.__head
    
    def get(self, index: int) -> int:
        curr = self.__head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.__head.next
        self.__head.next = newNode
        if newNode.next is None:
            self.__tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.__tail.next = newNode
        self.__tail = newNode

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.__head
        while i < index and curr is not None:
            i += 1
            curr = curr.next

        if curr is not None and curr.next is not None:
            if curr.next == self.__tail:
                self.__tail = curr
            curr.next = curr.next.next 
            return True
        return False

    def getValues(self) -> List[int]:
        vals = []
        curr = self.__head.next
        while curr is not None:
            val = curr.val
            vals.append(val)
            curr = curr.next
        return vals      