class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = collections.Counter(text)
        ret = []
        for i in ['b','a','n']:
            ret.append(d.get(i,0))
        ret.append(d.get('l',0)//2)
        ret.append(d.get('o',0)//2)
        return min(ret)