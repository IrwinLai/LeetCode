class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        l = list(d.keys())
        l.sort(key = lambda x:d[x], reverse = True)
        ret = []
        for i in range(k):
            ret.append(l[i])
        return ret