class Solution:
    def solve(self, A: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(A) <= 1:
            return A
        m = len(A)
        n = len(A[0])
        
        def dfs(i,j):
            if 0<=i<=m-1 and 0<=j<=n-1:
                if A[i][j] == 'O':
                    A[i][j] = 'B'
                    dfs(i-1,j)
                    dfs(i+1,j)
                    dfs(i,j+1)
                    dfs(i,j-1)
        
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                if A[i][j] == 'O':
                    A[i][j] = 'X'
                elif A[i][j] == 'B':
                    A[i][j] = 'O'