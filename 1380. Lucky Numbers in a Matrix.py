class Solution:
    def luckyNumbers (self, A: List[List[int]]) -> List[int]:
        if A == []:
            return []
        m = len(A)
        n = len(A[0])
        minrow = [[0]*n for i in range(m)]
        maxcol = [[0]*n for i in range(m)]
        AT = [[0]*m for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                AT[j][i] = A[i][j]
                
        for i in range(m):
            for j in range(n):
                if A[i][j] == min(A[i]):
                    minrow[i][j] = 1
                if A[i][j] == max(AT[j]):
                    maxcol[i][j] = 1
                    
        ret = []
        for i in range(m):
            for j in range(n):
                if minrow[i][j] == 1 and maxcol[i][j] == 1:
                    ret.append(A[i][j])
        
        return ret
        
        