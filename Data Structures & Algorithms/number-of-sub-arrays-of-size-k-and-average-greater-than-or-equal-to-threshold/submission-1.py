class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # return self.__numOfSubarraysBruteForce(arr, k, threshold) # Accepted
        return self.__numOfSubarraysOptimized(arr, k, threshold)
    
    # TC - O(n * k) SC - O(1)
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
    
    # TC - O(n) SC - O(1)
    def __numOfSubarraysOptimized(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0

        n = len(arr)
        running_sum = 0

        L = 0

        for R in range(n):
            running_sum += arr[R]

            if R - L + 1 > k:
                running_sum -= arr[L]
                L += 1
            
            if R - L + 1 == k and running_sum / k >= threshold:
                ans += 1
        
        return ans