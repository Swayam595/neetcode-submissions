class MinStack:

    def __init__(self):
        self.__stack = []
        self.__min_val = float('inf')
        

    def push(self, val: int) -> None:
        if not self.__stack:
            self.__stack.append(0)
            self.__min_val = val
        else:
            self.__stack.append(val - self.__min_val)
            if val < self.__min_val:
                self.__min_val = val
        

    def pop(self) -> None:
        if not self.__stack:
            return

        pop = self.__stack.pop()

        if pop < 0:
            self.__min_val = self.__min_val - pop
        

    def top(self) -> int:
        top = self.__stack[-1]
        if top > 0:
            return self.__min_val + top
        else:
            return self.__min_val
        

    def getMin(self) -> int:
        return self.__min_val
        
