class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        t1 = len(S)
        t2 = 0
        S += "I"
        ret = []
        for i in S:
            if i == 'I':
                ret.append(t2)
                t2 += 1
            else:
                ret.append(t1)
                t1 -= 1
        return ret