class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        d = [0]
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                d.append(i)
        d.append(len(s))
        for i in range(1,len(d)):
            if d[i] - d[i-1] > 1:
                ans += sum(cost[d[i-1]:d[i]]) - max(cost[d[i-1]:d[i]])

        return ans
                
                