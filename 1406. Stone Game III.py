class Solution:
    def stoneGameIII(self, sv: List[int]) -> str:
        n = len(sv)
        
        d = {}
        def dp(i):
            if d.get(i,'a') != 'a':
                return d[i]
            elif i >= n:
                d[i] = 0
            elif i == n-1:
                d[i] = sv[-1]
            elif i == n-2:
                d[i] = max(sv[i]-dp(i+1),sv[i]+sv[i+1]-dp(i+2))
            else:
                d[i] = max(sv[i]-dp(i+1),sv[i]+sv[i+1]-dp(i+2),sv[i]+sv[i+1]+sv[i+2]-dp(i+3))
            return d[i]
        ans = dp(0) 
        ans = d[0]
        if ans > 0:
            return "Alice"
        if ans == 0:
            return "Tie"
        else:
            return "Bob"