class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        seen = set()
        def dfs(node):
            for nei, adj in enumerate(M[node]):
                if adj == 1 and nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        ret = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ret += 1
        return ret

        '''
        n = len(M)
        dj = [i for i in range(n)]
        
        for i in range(n-1):
            for j in range(i+1,n):
                if M[i][j] == 1:
                    tem1 = dj[i]
                    tem2 = dj[j]
                    for k in range(n):
                        if dj[k] == tem1 or dj[k] == tem2:
                            dj[k] = min(tem1,tem2)
        
        return len(set(dj))
       '''