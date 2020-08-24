class Solution:
    def containsCycle(self, g: List[List[str]]) -> bool:
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        
        @lru_cache(None)
        def dfs(i,j,times):
            #print(i,j,times)
            ret = 0
            seen[i][j] = times
            for x,y in direction:
                if 0<=i+x<m and 0<=j+y<n and g[i][j] == g[i+x][j+y]:
                    if seen[i+x][j+y] != 0 and times - seen[i+x][j+y] >= 3:
                        return 1
                    elif seen[i+x][j+y] == 0:
                        ret += dfs(i+x, j+y, times+1)
            return ret
                    
                    
        m = len(g)
        n = len(g[0])
        seen = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if seen[i][j] == 0:
                    if dfs(i,j,1) == 1:
                        return True
        return False
                