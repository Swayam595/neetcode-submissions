class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.__productExceptSelfBruteForce(nums)

    # TC - O(n^2) SC - O(1)
    def __productExceptSelfBruteForce(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        running_prod = 1

        for i in range(n):
            curr_prod = 1
            for j in range(i + 1, n):
                curr_prod *= nums[j]
            ans.append(running_prod * curr_prod)
            running_prod *= nums[i]
        
        return ans