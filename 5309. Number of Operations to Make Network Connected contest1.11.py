class Solution:
    def makeConnected(self, n: int, c: List[List[int]]) -> int:
        if len(c) < n-1:
            return -1
        d = {}
        k = {}
        for i in range(n):
            d[i] = i
            k[i] = set([i])
        sz = n
        
        for item in c:
            t = min([d[i] for i in item])
            for i in item:
                if d[i] != t:
                    for j in k[d[i]]:
                        d[j] = t   # everyone point to the smallest one in this circle
                        k[t].add(j)  # add in this circle
                    d[i] = t
                    k[t].add(i)
                    k[i] = set()
        return len(set(d.values()))-1
    