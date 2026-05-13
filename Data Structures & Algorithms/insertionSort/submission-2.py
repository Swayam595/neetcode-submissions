# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
import copy

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return []
            
        ans = [pairs[:]]
        for i in range(1, len(pairs)):
            j = i - 1

            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                self.__swap(pairs, j, j + 1)
                j -= 1

            ans.append(pairs[:])
        return ans
    
    def __swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]