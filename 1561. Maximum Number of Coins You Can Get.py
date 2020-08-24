class Solution:
    def maxCoins(self, p: List[int]) -> int:
        p = list(sorted(p))[::-1]
        ret = 0
        
        while p:
            p.pop(0)
            ret += p.pop(0)
            p.pop(-1)
            
        return ret
        
        