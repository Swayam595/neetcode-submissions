class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # return self.__maxTurbulenceSizeBruteForce(arr) # Accepted
        return self.__maxTurbulenceSizeOptimized(arr) # Accpeted
    
    # TC - O(n^2) SC - O(1)
    def __maxTurbulenceSizeBruteForce(self, arr):
        longest_turbulent_subarray = 1

        for i in range(len(arr) - 1):
            curr_turbulent_subarray_reverse_checked = 1
            curr_turbulent_subarray_not_reverse_checked = 1
            for j in range(i, len(arr) - 1):
                if self.__is_turbulent(arr[j], arr[j + 1], j, False):
                    curr_turbulent_subarray_not_reverse_checked += 1
                else:
                    curr_turbulent_subarray_not_reverse_checked = 1
                
                if self.__is_turbulent(arr[j], arr[j + 1], j, True):
                    curr_turbulent_subarray_reverse_checked += 1
                else:
                    curr_turbulent_subarray_reverse_checked = 1

                longest_turbulent_subarray = max(
                                                longest_turbulent_subarray, 
                                                curr_turbulent_subarray_reverse_checked,
                                                curr_turbulent_subarray_not_reverse_checked)
        
        return longest_turbulent_subarray

    # TC - O(n) SC - O(1)
    def __maxTurbulenceSizeOptimized(self, arr: List[int]) -> int:
        return max(self.__maxTurbulenceSizeWithCheck(arr, True), 
                   self.__maxTurbulenceSizeWithCheck(arr, False))
        
    
    def __maxTurbulenceSizeWithCheck(self, arr: List[int], check_for_reverse: bool) -> int:
        longest_turbulent_subarray = 1
        curr_turbulent_subarray = 1

        for k in range(len(arr) - 1):
            if not self.__is_turbulent(arr[k], arr[k + 1], k, check_for_reverse):
                curr_turbulent_subarray = 0

            curr_turbulent_subarray += 1
            longest_turbulent_subarray = max(longest_turbulent_subarray, 
                                            curr_turbulent_subarray)

        return longest_turbulent_subarray

    def __is_turbulent(self, num1: int, num2: int, k: int, check_for_reverse: bool) -> bool:
        if check_for_reverse:
            if k % 2 != 0:
                return num1 > num2
            else:
                return num1 < num2
        else:
            if k % 2 != 0:
                return num1 < num2
            else:
                return num1 > num2