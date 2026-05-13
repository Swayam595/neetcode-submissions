class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums) - 1

        while j <= k:
            if nums[j] == 0:
                self.__swap(nums, i, j)
                i += 1
                j += 1
            elif nums[j] == 2:
                self.__swap(nums, j, k)
                k -= 1
            else:
                j += 1
    
    def __swap(self, nums, p1, p2):
        temp = nums[p1]
        nums[p1] = nums[p2]
        nums[p2] = temp

            