class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack = []
        ans = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while len(monotonic_stack) > 0 and temperatures[monotonic_stack[-1]] < temperature:
                top = monotonic_stack.pop()
                ans[top] = i - top

            monotonic_stack.append(i)
        
        return ans