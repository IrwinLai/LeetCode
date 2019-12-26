import numpy as np
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    count += 4
                    if row > 0 and grid[row-1][col] == 1: count -= 1
                    if col > 0 and grid[row][col-1] == 1: count -= 1
                    if row < m-1 and grid[row+1][col] == 1: count -= 1
                    if col < n-1 and grid[row][col+1] == 1: count -= 1
        return count
        
        '''
        def cal(grid,m,n):
            count = 0
            if grid[m-1][n] == 0:
                count += 1
            if grid[m+1][n] == 0:
                count += 1
            if grid[m][n+1] == 0:
                count += 1
            if grid[m][n-1] == 0:
                count += 1
            return count
        
        m = len(grid)
        n = len(grid[0])
        g = np.zeros((m+2, n+2), dtype=np.int)
        g[1:m+1,1:n+1] = grid
        
        count = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if g[i][j] == 1:
                    count += cal(g,i,j)
                       
                    
        return count
        '''