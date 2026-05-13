class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()

        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in nums_dict:
                j = nums_dict[num2]
                return [j, i]
            nums_dict[num1] = i
        