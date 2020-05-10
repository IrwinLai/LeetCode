class Solution:
    def minTime(self, n: int, edges: List[List[int]], A: List[bool]) -> int:
        d = {}
        check = set()
        visited = set()
        ans = 0
        
        for i in range(n-1):
            d[edges[i][1]] = edges[i][0]
        for i in range(1,n):
            if A[i] == True:
                check.add(i)
                visited.add(i)
                
        if A[0] == 0:
            visited.add(0)
            
        while check:
            tem = []
            print(check,visited)
            for i in check:
                if d[i]!= 0 and d[i] not in visited:
                    tem.append(d[i])
                    visited.add(d[i])
                ans += 2
            check = set(tem)
        return ans