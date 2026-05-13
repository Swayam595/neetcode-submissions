class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementDict = dict()

        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in complementDict:
                j = complementDict[num2]
                return [j, i]
            complementDict[num1] = i