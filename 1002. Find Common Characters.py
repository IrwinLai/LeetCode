class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        d1 = collections.Counter(A[0])
        for a in A[1:]:
            d2 = collections.Counter(a)
            for i in d1.keys():
                d1[i]= min(d1[i],d2.get(i,0))
        
        res = []
        for i in d1.keys():
            if d1[i] > 0:
                res.extend([i]*d1[i])
        return res