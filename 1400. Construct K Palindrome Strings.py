class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        if k == n:
            return True
        
        d = collections.Counter(s)
        count = 0
        for i in list(d.keys()):
            if d[i]%2 == 1:
                count += 1
        
        return count <= k