class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2

            if not self.__can_finish_in_curr_rate(piles, mid, h):
                low = mid + 1
            else:
                high = mid - 1
        
        return low
    
    def __can_finish_in_curr_rate(self, piles: List[int], rate: int, h: int):
        for pile in piles:
            hours_required_to_complete_ith_pile = self.__calculate_hours_required(rate, pile)
            
            if hours_required_to_complete_ith_pile > h:
                return False

            h -= hours_required_to_complete_ith_pile
        
        return h >= 0
    
    def __calculate_hours_required(self, rate: int, pile: int) -> int:
        hours_needed_at_curr_rate = pile // rate
        r = pile % rate

        if r > 0:
            hours_needed_at_curr_rate += 1
        
        return hours_needed_at_curr_rate