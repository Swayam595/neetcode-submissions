class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_seen_at = dict()

        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in num_seen_at:
                return [num_seen_at[num2], i]
            num_seen_at[num1] = i
