from functools import lru_cache
class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        n = len(A)
        if d >= n:
            return sum(A) if d == n else -1
        
        @lru_cache(maxsize=None)
        def helper(days,end): # from the last one to the first one
            if days == 1:
                return max(A[:end])
            
            res, mx = math.inf, 0
            for done in range(1,end-days+2): # do done jobs
                mx = max(mx,A[end-done])
                res = min(helper(days-1,end-done)+mx,res)  
            return res
            
        return helper(d,n)