# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.__mergeSort(pairs, 0, len(pairs) - 1)

    def __mergeSort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        mid = s + (e - s) // 2
        self.__mergeSort(arr, s, mid)
        self.__mergeSort(arr, mid + 1, e)

        self.__merge(arr, s, mid, e)
        return arr
    
    def __merge(self, arr, s, mid, e):
        l1 = arr[s : mid + 1]
        l2 = arr[mid + 1 : e + 1]

        i = 0
        j = 0
        k = s

        while i < len(l1) and j < len(l2):
            if l1[i].key <= l2[j].key:
                arr[k] = l1[i]
                i += 1
            else:
                arr[k] = l2[j]
                j += 1
            k += 1
        
        while i < len(l1):
            arr[k] = l1[i]
            i += 1
            k += 1
        
        while j < len(l2):
            arr[k] = l2[j]
            j += 1
            k += 1
            