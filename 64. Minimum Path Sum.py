class Solution:
    def minPathSum(self, g: List[List[int]]) -> int:
        m = len(g)
        n = len(g[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j != 0:
                    g[i][j] += g[i][j-1]
                if i != 0 and j == 0:
                    g[i][j] += g[i-1][j]
                if i != 0 and j != 0:
                    g[i][j] += min(g[i-1][j],g[i][j-1])
        return g[-1][-1]