class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1+word2
        ans = 0
        n1,n2,n = len(word1),len(word2),len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                    if i < n1 and j >= n1:
                        ans = max(ans,dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return ans