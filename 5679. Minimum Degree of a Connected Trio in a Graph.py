class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = [[0]*(n+1) for _ in range(n+1)] 
        node = [0]*(n+1)
        for i,j in edges:
            graph[i][j] = 1
            graph[j][i] = 1
            node[i] += 1
            node[j] += 1
        trio = 0
        ans = float('inf')
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if graph[i][j] == 1:
                    for k in range(j+1,n+1):
                        if graph[i][k] and graph[j][k]:
                            trio = 1
                            ans = min(ans,node[i]+node[j]+node[k] - 6)
                            
        if trio == 0:
            return -1
        return ans