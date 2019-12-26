class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        l = sorted(arr)
        ret = []
        t1 = l[-1] - l[0]
        for i in range(len(l) - 1):
            t2 = l[i+1] - l[i]
            if t2 < t1:
                t1 = t2
                ret = [[l[i],l[i+1]]]
            elif t2 == t1:
                ret.extend([[l[i],l[i+1]]])
        return ret
            