class DynamicArray:
    
    def __init__(self, capacity: int):
        self.__array = [0] * capacity
        self.__lastIndex = 0
        self.__tail = 0

    def get(self, i: int) -> int:
        return self.__array[i]

    def set(self, i: int, n: int) -> None:
        self.__array[i] = n

    def pushback(self, n: int) -> None:
        if self.__tail == len(self.__array):
            self.resize()
        self.__array[self.__tail] = n
        self.__tail += 1

    def popback(self) -> int:
        self.__tail -= 1
        top = self.__array[self.__tail]
        return top

    def resize(self) -> None:
        currArrayLen = len(self.__array)
        newArrayLen = currArrayLen * 2
        newArray = [0] * newArrayLen

        for i in range(currArrayLen):
            newArray[i] = self.__array[i]
        
        self.__array = newArray

    def getSize(self) -> int:
        return self.__tail
    
    def getCapacity(self) -> int:
        return len(self.__array)
