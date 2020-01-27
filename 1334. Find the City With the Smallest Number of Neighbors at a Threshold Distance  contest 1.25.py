class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], t: int) -> int:
        d = [[float('inf')] * n for i in range(n)]
        for i,j,k in edges:
            d[i][j] = d[j][i] = k
        for i in range(n):
            d[i][i] = 0
        
        # floyd
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][k]+d[k][j], d[i][j])
                    
        #print(d)
        ret = n
        ans = 0
        for i in range(n):
            if ret >= sum(j <= t for j in d[i]) and ans <= i:
                ans = i
                ret = sum(j <= t for j in d[i])
        return ans