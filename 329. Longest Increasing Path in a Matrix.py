class Solution:
    def longestIncreasingPath(self, A: List[List[int]]) -> int:
        m = len(A)
        if A == []:
            return 0
        n = len(A[0])
        v = [[-1]*n for i in range(m)]
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def dfs(i,j):
            if v[i][j] >= 0:
                return v[i][j]
            tem = 0
            for a,b in d:
                x,y = i+a, j+b
                if 0<=x<m and 0<=y<n and A[x][y] > A[i][j]:
                    tem = max(tem,dfs(x,y))
                    
            v[i][j] = tem+1
            return v[i][j]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                v[i][j] = dfs(i,j)
                ans = max(ans,v[i][j])
        return ans