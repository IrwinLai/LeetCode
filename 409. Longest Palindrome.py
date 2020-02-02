class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = collections.Counter(s)
        ans = 0
        tem = 0
        print(d)
        for i in list(d.keys()):
            if d[i] % 2 == 0:
                ans += d[i]
            else:
                ans += d[i] - 1
                tem = 1
        return ans + tem