class Solution:
    """
    TC - O(n * 2 ^ n)
    SC - O(h) ~ O(n)
    h - height of the decision tree which is equal to n
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        acc = []

        self.__backTrack(0, nums, subsets, acc)

        return subsets
    
    def __backTrack(self, i: int, nums: List[int], subsets: List[List[int]], acc: List[int]) -> None:
        if i == len(nums):
            subsets.append(acc.copy())
            return
        
        acc.append(nums[i])
        self.__backTrack(i + 1, nums, subsets, acc)

        acc.pop()
        self.__backTrack(i + 1, nums, subsets, acc)