class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = collections.Counter(arr)
        l = sorted(list(d.keys()),key = lambda x:d[x])
        tem = 0
        for i in range(len(l)):
            tem += d[l[i]]
            if tem == k:
                return len(d) - i -1
            if tem > k:
                return len(d) - i
        return len(d) - i -1