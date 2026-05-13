class MinStackNode:
    val = None
    min_val_seen = None
    
    def __init__(self, val, min_val_seen):
        self.val = val
        self.min_val_seen = min(val, min_val_seen)

class MinStack:
    __stack = None
    def __init__(self):
        self.__stack = []

    def push(self, val: int) -> None:
        if len(self.__stack) == 0:
            min_val_seen = val
        else:
            min_val_seen = self.__stack[-1].min_val_seen
        min_stack_node = MinStackNode(val, min_val_seen)
        self.__stack.append(min_stack_node)
        

    def pop(self) -> None:
        self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1].val

    def getMin(self) -> int:
        return self.__stack[-1].min_val_seen
