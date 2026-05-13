class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2

            if not self.__canFinishInCurrRate(piles, mid, h):
                low = mid + 1
            else:
                high = mid - 1
        
        return low
    
    def __canFinishInCurrRate(self, piles, rate, h):
        for pile in piles:
            hours_needed_at_curr_rate = self.__hoursNeeded(rate, pile)
            if hours_needed_at_curr_rate > h:
                return False
            h -= hours_needed_at_curr_rate
        return h >= 0
    
    def __hoursNeeded(self, rate, pile):
        hours_needed_at_curr_rate = pile // rate
        r = pile % rate

        if r > 0:
            hours_needed_at_curr_rate += 1
        
        return hours_needed_at_curr_rate
        