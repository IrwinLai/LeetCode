class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0
    
        '''
        def dfs(i,j,m,n,d):
            if grid[i][j] == 1:
                grid[i][j] = 0
                if 0<=i+1<=m and 0<=j<=n:d = dfs(i+1,j,m,n,d)
                if 0<=i<=m and 0<=j+1<=n:d = dfs(i,j+1,m,n,d)
                if 0<=i-1<=m and 0<=j<=n:d = dfs(i-1,j,m,n,d)
                if 0<=i<=m and 0<=j-1<=n:d = dfs(i,j-1,m,n,d)
                return d+1
            return d
            
        m = len(grid) # i
        n = len(grid[0]) # j
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans,dfs(i,j,m-1,n-1,0))
        
        return ans
        '''