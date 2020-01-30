class Solution:
    def trailingZeroes(self, n: int) -> int:
        def helper(n):
            return 0 if n == 0 else n//5 + helper(n//5)
        
        return helper(n)