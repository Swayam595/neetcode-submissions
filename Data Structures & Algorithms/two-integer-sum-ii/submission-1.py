class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.__twoSumBruteForce(numbers, target)
    
    # TC - O(n^2) SC - O(n)
    def __twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i + 1, j + 1]