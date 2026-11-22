class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.__sum_of_digits(n)

        while slow != fast:
            fast = self.__sum_of_digits(fast)
            fast = self.__sum_of_digits(fast)
            slow = self.__sum_of_digits(slow)
        
        return True if fast == 1 else False
        
    def __sum_of_digits(self, n: int) -> int:
        total = 0

        while n > 0:
            digit = n % 10
            total += digit ** 2
            n = n // 10
        
        return total