class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        count,ans = 0,0
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                ans += count*(count+1)//2
                count = 0
        ans += count*(count+1)//2
        return ans%mod