class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dj = [i for i in range(n+1)]
        
        def find(u):
            if u != dj[u]:
                dj[u] = find(dj[u])
            return dj[u]
            
        def union(u,v):
            tem1 = find(u)
            tem2 = find(v)
            if tem1 == tem2: # u, v in set already
                return 0
            else:
                dj[tem1] = tem2
            return 1
        
        for item in edges:
            if(union(item[0],item[1]) == 0):
                return item
        