class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a = A.split(' ')
        b = B.split(' ')
        da = collections.Counter(a)
        db = collections.Counter(b)
        s = list((set(a)|set(b)) - (set(a)&set(b)))
        print(da,db,s)
        ret = []
        for i in s:
            if da.get(i,0) < 2 and db.get(i,0) < 2:
                ret.append(i)
        return ret