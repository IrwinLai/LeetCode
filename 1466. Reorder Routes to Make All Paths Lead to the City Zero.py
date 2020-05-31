class Solution:
    def minReorder(self, n: int, c: List[List[int]]) -> int:
        # from 0, reverse all the point which doesn't point to 0
        self.res = 0
        roads = set()
        graph = collections.defaultdict(list)
        
        for x,y in c:
            roads.add((x,y))
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(child,parent): # parent point to child
            # find reverse
            if (parent,child) in roads:
                self.res += 1
            for c in graph[child]:
                if c != parent:
                    dfs(c,child)
        
        dfs(0,-1)
        return self.res