class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()
        freq_list = [[] for _ in range(len(nums) + 1)]
        ans = []

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
            
        for num in freq_dict:
            freq = freq_dict[num]
            freq_list[freq].append(num)

        i = len(nums)
    
        while i >= 0 and len(ans) < k:
            if len(freq_list[i]) > 0:
                ans += freq_list[i]
            i -= 1
        
        return ans


