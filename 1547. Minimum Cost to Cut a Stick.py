class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        INF = 100000000
        cuts.sort()
        
        
        @lru_cache(None)
        def dp(i,j,a,b):
            if a == b:
                return 0
            
            else:
                m = INF
                for k in range(a,b):
                    m = min(m, dp(i,cuts[k],a,k) + dp(cuts[k],j,k+1,b) + j-i)
   
                return m
            
        return dp(0,n,0,len(cuts))