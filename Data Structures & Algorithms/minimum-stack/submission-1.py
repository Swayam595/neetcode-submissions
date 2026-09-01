class MinStack:

    def __init__(self):
        self.__stack = []
        

    def push(self, val: int) -> None:
        new_top = [val, val]
        if len(self.__stack) > 0 and self.__stack[-1][1] < new_top[1]:
            new_top[1] = self.__stack[-1][1]
        self.__stack.append(new_top)
        

    def pop(self) -> None:
        self.__stack.pop()
        

    def top(self) -> int:
        return self.__stack[-1][0]
        

    def getMin(self) -> int:
        return self.__stack[-1][1]
        
