class Solution:
    def rankTeams(self, v: List[str]) -> str:
        if len(v) == 1:
            return v[0]
        
        t = 100000000
        res = list(v[0])
        d = {}
        for i in res:
            d[i] = 0
            
        for i in v:
            for j in range(len(i)):
                d[i[j]] += t/1000**j
        
        
        res.sort(key = lambda x:(-d[x],x))
        
        return "".join(res)