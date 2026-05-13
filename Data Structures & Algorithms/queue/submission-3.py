class ListNode:
    def __init__(self, val = -1, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.__head = ListNode(val = -1)
        self.__tail = ListNode(val = -1)
        self.__head.next = self.__tail
        self.__tail.prev =self.__head

    def isEmpty(self) -> bool:
        return self.__head.next == self.__tail
        
    def append(self, value: int) -> None:
        newNode = ListNode(val = value)
        lastNode = self.__tail.prev

        lastNode.next = newNode
        newNode.prev = lastNode
        newNode.next = self.__tail
        self.__tail.prev = newNode

    def appendleft(self, value: int) -> None:
        newNode = ListNode(val = value)
        frontNode = self.__head.next

        frontNode.prev = newNode
        newNode.next = frontNode
        newNode.prev = self.__head
        self.__head.next = newNode     
        
    def pop(self) -> int:
        if self.isEmpty():
            return -1

        lastNode = self.__tail.prev
        prevNode = lastNode.prev
        prevNode.next = self.__tail
        self.__tail.prev = prevNode
        return lastNode.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        frontNode = self.__head.next
        nextNode = frontNode.next
        self.__head.next = nextNode
        nextNode.prev = self.__head
        return frontNode.val 
