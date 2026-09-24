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
        
        while l <= h:
            mid = l + (h - l) // 2
            curr_timestamp = search_space[mid][0]

            if curr_timestamp <= timestamp:
                l = mid + 1
            else:
                h = mid - 1
        
        if search_space[l - 1][0] <= timestamp:
            return search_space[l - 1][1]
        return ""

