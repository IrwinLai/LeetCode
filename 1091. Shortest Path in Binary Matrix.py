class Solution:
    def shortestPathBinaryMatrix(self, m: List[List[int]]) -> int:
        n = len(m)
        if m[0][0] or m[n-1][n-1]:
            return -1
        p = [(0,0,1)]
        for x,y,d in p:
            if x == n-1 and y == n-1:
                return d
            for i,j in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
                if 0<=i<=n-1 and 0<=j<=n-1 and m[i][j] == 0:
                    m[i][j] = 1
                    p.append((i,j,d+1))
        return -1