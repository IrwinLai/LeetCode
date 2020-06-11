class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = collections.Counter(p)
        n = len(p)
        
        ret = []
        for i in range(len(s)-n+1):
            if i == 0:
                d = collections.Counter(s[:n])
            else:
                d[s[i-1]] = d.get(s[i-1],0) - 1
                d[s[i+n-1]] = d.get(s[i+n-1],0) + 1 
            if all(d.get(i,0) == target[i] for i in target):
                ret.append(i)
                
        return ret
            