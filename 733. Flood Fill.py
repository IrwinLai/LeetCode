class Solution:
    def floodFill(self, A: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n,m = len(A),len(A[0])
        color = A[sr][sc]
        
        def dfs(r,c):
            if 0 <= r < n and 0<= c < m and A[r][c] == color:
                A[r][c] = newColor
                [dfs(r+x,c+y) for x,y in [(0,1),(1,0),(0,-1),(-1,0)]]
            else:
                return 
        
        if color != newColor:
            dfs(sr,sc)
        
        return A
                    