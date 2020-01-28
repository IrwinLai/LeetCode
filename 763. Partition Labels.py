class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rightmost = {c:i for i, c in enumerate(S)}
        
        left,right = 0,0
        ret = []
        for i,c in enumerate(S):
            right = max(right,rightmost[c])
            if i == right:
                ret.append(right-left+1)
                left = right+1
        return ret
        
        '''
        d1 = collections.Counter(S)
        ret = []
        i = 0
        d2 = {}
        for j in range(len(S)):
            d2[S[j]] = d2.get(S[j],0) + 1
            if sum(d2[k] == d1[k] for k in list(d2.keys())) == len(d2):
                ret.append(j-i+1)
                i = j+1
                d2 = {}
        return ret
        '''