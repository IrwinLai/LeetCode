class Solution:
    def minNumberOfFrogs(self, s: str) -> int:
        d = collections.Counter(s)
        n = d['c']
        if d['r'] != n or d['o'] != n or d['a'] != n or d['k'] != n:
            return -1
        
        d = {}
        ans = 0
        for i in s:
            d[i] = d.get(i,0) + 1
            if i == "r":
                if d[i] > d.get('c',0):
                    return -1
            if i == "o":
                if d[i] > d.get('r',0):
                    return -1
            if i == "a":
                if d[i] > d.get('a',0):
                    return -1
            if i == "k":
                if d[i] > d.get('k',0):
                    return -1
            ans = max(ans,d[i])
            if d.get('c',0) > 0 and d.get('r',0) > 0 and d.get('o',0) > 0 and d.get('a',0) > 0 and d.get('k',0) > 0:
                for k in ['c','r','o','a','k']:
                    d[k] = d.get(k,0) - 1
                    
        for i in ['c','r','o','a','k']:
            if d['c'] != 0:
                return -1
        return ans