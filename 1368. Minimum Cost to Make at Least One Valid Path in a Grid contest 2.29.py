class Solution:
    def minCost(self, g: List[List[int]]) -> int:
        m,n,inf,s = len(g),len(g[0]),10000,0
        dp = [[inf] * n for i in range(m)]
        bfs = []
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(i,j):
            if not (0<=i<m and 0<=j<n and dp[i][j] == inf):
                return 0
            dp[i][j] = s
            bfs.append([i,j])
            return dfs(i+d[g[i][j]-1][0],j+d[g[i][j]-1][1])
        
        dfs(0,0)
        while bfs:
            bfs,bfs2 = [],bfs
            s += 1
            for x,y in bfs2:
                for i,j in d:
                    dfs(x+i,y+j)
            bfs2 = bfs
        print(dp)
        return dp[-1][-1]
            