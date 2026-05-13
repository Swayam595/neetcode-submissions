class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__size = 0
        self.__map = [None] * self.__capacity


    def insert(self, key: int, value: int) -> None:
        index = self.__hash(key)

        while True:
            if self.__map[index] == None:
                self.__map[index] = Pair(key, value)
                self.__size += 1

                if self.__size >= self.__capacity // 2:
                    self.resize()
                return
            elif self.__map[index].key == key:
                self.__map[index].value = value
            index += 1
            index = index % self.__capacity



    def get(self, key: int) -> int:
        index = self.__getPairIndex(key)
        value = -1

        if index != -1:
            value = self.__map[index].value

        return value



    def remove(self, key: int) -> bool:
        index = self.__getPairIndex(key)

        is_removed = False
        if index != -1:
            is_removed = True
            self.__map[index] = None
            self.__size -= 1
        
        return is_removed


    def getSize(self) -> int:
        return self.__size


    def getCapacity(self) -> int:
        return self.__capacity


    def resize(self) -> None:
        self.__capacity = 2 * self.__capacity
        new_map = [None] * self.__capacity

        old_map = self.__map
        self.__map = new_map
        self.__size = 0

        for pair in old_map:
            if pair is not None:
                self.insert(pair.key, pair.value)

    def __hash(self, key):
        return key % self.__capacity

    def __getPairIndex(self, key):
        index = self.__hash(key)

        while self.__map[index] != None:
            if self.__map[index].key == key:
                return index
            index += 1
        
        return -1
