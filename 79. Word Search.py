class Solution:
    def exist(self, A: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return True
        m = len(A)
        if m == 0:
            return False
        n = len(A[0])
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        
        def dfs(path,i,j, flag = 0):
            if flag == 0:
                tem = A[i][j]
                A[i][j] = '#'    # smart move!
                for a,b in direction:
                    x,y = i+a,j+b
                    if 0<=x<m and 0<=y<n and A[x][y] == path[0]:
                        if len(path) == 1:
                            flag = 1
                            break
                        else:
                            flag = dfs(path[1:],x,y,flag)
                A[i][j] = tem
            return flag
                    
        for i in range(m):
            for j in range(n):
                if A[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    elif dfs(word[1:],i,j,0) == 1:
                        return True
        
        return False