class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        for line in grid:
            line.insert(0,0)
            line.append(0)
        
        @lru_cache(None)
        def dp(i,j1,j2):
            j1,j2 = min(j1,j2),max(j1,j2)
            if i == len(grid)-1 or j1 == 0 or j2 == len(grid[0])-1:
                return 0
            a = []
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if j1+x != j2+y:
                        a.append(dp(i+1,j1+x,j2+y)+grid[i+1][j1+x]+grid[i+1][j2+y])
                    else:
                        a.append(dp(i+1,j1+x,j2+y)+grid[i+1][j1+x])
            
            return max(a)
        
        return grid[0][1]+grid[0][len(grid[0])-2]+dp(0,1,len(grid[0])-2)
                
            