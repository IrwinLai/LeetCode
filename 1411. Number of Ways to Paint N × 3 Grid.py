class Solution:
    def numOfWays(self, n: int) -> int:
        t = [6]
        d = [6]
        
        for i in range(n-1):
            temt = t[-1]
            temd = d[-1]
            t.append(2*temt+2*temd)
            d.append(2*temt+3*temd)
        
        return (t[-1]+d[-1])%(10**9 + 7)