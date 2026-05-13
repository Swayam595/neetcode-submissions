class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        return self.__numOfSubarraysBruteForce(arr, k, threshold)
    
    def __numOfSubarraysBruteForce(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        ans = 0

        for i in range(n - k + 1):
            curr_sum = 0
            for j in range(i, min(i + k, n)):
                curr_sum += arr[j]
            
            if curr_sum / k >= threshold:
                ans += 1
            
        return ans