class Solution:
    def frequencySort(self, s: str) -> str:
        d = collections.Counter(s)
        l = list(d.keys())
        l.sort(key = lambda x:-d[x])
        ret = ''
        for i in l:
            ret += i*d[i]
        return ret