class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return self.__two_sum_brute_force(numbers, target)
        return self.__two_sum_hash_map(numbers, target)
    
    # TC -> O(N)
    # SC -> O(N)
    # N -> len of numbers array
    def __two_sum_hash_map(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()

        for i, num2 in enumerate(nums):
            num1 = target - num2

            if num1 in num_dict:
                return [num_dict[num1] + 1, i + 1]
            
            num_dict[num2] = i
            

    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> len of numbers array
    def __two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i + 1, j + 1]