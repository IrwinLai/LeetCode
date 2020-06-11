class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        inf = float('inf')
        @lru_cache(None)
        def dp(i, nei, color):
            if houses[i] != 0 and houses[i] != color:
                return inf
            
            if i == 0:
                if nei != 1:
                    return inf
                else:
                    return cost[0][color-1] if houses[0] == 0 else 0
            
            # could print
            tem = inf
            for c in range(1,n+1):
                # same color with previous one
                if c == color:
                    tem = min(tem, dp(i-1, nei, c) + cost[i][color-1])
                else:
                    tem = min(tem, dp(i-1, nei-1, c) + cost[i][color-1])
                    
            return tem if houses[i] == 0 else tem - cost[i][color-1]
        
        ans = inf
        for c in range(1,n+1):
            ans =  min(ans, dp(m-1,target,c))
                
        if ans == float('inf'):
            return -1
        return ans