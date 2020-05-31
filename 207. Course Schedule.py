class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        # create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
            
    
        # visited = 1 is visiting it now
        # visited = 2 is done visited
        def dfs(graph,visited,i):
            if visited[i] == 1:
                return False
            if visited[i] == 2:
                return True
            visited[i] = 1
            for j in graph[i]:
                if not dfs(graph, visited, j):
                    return False
            visited[i] = 2
            return True
        
        
        # visit each node
        for i in range(numCourses):
            if not dfs(graph, visited, i):
                return False
        return True