class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[1]*n for _ in range(n)]
        
        for j in range(1,n):
            for i in range(0,j)[::-1]:
                if s[i] == s[j]:
                    if i+1 <= j-1:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    else:
                        dp[i][j] = 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])

        return dp[0][n-1]