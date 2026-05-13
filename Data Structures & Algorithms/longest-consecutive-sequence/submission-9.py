class Solution:
    # TC - O(n) SC - O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_dict = dict()

        for num in nums:
            if num not in nums_dict:
                previous_number_rank = nums_dict.get(num - 1, 0)
                next_number_rank = nums_dict.get(num + 1, 0)

                nums_dict[num] = previous_number_rank + next_number_rank + 1
                nums_dict[num - previous_number_rank] = nums_dict[num]
                nums_dict[num + next_number_rank] = nums_dict[num]

                max_len = max(max_len, nums_dict[num])
        
        return max_len