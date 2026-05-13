class MyStack:

    def __init__(self):
        self.__queue = deque()

    def push(self, x: int) -> None:
        self.__queue.append(x)

    def pop(self) -> int:
        self.__queue.append(None)

        while self.__queue[1] != None:
            front = self.__queue.popleft()
            self.__queue.append(front)
        
        
        top = self.__queue.popleft()
        self.__queue.popleft()

        return top

    def top(self) -> int:
        front = self.pop()
        self.__queue.append(front)
        return front

    def empty(self) -> bool:
        return len(self.__queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()