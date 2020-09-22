class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        l1 = []
        l2 = []
        for i in range(m):
            if sum(mat[i]) == 1:
                for j in range(n):
                    if mat[i][j] == 1:
                        l1.append((i,j))
                        
        for j in range(n):
            c = 0
            for i in range(m):
                c += mat[i][j]
            if c == 1:
                for i in range(m):
                    if mat[i][j] == 1:
                        l2.append((i,j))
        
        return len(set(l1)&set(l2))
        