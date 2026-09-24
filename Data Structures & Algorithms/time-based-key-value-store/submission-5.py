class TimeMap:
    # SC -> O(N * M)
    # N -> # of keys 
    # M -> max len of the value array
    def __init__(self):
        self.__map = dict()
        
    # TC -> O(1)
    # SC -> O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.__map:
            self.__map[key] = []
            
        self.__map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.__map:
            return ""
        
        return self.__binary_search(self.__map[key], timestamp)
    
    # TC -> O(log(M))
    # SC -> O(1)
    # M -> max len of the value array
    def __binary_search(self, values_array: List[List[int, str]], timestamp: int) -> str:
        n = len(values_array)
        l = 0
        h = n - 1
        
        while l <= h:
            mid = l + (h - l) // 2
            curr_timestamp = values_array[mid][0]

            if curr_timestamp <= timestamp:
                l = mid + 1
            else:
                h = mid - 1
        
        if values_array[l - 1][0] <= timestamp:
            return values_array[l - 1][1]
        return ""

