class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = dict()

        for i, num1 in enumerate(nums):
            num2 = target - num1

            if num2 in num_map:
                return [num_map[num2], i]
            
            num_map[num1] = i
        