class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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
                num2 = nums[l]
                num3 = nums[r]

                three_sum = num1 + num2 + num3

                if three_sum == 0:
                    ans.append([num1, num2, num3])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1
        
        return ans
