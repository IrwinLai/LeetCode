class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[n-1][i] = A[n-1][i]
        
        for i in range(n-2,-1,-1):
            for j in range(n):
                if j == 0:
                    dp[i][j] = A[i][j] + min(dp[i+1][j], dp[i+1][j+1])
                elif j == n-1:
                    dp[i][j] = A[i][j] + min(dp[i+1][j], dp[i+1][j-1])
                else:
                    dp[i][j] = A[i][j] + min(dp[i+1][j], dp[i+1][j+1], dp[i+1][j-1])
        
        return min(dp[0][i] for i in range(n))
        