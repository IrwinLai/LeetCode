class Solution:
    def diagonalSort(self, A: List[List[int]]) -> List[List[int]]:
        n,m = len(A), len(A[0])
        d = collections.defaultdict(list)
        
        for i in range(n):
            for j in range(m):
                d[i - j].append(A[i][j])
                
        for k in d:
            d[k].sort(reverse=True)
            
        for i in range(n):
            for j in range(m):
                A[i][j] = d[i - j].pop()
        return A
        
        '''
        m = len(mat)
        n = len(mat[0])
        for k in range(n):
            i = 0
            j = k
            tem = []
            while(j < n and i < m):
                tem.append(mat[i][j])
                i+=1
                j+=1
            tem.sort()
            i = 0
            j = k
            while(j < n and i < m):
                mat[i][j] = tem[i]
                i+=1
                j+=1
                
        for k in range(m):
            i = k
            j = 0
            tem = []
            while(j < n and i < m):
                tem.append(mat[i][j])
                i+=1
                j+=1
            tem.sort()
            i = k
            j = 0
            while(j < n and i < m):
                mat[i][j] = tem[j]
                i+=1
                j+=1
        
        return mat
        '''