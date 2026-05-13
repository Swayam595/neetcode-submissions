class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return self.__twoSumBruteForce(numbers, target) # Accepted
        return self.__twoSumTwoPointer(numbers, target) # Accepted
    
    # TC - O(n^2) SC - O(n)
    def __twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i + 1, j + 1]

    # TC - O(n) SC - O(1)
    def __twoSumTwoPointer(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            curr_sum = nums[l] + nums[r]

            if curr_sum == target:
                return [l + 1, r + 1]
            elif curr_sum < target:
                l += 1
                while nums[l - 1] == nums[l] and l < r:
                    l += 1
            else:
                r -= 1
                while nums[r] == nums[r - 1] and l < r:
                    r -= 1