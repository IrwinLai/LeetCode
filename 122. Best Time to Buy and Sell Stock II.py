class Solution:
    def maxProfit(self, P: List[int]) -> int:
        n = len(P)
        if n <= 1:
            return 0
        
        prmn = P[0]
        ans = 0
        for i in range(1,n):
            if P[i] > P[i-1]:
                ans += P[i] - prmn
                prmn = P[i]
            else:
                prmn = min(prmn,P[i])
        return ans