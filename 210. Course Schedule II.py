class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        # top algorithm
        
        
        res = []
        d_parent,d_child = {i:[] for i in range(n)},{i:[] for i in range(n)}
        # parent point to child / child be pointed
        for x,y in pre:
            d_parent[y].append(x)
            d_child[x].append(y)
            
        '''
        # bfs
        check = [i for i in d_child if len(d_child[i])==0]
        count = 0
        while check:
            node = check.pop(0)
            res.append(node)
            count += 1
            # update
            for i in d_parent[node]:
                d_child[i].remove(node)
                if len(d_child[i]) == 0:
                    check.append(i)
            
        return res if count == n else []
        '''
        
        # dfs
        stack = [i for i in d_child if len(d_child[i])==0]
        while stack:
            # stack is FILO, and pop in list is the last item for default
            node = stack.pop(0)
            res.append(node)
            for i in d_parent[node]:
                d_child[i].remove(node)
                if len(d_child[i]) == 0:
                    stack.append(i)
            d_child.pop(node)
        return res if not d_child else []
                
        