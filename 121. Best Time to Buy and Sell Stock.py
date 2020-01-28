class Solution:
    def maxProfit(self, P: List[int]) -> int:
        n = len(P)
        if n <= 1:
            return 0
        mn = P[0]
        ans = 0
        for i in range(1,n):
            mn = min(mn,P[i])
            ans = max(ans,P[i] - mn)
        return ans
        