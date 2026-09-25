class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.__find_median_sorted_arrays_brute_force(nums1, nums2)

    # TC -> O(N + M)
    # SC -> O(N + M)
    # N -> len of nums1
    # M -> len of nums2
    def __find_median_sorted_arrays_brute_force(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        self.__add_remaining(nums1, i, nums)
        self.__add_remaining(nums2, j, nums)

        if len(nums) % 2 == 1:
            return nums[len(nums) // 2]
        else:
            n1 = nums[len(nums) // 2]
            n2 = nums[len(nums) // 2 - 1]
            return (n1 + n2) / 2
    
    def __add_remaining(self, nums: List[int], i: int, result: List[int]) -> None:
        while i < len(nums):
            result.append(nums[i])
            i += 1
