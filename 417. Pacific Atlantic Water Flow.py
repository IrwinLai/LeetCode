# from lower to higher, from edges to center

class Solution:
    def pacificAtlantic(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) == 0:
            return []
        m = len(A)
        n = len(A[0])
        pv = [[0]*n for i in range(m)]
        av = [[0]*n for i in range(m)]
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        
        def helper(i,j,v):
            v[i][j] = 1
            for x,y in direction:
                x +=i
                y +=j
                if x==-1 or x==m or y==-1 or y==n:
                    v[i][j] = 1
                elif A[i][j] <= A[x][y] and v[x][y] != 1:
                    helper(x,y,v)
            
        for i in range(m):
            helper(i,0,pv)
            helper(i,n-1,av)
        
        for j in range(n):
            helper(0,j,pv)
            helper(m-1,j,av)

        res = []
        for i in range(m):
            for j in range(n):
                if pv[i][j] and av[i][j]:
                    res.extend([[i,j]])
                    
        return res
            