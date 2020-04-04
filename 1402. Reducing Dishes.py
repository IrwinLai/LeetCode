class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        s.sort(reverse = True)
        ans = 0
        for i in range(len(s)):
            tem = 0
            for j in range(i+1):
                tem += s[i-j]*(j+1)
            ans = max(ans,tem)
        return ans