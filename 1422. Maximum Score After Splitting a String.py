class Solution:
    def maxScore(self, s: str) -> int:
        d1 = collections.Counter(s)
        d2 = {'0':0,'1':0}
        
        m = 0
        for i in range(0,len(s)-1):
            d2[s[i]] += 1
            m = max(m, (d1['1']-d2['1']) + d2['0'])
        return m