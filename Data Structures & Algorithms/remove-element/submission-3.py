class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                self.__swap(nums, i, k)
                k += 1
        
        return k
    
    def __swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]