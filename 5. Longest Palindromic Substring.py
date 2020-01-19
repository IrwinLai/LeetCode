class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for i in range(len(s))]
        ans = ""
        max_length = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                # if start and end item is same and between them is Palindromic
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if ans == "" or max_length < j - i + 1:
                        ans = s[i:j+1]
                        max_length = j - i + 1
        return ans

        '''
        if len(s) == 0:
            return ""
        count = 0
        ret = s[0]
        n = len(s)
        for i in range(n):
            for j in range(1,n+1):
                if s[i] == s[j-1]:
                    if s[i:j] == s[i:j][::-1]:
                        if j-i > count:
                            count = j-i
                            ret = s[i:j]
        return ret
        '''