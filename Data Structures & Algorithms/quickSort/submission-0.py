# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.__quickSort(pairs, 0, len(pairs) - 1)

    def __quickSort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i].key < pivot.key:
                self.__swap(arr, left, i)
                left += 1
        
        self.__swap(arr, left, e)

        self.__quickSort(arr, s, left - 1)
        self.__quickSort(arr, left + 1, e)

        return arr
        
    
    def __swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
