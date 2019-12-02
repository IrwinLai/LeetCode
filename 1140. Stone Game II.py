from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:      
        n = len(piles)
        
        @lru_cache(maxsize=None)
        def find(start,m):
            if start > n:
                return 0
            else:
                return max(sum(piles[start:start+x]) - find(start+x,max(x,m)) \
                           for x in range(1,2*m+1))
        
        return int((sum(piles)+find(0,1))/2)