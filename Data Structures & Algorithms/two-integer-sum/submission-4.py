class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()

        for i, num1 in enumerate(nums):
            num2 = target - num1

            if num2 in num_dict:
                j = num_dict[num2]
                return [j, i]
            
            num_dict[num1] = i
        
        