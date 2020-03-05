class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        dp = [[0]*n for i in range(m)]
        dp[m-2][n-1],dp[m-1][n-2] = 1,1
        
        def helper(i,j):
            if dp[i][j] != 0:
                return dp[i][j]
            if i == m-1:
                dp[i][j] = helper(i,j+1)
            elif j == n-1:
                dp[i][j] = helper(i+1,j)
            else:
                dp[i][j] = helper(i+1,j) + helper(i,j+1)
            return dp[i][j]
        
        return helper(0,0)