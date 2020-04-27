class Solution:
    def maximalSquare(self, A: List[List[str]]) -> int:
        n = len(A)
        if n == 0:
            return 0
        m = len(A[0])
        for i in range(n):
            for j in range(m):
                A[i][j] = int(A[i][j])
                if i != 0 and j != 0:
                    if A[i][j] == 1:
                        A[i][j] = min(A[i-1][j-1],A[i-1][j],A[i][j-1])+1
        return max(map(max,A))**2