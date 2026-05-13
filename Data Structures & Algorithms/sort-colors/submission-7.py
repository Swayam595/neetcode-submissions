class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        i = 0
        r = len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                self._swap(nums, l, i)
                l += 1
                i += 1
            elif nums[i] == 2:
                self._swap(nums, i, r)
                r -= 1
            else:
                i += 1
    
    def _swap(self, nums, p1, p2):
        temp = nums[p1]
        nums[p1] = nums[p2]
        nums[p2] = temp
