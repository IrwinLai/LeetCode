class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr)  == 1:
            return [1]
        rank = sorted(list(set(arr)))
        d = {}
        for i in range(len(rank)):
            d[rank[i]] = i
        ret = []
        for i in arr:
            ret.append(d[i]+1)
        return ret