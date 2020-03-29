class Solution:
    def findLucky(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return -1
        d = collections.Counter(arr)
        k = sorted(list(d.keys()))
        for i in k[::-1]:
            if i == d[i]:
                return i
        return -1