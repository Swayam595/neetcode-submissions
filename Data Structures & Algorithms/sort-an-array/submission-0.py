class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.__merge_sort(nums, 0, len(nums) - 1)
    
    def __merge_sort(self, nums, l, r):
        if l >= r:
            return [nums[l]]
        mid = l + (r - l) // 2
        left_sub_array = self.__merge_sort(nums, l, mid)
        right_sub_array = self.__merge_sort(nums, mid + 1, r)
        sorted_array = self.__merge(left_sub_array, right_sub_array)
        
        return sorted_array
    
    def __merge(self, left_array, right_array):
        sorted_array = []
        i = 0
        j = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                sorted_array.append(left_array[i])
                i += 1
            else:
                sorted_array.append(right_array[j])
                j += 1
        
        self.__add_remaining_elements(sorted_array, left_array, i)
        self.__add_remaining_elements(sorted_array, right_array, j)
        
        return sorted_array
    
    def __add_remaining_elements(self, sorted_array, array, k):
        while k < len(array):
            sorted_array.append(array[k])
            k += 1