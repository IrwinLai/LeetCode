class Solution:
    def hasValidPath(self, g: List[List[int]]) -> bool:
        m = len(g)
        n = len(g[0])
        i,j = 0,0
        count = 0
        
        def helper(i,j,t='i'):
            if i==m-1 and j == n-1:
                if (t == 'r' and g[i][j] in [1,3,5]) or (t == 'l' and g[i][j] in [1,4,6]) \
                    or (t == 'u' and g[i][j] in [2,3,4]) or (t == 'd' and g[i][j] in [2,5,6]):
                    return i,j
                else:
                    return 0,0
                    
            if 0<=i<m and 0<=j<n:
                if t == 'i':
                    if g[i][j] == 1:return helper(i,j+1,'r')
                    elif g[i][j] == 2:return helper(i+1,j,'d')
                    elif g[i][j] == 3:return helper(i+1,j,'d')
                    elif g[i][j] == 4:return helper(i+1,j,'d')
                    elif g[i][j] == 6:return helper(i,j+1,'r')
                if t == 'r':
                    if g[i][j] == 1:return helper(i,j+1,'r')
                    elif g[i][j] == 3:return helper(i+1,j,'d')
                    elif g[i][j] == 5:return helper(i-1,j,'u')
                if t == 'l':
                    if g[i][j] == 1:return helper(i,j-1,'l')
                    elif g[i][j] == 4:return helper(i+1,j,'d')
                    elif g[i][j] == 6:return helper(i-1,j,'u')
                if t == 'u':
                    if g[i][j] == 2:return helper(i-1,j,'u')
                    elif g[i][j] == 3:return helper(i,j-1,'l')
                    elif g[i][j] == 4:return helper(i,j+1,'r')
                if t == 'd':
                    if g[i][j] == 2:return helper(i+1,j,'d')
                    elif g[i][j] == 5:return helper(i,j-1,'l')
                    elif g[i][j] == 6:return helper(i,j+1,'r')
            return i,j
        
        i,j = helper(0,0,'i')
        return i == m-1 and j == n-1