class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums_dict = dict()

        for num in nums:
            if not nums_dict.get(num, 0):
                nums_dict[num] = nums_dict.get(num - 1, 0) + nums_dict.get(num + 1, 0) + 1
                nums_dict[num - nums_dict.get(num - 1, 0)] = nums_dict[num]
                nums_dict[num + nums_dict.get(num + 1, 0)] = nums_dict[num]
                max_length = max(max_length, nums_dict[num])
            
        return max_length

