class Solution:
    def countHomogenous(self, s: str) -> int:
        k = 1
        ans = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                k += 1
            else:
                ans += k*(k+1)/2
                k = 1
        ans += k*(k+1)//2
        return int(ans) % (10**9+7)