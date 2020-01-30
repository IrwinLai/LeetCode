class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            n /= 3
        return True if n == 1 or n == 1.0 else False