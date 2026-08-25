class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return self.__three_sum_brute_force(nums)
        return self.__three_sum_2_pointer(nums)

    # TC -> O(N * log(N) + N ^ 2) ~ O(N ^ 2)
    # SC -> O(N) or O(1) based on the sorting algo used
    # N -> len of nums
    # M -> # of unique triplets
    def __three_sum_2_pointer(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        
        for i, num1 in enumerate(nums):
            if num1 > 0:
                break
            
            if i > 0 and num1 == nums[i - 1]:
                continue
            
            l = i + 1
            r = n - 1
            while l < r:
                three_sum = num1 + nums[l] + nums[r]
                if three_sum == 0:
                    ans.append([num1, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1

        return ans

    # TC -> O(N ^ 3)
    # SC -> O(M)
    # N -> len of nums
    # M -> # of unique triplets
    def __three_sum_brute_force(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        nums_list = sorted([nums[i], nums[j], nums[k]])
                        nums_tuple = tuple(nums_list)
                        if nums_tuple not in seen:
                            ans.append(nums_list)
                            seen.add(nums_tuple)
        
        return ans

        