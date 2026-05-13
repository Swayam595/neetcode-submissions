class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = -1
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                i = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return i