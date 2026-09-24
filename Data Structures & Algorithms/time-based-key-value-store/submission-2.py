class TimeMap:

    def __init__(self):
        self.__map = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.__map[key] = self.__map.get(key, [])
        self.__map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.__map:
            return ""
        
        return self.__binary_search(self.__map[key], timestamp)
    
    def __binary_search(self, search_space: List[List[int, str]], timestamp: int) -> str:
        n = len(search_space)
        l = 0
        h = n - 1
        value = ""

        while l <= h:
            mid = l + (h - l) // 2
            curr_timestamp, curr_val = search_space[mid]

            if curr_timestamp <= timestamp:
                value = curr_val
                l = mid + 1
            else:
                h = mid - 1
        
        return value