class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        l = 0
        r = len(numbers) - 1

        while l < r:
            twoSum = numbers[l] + numbers[r]
            if twoSum < target:
                l += 1
                while numbers[l] == numbers[l - 1] and l < r:
                    l += 1
            elif twoSum > target:
                r -= 1
                while numbers[r] == numbers[r + 1] and l < r:
                    r -= 1
            else:
                break
        return [l + 1, r + 1]
        